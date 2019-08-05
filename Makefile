# USE_REDIS = -DUSE_REDIS
ifdef USE_REDIS
	LREDIS = -lhiredis
	OREDIS = redis_tool.o
endif

CURR_DIR := $(shell pwd)/$(lastword $(MAKEFILE_LIST))
CURR_DIR := $(shell dirname $(CURR_DIR))

SOURCES = $(wildcard *.c) $(wildcard */*.c)
TARGET = exchange
# OBJECTS = exchange_main.o log.o error.o base64.o config.o mq.o tool.o queue.o $(OREDIS)
#
# $(warning "SOURCES is $(SOURCES)")
ifndef USE_REDIS
	SOURCES := $(filter-out redis/redis_tool.c, $(SOURCES))
endif
# $(warning "after SOURCES is $(SOURCES)")
OBJECTS = $(patsubst %.c, %.o, $(SOURCES))
MQ_INSTALL_PATH = /opt/mqm
# CC_FLAGS = -std=c11 -m64 -I $(MQ_INSTALL_PATH)/inc -L $(MQ_INSTALL_PATH)/lib64 -Wl,-rpath=$(MQ_INSTALL_PATH)/lib64 -Wl,-rpath=/usr/lib64


CC = gcc
DEFS += $(USE_REDIS)
CC_FLAGS += $(DEFS) -std=c11 -O3 -m64 -Wall -I $(MQ_INSTALL_PATH)/inc -I include
CC_STATIC_LINK = -L $(CURR_DIR)/lib -lcjson
CC_LINK_FLAGS = -L $(MQ_INSTALL_PATH)/lib64 -lmqic_r -lpthread -luuid $(LREDIS)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CC_FLAGS) $(CC_LINK_FLAGS) -o $@ $^ $(CC_STATIC_LINK)

$(OBJECTS): %.o : %.c
	$(CC) -c $(CC_FLAGS) -Wp,-MMD,$@.d -o $@ $<

-include *.o.d
-include **/*.o.d

cjson:
	cd lib/cJSON/ && \
	mkdir -v build && \
	cd build && \
	cmake -DBUILD_SHARED_LIBS=Off .. && \
	make && \
	cp -v libcjson.a ../../

clean:
	-rm -vf *.h.gch
	-rm -vf **/*.h.gch
	-rm -vf *.o
	-rm -vf **/*.o
	-rm -vf *.o.d
	-rm -vf **/*.o.d
	-rm -vf $(TARGET)
