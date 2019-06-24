## 首先安装rpm目录中的mq客户端

## setting LD_LIBRARY_PATH
(e.g. LD_LIBRARY_PATH=/opt/mqm/lib64:/usr/lib64)

## copy lib/libcjson.so.1.7.12 to /usr/lib64
    ```
    ln -svf libcjson.so.1.7.12 /usr/lib64/libcjson.so
    ln -svf libcjson.so.1.7.12 /usr/lib64/libcjson.so.1
    ```
