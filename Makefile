# USE_REDIS = -DUSE_REDIS
ifdef USE_REDIS
	LREDIS = -lhiredis
	OREDIS = redis_tool.o
endif

CURR_DIR := $(shell pwd)/$(lastword $(MAKEFILE_LIST))
CURR_DIR := $(shell dirname $(CURR_DIR))

TARGET = exchange
OBJECTS = exchange_main.o log.o error.o base64.o config.o mq.o tool.o queue.o $(OREDIS)
MQ_INSTALL_PATH = /opt/mqm
# CC_FLAGS = -std=c11 -m64 -I $(MQ_INSTALL_PATH)/inc -L $(MQ_INSTALL_PATH)/lib64 -Wl,-rpath=$(MQ_INSTALL_PATH)/lib64 -Wl,-rpath=/usr/lib64


DEFS += $(USE_REDIS)
CC_FLAGS += $(DEFS) -std=c11 -O3 -m64 -I $(MQ_INSTALL_PATH)/inc -I include
CC_STATIC_LINK = -L $(CURR_DIR)/lib -lcjson
CC_LINK_FLAGS = -L $(MQ_INSTALL_PATH)/lib64 -lmqic_r -lpthread -luuid $(LREDIS)

$(TARGET): $(OBJECTS)
	cc $(CC_FLAGS) $(CC_LINK_FLAGS) -o $@ $^ $(CC_STATIC_LINK)

log.o: log/log.c log/log.h
	cc $(CC_FLAGS) -c $^

error.o: err/error.c err/error.h
	cc $(CC_FLAGS) -c $^

base64.o: base64/base64.c base64/base64.h
	cc $(CC_FLAGS) -c $^

config.o: config/config.c config/config.h
	cc $(CC_FLAGS) -c $^

redis_tool.o: redis/redis_tool.c redis/redis_tool.h
	cc $(CC_FLAGS) -c $^

mq.o: mq.c mq.h
	cc $(CC_FLAGS) -c $^

tool.o: tool/tool.c tool/tool.h
	cc $(CC_FLAGS) -c $^

queue.o: queue/queue.c queue/queue.h
	cc $(CC_FLAGS) -c $^

exchange_main.o: exchange_main.c log/log.h err/error.h mq.h
	cc $(CC_FLAGS) -c $^

cjson:
	cd lib/cJSON/ && \
	mkdir -v build && \
	cd build && \
	cmake -DBUILD_SHARED_LIBS=Off .. && \
	make && \
	cp -v libcjson.a ../../

%.o: %.c
	@echo "using generic rule"
	cc $(CC_FLAGS) -c $<

clean:
	-rm -vf *.h.gch
	-rm -vf **/*.h.gch
	-rm -vf *.o
	-rm -vf $(TARGET)
