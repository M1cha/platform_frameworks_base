LOCAL_PATH:= $(call my-dir)

include $(CLEAR_VARS)

ifeq ($(BOARD_HAVE_FMRADIO_SUPPORT),STERICSSON_FMRADIO_SUPPORT)
        LOCAL_CFLAGS += -DSTERICSSON_FMRADIO_SUPPORT
endif

LOCAL_SRC_FILES:=               \
    AudioFlinger.cpp            \
    AudioMixer.cpp.arm          \
    AudioResampler.cpp.arm      \
    AudioResamplerSinc.cpp.arm  \
    AudioResamplerCubic.cpp.arm \
    AudioPolicyService.cpp

LOCAL_C_INCLUDES := \
    system/media/audio_effects/include

LOCAL_SHARED_LIBRARIES := \
    libcutils \
    libutils \
    libbinder \
    libmedia \
    libhardware \
    libhardware_legacy \
    libeffects \
    libdl \
    libpowermanager

LOCAL_STATIC_LIBRARIES := \
    libcpustats \
    libmedia_helper

LOCAL_MODULE:= libaudioflinger

include $(BUILD_SHARED_LIBRARY)
