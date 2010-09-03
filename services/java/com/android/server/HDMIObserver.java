/*
 * Copyright (C) 2008 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.android.server;

import android.app.ActivityManagerNative;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.os.Message;
import android.os.PowerManager;
import android.os.PowerManager.WakeLock;
import android.os.UEventObserver;
import android.util.Slog;
import android.media.AudioManager;

import java.io.FileReader;
import java.io.FileNotFoundException;

/**
 * <p>HDMIObserver monitors for HDMI connection.
 */
class HDMIObserver extends UEventObserver {
    private static final String TAG = HDMIObserver.class.getSimpleName();
    private static final boolean LOG = true;

    private static final String HDMI_UEVENT_MATCH = "DEVPATH=/devices/virtual/switch/hdmi";
    private static final String HDMI_STATE_PATH = "/sys/class/switch/hdmi/state";
    private static final String HDMI_NAME_PATH = "/sys/class/switch/hdmi/name";

    private int mHDMIState;
    private int mPrevHDMIState;
    private String mHDMIName;

    private final Context mContext;
    private final WakeLock mWakeLock;  // held while there is a pending route change

    private static final String ACTION_HDMI_PLUG = "android.intent.action.HDMI_PLUG";

    public HDMIObserver(Context context) {
        mContext = context;
        PowerManager pm = (PowerManager)context.getSystemService(Context.POWER_SERVICE);
        mWakeLock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "HDMIObserver");
        mWakeLock.setReferenceCounted(false);

        startObserving(HDMI_UEVENT_MATCH);

        init();  // set initial status
    }

    @Override
    public void onUEvent(UEventObserver.UEvent event) {
        if (LOG) Slog.v(TAG, "HDMI UEVENT: " + event.toString());

        try {
            update(event.get("SWITCH_NAME"), Integer.parseInt(event.get("SWITCH_STATE")));
        } catch (NumberFormatException e) {
            Slog.e(TAG, "Could not parse switch state from event " + event);
        }
    }

    private synchronized final void init() {
        char[] buffer = new char[1024];

        String newName = mHDMIName;
        int newState = mHDMIState;
        mPrevHDMIState = mHDMIState;
        try {
            FileReader file = new FileReader(HDMI_STATE_PATH);
            int len = file.read(buffer, 0, 1024);
            newState = Integer.valueOf((new String(buffer, 0, len)).trim());

            file = new FileReader(HDMI_NAME_PATH);
            len = file.read(buffer, 0, 1024);
            newName = new String(buffer, 0, len).trim();
        } catch (FileNotFoundException e) {
            Slog.w(TAG, "This kernel does not have HDMI support");
        } catch (Exception e) {
            Slog.e(TAG, "" , e);
        }

        update(newName, newState);
    }

    private synchronized final void update(String newName, int newState) {
        // Retain only relevant bits
        int HDMIState = newState;
        int newOrOld = HDMIState | mHDMIState;
        int delay = 0;
        if (((newOrOld & (newOrOld - 1)) != 0)) {
            return;
        }

        mHDMIName = newName;
        mPrevHDMIState = mHDMIState;
        mHDMIState = HDMIState;

        mWakeLock.acquire();
        mHandler.sendMessageDelayed(mHandler.obtainMessage(0,
                                                           mHDMIState,
                                                           mPrevHDMIState,
                                                           mHDMIName),
                                    delay);
    }

    private synchronized final void sendIntents(int HDMIState, int prevHDMIState, String HDMIName) {
       int curHDMI = 1;
       int allHDMI = 1;
       sendIntent(curHDMI, HDMIState, prevHDMIState, HDMIName);
    }

    private final void sendIntent(int HDMI, int HDMIState, int prevHDMIState, String HDMIName) {
        if ((HDMIState & HDMI) != (prevHDMIState & HDMI)) {
            //  Pack up the values and broadcast them to everyone
            Intent intent = new Intent(ACTION_HDMI_PLUG);
            intent.addFlags(Intent.FLAG_RECEIVER_REGISTERED_ONLY);
            int state = 0;
            if ((HDMIState & HDMI) != 0) {
                state = 1;
            }
            intent.putExtra("state", state);
            intent.putExtra("name", HDMIName);

            if (LOG) Slog.e(TAG, "ACTION_HDMI_PLUG: state: "+state+" name: "+HDMIName);
            // TODO: Should we require a permission?
            ActivityManagerNative.broadcastStickyIntent(intent, null);
        }
    }

    private final Handler mHandler = new Handler() {
        @Override
        public void handleMessage(Message msg) {
            sendIntents(msg.arg1, msg.arg2, (String)msg.obj);
            mWakeLock.release();
        }
    };
}
