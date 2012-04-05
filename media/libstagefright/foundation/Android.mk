LOCAL_PATH:= $(call my-dir)
include $(CLEAR_VARS)

ifeq ($(BOARD_HAVE_CODEC_SUPPORT),STERICSSON_CODEC_SUPPORT)
        LOCAL_CFLAGS += -DSTERICSSON_CODEC_SUPPORT
endif

LOCAL_SRC_FILES:=                 \
    AAtomizer.cpp                 \
    ABitReader.cpp                \
    ABuffer.cpp                   \
    AHandler.cpp                  \
    AHierarchicalStateMachine.cpp \
    ALooper.cpp                   \
    ALooperRoster.cpp             \
    AMessage.cpp                  \
    AString.cpp                   \
    base64.cpp                    \
    hexdump.cpp

LOCAL_C_INCLUDES:= \
    frameworks/base/include/media/stagefright/foundation

LOCAL_SHARED_LIBRARIES := \
        libbinder         \
        libutils          \

LOCAL_CFLAGS += -Wno-multichar

LOCAL_MODULE:= libstagefright_foundation



include $(BUILD_SHARED_LIBRARY)
