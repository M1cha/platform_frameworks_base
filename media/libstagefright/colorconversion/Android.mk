LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

ifeq ($(BOARD_HAVE_CODEC_SUPPORT),STERICSSON_CODEC_SUPPORT)
        LOCAL_CFLAGS += -DSTERICSSON_CODEC_SUPPORT
endif

LOCAL_SRC_FILES:=                     \
        ColorConverter.cpp            \
        SoftwareRenderer.cpp

LOCAL_C_INCLUDES := \
        $(TOP)/frameworks/base/include/media/stagefright/openmax \
        $(TOP)/hardware/msm7k

LOCAL_MODULE:= libstagefright_color_conversion

include $(BUILD_STATIC_LIBRARY)
