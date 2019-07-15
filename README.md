## 首先安装rpm目录中的mq客户端

## 如果lib下的静态库没有或者需要重新编译需要拉取子模块
```
git submodule update --init --recursive

执行 make cjson来生成cjson的静态库
```

## setting LD_LIBRARY_PATH
(e.g. LD_LIBRARY_PATH=/opt/mqm/lib64:/usr/lib64)

# 执行编译命令
```
make
```
