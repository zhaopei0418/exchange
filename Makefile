TARGET = exchange
OBJECTS = exchange.o log.o error.o base64.o
MQ_INSTALL_PATH = /opt/mqm
#CC_FLAGS = -std=c11 -m64 -I $(MQ_INSTALL_PATH)/inc -L $(MQ_INSTALL_PATH)/lib64 -Wl,-rpath=$(MQ_INSTALL_PATH)/lib64 -Wl,-rpath=/usr/lib64
CC_FLAGS = -std=c11 -m64 -I $(MQ_INSTALL_PATH)/inc -L $(MQ_INSTALL_PATH)/lib64 \
		   -I include -L lib -lmqic_r -lpthread -luuid -lcjson

$(TARGET): $(OBJECTS)
	cc $(CC_FLAGS) -o $@ $^

log.o: log/log.c log/log.h
	cc $(CC_FLAGS) -c $< $

error.o: err/error.c err/error.h
	cc $(CC_FLAGS) -c $< $

base64.o: base64/base64.c base64/base64.h
	cc $(CC_FLAGS) -c $< $

exchange.o: exchange.c log/log.h err/error.h
	cc $(CC_FLAGS) -c $< $

%.o: %.c
	@echo "using generic rule"
	cc $(CC_FLAGS) -c $< $

clean:
	-rm *.o
	-rm $(TARGET)
