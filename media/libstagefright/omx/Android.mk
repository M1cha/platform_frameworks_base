LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

ifeq ($(BOARD_HAVE_CODEC_SUPPORT),STERICSSON_CODEC_SUPPORT)
        LOCAL_CFLAGS += -DSTERICSSON_CODEC_SUPPORT
endif

LOCAL_C_INCLUDES += $(JNI_H_INCLUDE)

LOCAL_SRC_FILES:=                     \
        OMX.cpp                       \
        OMXComponentBase.cpp          \
        OMXMaster.cpp                 \
        OMXNodeInstance.cpp           \
        SimpleSoftOMXComponent.cpp    \
        SoftOMXComponent.cpp          \
        SoftOMXPlugin.cpp             \

LOCAL_C_INCLUDES += \
        frameworks/base/media/libstagefright \
        $(TOP)/frameworks/base/include/media/stagefright/openmax

LOCAL_SHARED_LIBRARIES :=               \
        libbinder                       \
        libmedia                        \
        libutils                        \
        libui                           \
        libcutils                       \
        libstagefright_foundation       \
        libdl

LOCAL_MODULE:= libstagefright_omx

include $(BUILD_SHARED_LIBRARY)

################################################################################

include $(call all-makefiles-under,$(LOCAL_PATH))
