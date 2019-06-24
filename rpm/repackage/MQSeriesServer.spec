Summary: IBM MQ Server FileSet
Name: MQSeriesServer
Version: 9.0.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesRuntime = 9.0.0-0
%define _source_filedigest_algorithm md5
%define _binary_filedigest_algorithm md5
%define _source_payload w7.lzdio
%define _binary_payload w7.lzdio
%global __strip /bin/true
%global _rpmdir /build/slot2/p900_P/inst.images/amd64_linux_2/images/
%global _tmppath /build/slot2/p900_P/obj/amd64_linux_2/install/unix/linux_2
BuildRoot: /build/slot2/p900_P/obj/amd64_linux_2/ship

%description
IBM MQ for Developers for Linux for x86_64 
5724-H72 
This package provides the queue manager messaging and queuing services for
IBM MQ.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/lib
install -d $RPM_BUILD_ROOT/opt/mqm/lib/compat
install -d $RPM_BUILD_ROOT/opt/mqm/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/lib64/compat
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/inc
install -d $RPM_BUILD_ROOT/opt/mqm/bin/security
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc
install -d $RPM_BUILD_ROOT/opt/mqm/java/bin
install -d $RPM_BUILD_ROOT/opt/mqm/doc
install -d $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz
install -d $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/de_de
install -d $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/en_us
install -d $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/es_es
install -d $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr
install -d $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu
install -d $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/it_it
install -d $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp
install -d $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr
install -d $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl
install -d $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/pt_br
install -d $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru
install -d $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn
install -d $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info
install -d $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw
install -d $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqbrk $RPM_BUILD_ROOT/opt/mqm/bin/runmqbrk
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqfcxba $RPM_BUILD_ROOT/opt/mqm/bin/amqfcxba
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dltmqbrk $RPM_BUILD_ROOT/opt/mqm/bin/dltmqbrk
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqbrk $RPM_BUILD_ROOT/opt/mqm/bin/endmqbrk
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqfqpub $RPM_BUILD_ROOT/opt/mqm/bin/amqfqpub
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqcrsta $RPM_BUILD_ROOT/opt/mqm/bin/amqcrsta
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqpcsea $RPM_BUILD_ROOT/opt/mqm/bin/amqpcsea
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzif_r $RPM_BUILD_ROOT/opt/mqm/lib64/amqzif_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzfu $RPM_BUILD_ROOT/opt/mqm/lib64/amqzfu
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzfud $RPM_BUILD_ROOT/opt/mqm/lib64/amqzfud
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmz1_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmz1_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzfuma $RPM_BUILD_ROOT/opt/mqm/bin/amqzfuma
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqoamd $RPM_BUILD_ROOT/opt/mqm/bin/amqoamd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/security/amqoamax $RPM_BUILD_ROOT/opt/mqm/bin/security/amqoamax
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/security/amqoampx $RPM_BUILD_ROOT/opt/mqm/bin/security/amqoampx
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/security/amqpamcf $RPM_BUILD_ROOT/opt/mqm/bin/security/amqpamcf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzsc $RPM_BUILD_ROOT/opt/mqm/lib/amqzsc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzscg $RPM_BUILD_ROOT/opt/mqm/lib/amqzscg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcics_r.a $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcics_r.a
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzlaa0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzlaa0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzlsa0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzlsa0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzxma0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzxma0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmgr0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmgr0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmuc0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmuc0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmuf0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmuf0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzmur0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzmur0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqm $RPM_BUILD_ROOT/opt/mqm/bin/crtmqm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dltmqm $RPM_BUILD_ROOT/opt/mqm/bin/dltmqm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqaut $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqaut
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqcsv $RPM_BUILD_ROOT/opt/mqm/bin/dspmqcsv
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqfls $RPM_BUILD_ROOT/opt/mqm/bin/dspmqfls
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqaut $RPM_BUILD_ROOT/opt/mqm/bin/dspmqaut
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqtrn $RPM_BUILD_ROOT/opt/mqm/bin/dspmqtrn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmq $RPM_BUILD_ROOT/opt/mqm/bin/dspmq
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqrte $RPM_BUILD_ROOT/opt/mqm/bin/dspmqrte
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqaut $RPM_BUILD_ROOT/opt/mqm/bin/setmqaut
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqcsv $RPM_BUILD_ROOT/opt/mqm/bin/endmqcsv
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqm $RPM_BUILD_ROOT/opt/mqm/bin/endmqm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/rcdmqimg $RPM_BUILD_ROOT/opt/mqm/bin/rcdmqimg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/rcrmqobj $RPM_BUILD_ROOT/opt/mqm/bin/rcrmqobj
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqchi $RPM_BUILD_ROOT/opt/mqm/bin/runmqchi
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqlsr $RPM_BUILD_ROOT/opt/mqm/bin/runmqlsr
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runswchl $RPM_BUILD_ROOT/opt/mqm/bin/runswchl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrcmla $RPM_BUILD_ROOT/opt/mqm/bin/amqrcmla
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrrmfa $RPM_BUILD_ROOT/opt/mqm/bin/amqrrmfa
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrmppa $RPM_BUILD_ROOT/opt/mqm/bin/amqrmppa
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqzlwa0 $RPM_BUILD_ROOT/opt/mqm/bin/amqzlwa0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqlsr $RPM_BUILD_ROOT/opt/mqm/bin/endmqlsr
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqchl $RPM_BUILD_ROOT/opt/mqm/bin/runmqchl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqtrm $RPM_BUILD_ROOT/opt/mqm/bin/runmqtrm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/rsvmqtrn $RPM_BUILD_ROOT/opt/mqm/bin/rsvmqtrn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/addmqinf $RPM_BUILD_ROOT/opt/mqm/bin/addmqinf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqinf $RPM_BUILD_ROOT/opt/mqm/bin/dspmqinf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/rmvmqinf $RPM_BUILD_ROOT/opt/mqm/bin/rmvmqinf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqsstop $RPM_BUILD_ROOT/opt/mqm/bin/amqsstop
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqm $RPM_BUILD_ROOT/opt/mqm/bin/setmqm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqprd $RPM_BUILD_ROOT/opt/mqm/bin/setmqprd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqspl $RPM_BUILD_ROOT/opt/mqm/bin/dspmqspl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqspl $RPM_BUILD_ROOT/opt/mqm/bin/setmqspl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqm $RPM_BUILD_ROOT/opt/mqm/bin/strmqm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqcsv $RPM_BUILD_ROOT/opt/mqm/bin/strmqcsv
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqml_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqml_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqml_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqml_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmalda_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmalda_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmaldb_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmaldb_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmzf.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzf.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmzf.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzf.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmzf_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzf_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmzf_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzf_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqutl.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqutl.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqutl.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqutl.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqutl_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqutl_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqutl_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqutl_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzi.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzi.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzi.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzi.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzi_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzi_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzi_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzi_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqds.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqds.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqds.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqds.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqds_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqds_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqds_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqds_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmr.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmr.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmr.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmr.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmr_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmr_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmr_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmr_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcb.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcb.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcb.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcb.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcb_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcb_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcb_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcb_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcbrt.o $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcbrt.o
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmxa.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmxa.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa64.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa64.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmxa_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmxa_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmxa64_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmxa64_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmax.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmax.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmax_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmax_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax64.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax64.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmax64_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmax64_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzaax $RPM_BUILD_ROOT/opt/mqm/lib/amqzaax
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzaax $RPM_BUILD_ROOT/opt/mqm/lib64/amqzaax
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqzaax_r $RPM_BUILD_ROOT/opt/mqm/lib/amqzaax_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzaax_r $RPM_BUILD_ROOT/opt/mqm/lib64/amqzaax_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amq64ax $RPM_BUILD_ROOT/opt/mqm/lib64/amq64ax
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amq64ax_r $RPM_BUILD_ROOT/opt/mqm/lib64/amq64ax_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqdlq $RPM_BUILD_ROOT/opt/mqm/bin/runmqdlq
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqlog $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqlog
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqmsg $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqmsg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqs23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqs23gl.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqs23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqs23gl_r.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqs23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqs23gl.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqs23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqs23gl_r.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqpcert.lic $RPM_BUILD_ROOT/opt/mqm/lib/amqpcert.lic
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqdcert.lic $RPM_BUILD_ROOT/opt/mqm/lib/amqdcert.lic
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/ffstsummary $RPM_BUILD_ROOT/opt/mqm/bin/ffstsummary
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqldmpa $RPM_BUILD_ROOT/opt/mqm/bin/amqldmpa
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqspdbg $RPM_BUILD_ROOT/opt/mqm/bin/amqspdbg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrfdm $RPM_BUILD_ROOT/opt/mqm/bin/amqrfdm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqrdbgm $RPM_BUILD_ROOT/opt/mqm/bin/amqrdbgm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqmfsck $RPM_BUILD_ROOT/opt/mqm/bin/amqmfsck
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqorxr $RPM_BUILD_ROOT/opt/mqm/bin/amqorxr
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqwasoa $RPM_BUILD_ROOT/opt/mqm/lib64/amqwasoa
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqwascx $RPM_BUILD_ROOT/opt/mqm/lib64/amqwascx
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjxs_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxs_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjxs_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxs_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjxds_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxds_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjxds_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxds_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqzxmr0 $RPM_BUILD_ROOT/opt/mqm/lib64/amqzxmr0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/libmqjbnd.so $RPM_BUILD_ROOT/opt/mqm/java/lib/libmqjbnd.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/libmqjbnd.so $RPM_BUILD_ROOT/opt/mqm/java/lib64/libmqjbnd.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jdbc/jdbcdb2.o $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/jdbcdb2.o
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jdbc/jdbcora.o $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/jdbcora.o
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jdbc/Makefile $RPM_BUILD_ROOT/opt/mqm/java/lib/jdbc/Makefile
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/jdbc/jdbcdb2.o $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/jdbcdb2.o
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/jdbc/jdbcora.o $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/jdbcora.o
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/jdbc/Makefile $RPM_BUILD_ROOT/opt/mqm/java/lib64/jdbc/Makefile
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.postcard.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.postcard.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/postcard $RPM_BUILD_ROOT/opt/mqm/java/bin/postcard
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqpcard $RPM_BUILD_ROOT/opt/mqm/bin/amqpcard
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runpcard $RPM_BUILD_ROOT/opt/mqm/bin/runpcard
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.defaultconfig.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.defaultconfig.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/DefaultConfiguration $RPM_BUILD_ROOT/opt/mqm/java/bin/DefaultConfiguration
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/rundefconf $RPM_BUILD_ROOT/opt/mqm/bin/rundefconf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqmgse $RPM_BUILD_ROOT/opt/mqm/bin/amqmgse
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqp.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqp.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqxacred $RPM_BUILD_ROOT/opt/mqm/bin/setmqxacred
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqcertck $RPM_BUILD_ROOT/opt/mqm/bin/mqcertck
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/cs_cz/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/cs_cz/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/de_de/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/de_de/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/de_de/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/de_de/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/de_de/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/de_de/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/en_us/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/en_us/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/en_us/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/plugin.xml $RPM_BUILD_ROOT/opt/mqm/doc/en_us/plugin.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/en_us/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/en_us/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/en_us/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/es_es/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/es_es/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/es_es/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/es_es/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/es_es/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/es_es/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/fr_fr/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/fr_fr/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/hu_hu/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/hu_hu/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/it_it/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/it_it/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/it_it/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/it_it/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/it_it/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/it_it/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ja_jp/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/ja_jp/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ko_kr/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/ko_kr/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pl_pl/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/pl_pl/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/pt_br/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/pt_br/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/ru_ru/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/ru_ru/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_cn/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/zh_cn/wizard_help.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ax99995_.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ax99995_.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/bip4.css $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/bip4.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/epub.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/epub.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/g_postcard.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/g_postcard.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/g_postcard_different.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/g_postcard_different.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/g_postcard_oneqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/g_postcard_oneqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/g_postcard_signon.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/g_postcard_signon.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/g_postcard_twoqm.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/g_postcard_twoqm.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/g_postcard_workings.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/g_postcard_workings.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_comp_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_comp_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_conf_win2000.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_conf_win2000.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_config.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_config.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_def_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_def_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_def_conf_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_def_conf_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_join_def_clus.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_join_def_clus.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_local_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_local_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_prepare_wiz.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_prepare_wiz.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_qmgr_conf.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_qmgr_conf.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_rem_repos.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_rem_repos.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_uninst.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_uninst.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/i_wsmq.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/i_wsmq.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ibmdita.css $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ibmdita.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ng9000.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ng9000.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ngaix.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ngaix.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ngandroid.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ngandroid.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/nghpux.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/nghpux.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ngios.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ngios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ngsolaris.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ngsolaris.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/ngzos.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/ngzos.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/wizard_intro.htm $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/wizard_intro.htm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/IC-lotus-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/IC-lotus-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/IC-rtl-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/IC-rtl-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/IC-tiv-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/IC-tiv-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/IC-ws-sm.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/IC-ws-sm.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L1_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L1_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Administering.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Administering.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Benefits.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Benefits.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Config-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Config-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Data.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Data.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Developing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Developing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Files.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Files.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Generic.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Generic.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_HW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_HW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Monitoring.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Monitoring.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Product-Overview.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Product-Overview.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_APIs.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_APIs.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Assembling.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Assembling.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Auditing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Auditing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Basic-skills.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Basic-skills.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Commands.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Commands.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Config.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Config.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Debugging.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Debugging.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Deploying.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Deploying.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Education.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Education.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Examples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Examples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Glossary.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Glossary.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Install.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Install.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Language-reference.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Language-reference.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_LogInOut.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_LogInOut.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Messages.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Messages.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Migrate.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Migrate.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Network.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Network.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Network_Pattern.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Network_Pattern.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Phys.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Phys.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Setup.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Setup.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Scripting-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Scripting-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Settings.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Settings.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Testing.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Testing.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Troubleshooting.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Troubleshooting.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Tuning.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Tuning.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Tutorials-samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Tutorials-samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_Upgrade.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_Upgrade.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_User-interface.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_User-interface.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_SW_User_Role.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_SW_User_Role.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Samples.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Samples.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Scenarios.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Scenarios.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Security.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Security.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/L2_Tuning-Gen.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/L2_Tuning-Gen.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/apiOperation_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/apiOperation_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/apiPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/apiPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/apiRef_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/apiRef_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/authorInfo_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/authorInfo_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/concept_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/concept_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/cshelp_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/cshelp_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/fw_bold.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/fw_bold.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/info_ws.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/info_ws.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/javaClass_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/javaClass_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/javaInterface_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/javaInterface_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/javaPackage_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/javaPackage_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/msg_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/msg_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/pdf_image.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/pdf_image.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/reference_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/reference_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/sampleDetails_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/sampleDetails_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/sampleSetup_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/sampleSetup_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/sample_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/sample_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/task_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/task_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/timestamp.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/timestamp.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/topic_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/topic_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/topictype_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/topictype_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tsTroubleshooting_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tsTroubleshooting_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tutorialAbstract_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tutorialAbstract_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tutorialIntro_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tutorialIntro_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tutorialLesson_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tutorialLesson_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tutorialModule_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tutorialModule_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tutorialSummary_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tutorialSummary_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/tutorial_obj.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/tutorial_obj.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/info/ws_16x16.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/info/ws_16x16.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/plugin.properties $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/plugin.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/sout.gif $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/sout.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/doc/zh_tw/wizard_help.xml $RPM_BUILD_ROOT/opt/mqm/doc/zh_tw/wizard_help.xml

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc"
%dir %attr(550,root,mqm) "/opt/mqm/bin/security"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/jdbc"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib64/jdbc"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/cs_cz"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/cs_cz/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/de_de"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/de_de/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/en_us"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/en_us/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/es_es"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/es_es/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/fr_fr"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/fr_fr/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/hu_hu"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/hu_hu/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/it_it"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/it_it/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/ja_jp"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/ja_jp/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/ko_kr"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/ko_kr/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/pl_pl"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/pl_pl/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/pt_br"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/pt_br/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/ru_ru"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/ru_ru/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/zh_cn"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/zh_cn/info"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/zh_tw"
%dir %attr(555,mqm,mqm) "/opt/mqm/doc/zh_tw/info"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqbrk"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqfcxba"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dltmqbrk"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqbrk"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqfqpub"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqcrsta"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqpcsea"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzif_r"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzfu"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzfud"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmz1_r.so"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzfuma"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqoamd"
%attr(4550,root,mqm) %verify(not md5 mtime) "/opt/mqm/bin/security/amqoamax"
%attr(4550,root,mqm) %verify(not md5 mtime) "/opt/mqm/bin/security/amqoampx"
%attr(555,mqm,mqm) "/opt/mqm/bin/security/amqpamcf"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzsc"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzscg"
%attr(555,mqm,mqm) "/opt/mqm/lib/libmqmcics_r.a"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzlaa0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzlsa0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzxma0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmgr0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmuc0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmuf0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzmur0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dltmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqaut"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqcsv"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqfls"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqaut"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqtrn"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqrte"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqaut"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqcsv"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rcdmqimg"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rcrmqobj"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqchi"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqlsr"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runswchl"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrcmla"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrrmfa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrmppa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqzlwa0"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqlsr"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqchl"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqtrm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rsvmqtrn"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/addmqinf"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqinf"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/rmvmqinf"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqsstop"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqm"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqprd"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqspl"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqspl"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/strmqm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/strmqcsv"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqml_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqml_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmalda_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmaldb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmzf.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmzf.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmzf_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmzf_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqutl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqutl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqutl_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqutl_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzi.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzi.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzi_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzi_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqds.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqds.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqds_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqds_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmr.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmr.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmr_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmr_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcb.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcb.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcb_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcbrt.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmxa.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa64.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmxa_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmxa64_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmax.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmax_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax64.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmax64_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzaax"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzaax"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqzaax_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzaax_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amq64ax"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amq64ax_r"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqdlq"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqlog"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqmsg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqs23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqs23gl_r.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqs23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqs23gl_r.so.4.1"
%attr(444,mqm,mqm) "/opt/mqm/lib/amqpcert.lic"
%attr(444,mqm,mqm) "/opt/mqm/lib/amqdcert.lic"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/ffstsummary"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqldmpa"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqspdbg"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrfdm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqrdbgm"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqmfsck"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqorxr"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqwasoa"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqwascx"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjxs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjxs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjxds_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjxds_r.so"
%attr(554,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqzxmr0"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/libmqjbnd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/libmqjbnd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/jdbc/jdbcdb2.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/jdbc/jdbcora.o"
%attr(555,mqm,mqm) "/opt/mqm/java/lib/jdbc/Makefile"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/jdbc/jdbcdb2.o"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/jdbc/jdbcora.o"
%attr(555,mqm,mqm) "/opt/mqm/java/lib64/jdbc/Makefile"
%attr(555,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.postcard.jar"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/postcard"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqpcard"
%attr(555,mqm,mqm) "/opt/mqm/bin/runpcard"
%attr(555,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.defaultconfig.jar"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/DefaultConfiguration"
%attr(555,mqm,mqm) "/opt/mqm/bin/rundefconf"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqmgse"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqp.sh"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqxacred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/mqcertck"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/cs_cz/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/de_de/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/plugin.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/en_us/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/es_es/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/fr_fr/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/hu_hu/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/it_it/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ja_jp/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ko_kr/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pl_pl/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/pt_br/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/ru_ru/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_cn/wizard_help.xml"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ax99995_.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/bip4.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/epub.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/g_postcard.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/g_postcard_different.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/g_postcard_oneqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/g_postcard_signon.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/g_postcard_twoqm.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/g_postcard_workings.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_comp_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_conf_win2000.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_config.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_def_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_def_conf_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_join_def_clus.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_local_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_prepare_wiz.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_qmgr_conf.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_rem_repos.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_uninst.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/i_wsmq.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ibmdita.css"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ng9000.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ngaix.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ngandroid.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/nghpux.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ngios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ngsolaris.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/ngzos.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/wizard_intro.htm"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/IC-lotus-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/IC-rtl-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/IC-tiv-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/IC-ws-sm.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L1_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Administering.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Benefits.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Config-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Data.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Developing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Files.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Generic.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_HW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Monitoring.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Product-Overview.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_APIs.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Assembling.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Auditing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Basic-skills.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Commands.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Config.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Debugging.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Deploying.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Education.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Examples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Glossary.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Install.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Language-reference.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_LogInOut.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Messages.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Migrate.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Network.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Network_Pattern.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Phys.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Plan-Setup.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Scripting-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Settings.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Testing.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Troubleshooting.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Tuning.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Tutorials-samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_Upgrade.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_User-interface.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_SW_User_Role.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Samples.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Scenarios.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Security.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/L2_Tuning-Gen.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/apiOperation_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/apiPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/apiRef_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/authorInfo_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/concept_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/cshelp_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/fw_bold.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/info_ws.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/javaClass_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/javaInterface_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/javaPackage_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/msg_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/pdf_image.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/reference_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/sampleDetails_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/sampleSetup_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/sample_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/task_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/timestamp.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/topic_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/topictype_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tsTroubleshooting_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tutorialAbstract_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tutorialIntro_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tutorialLesson_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tutorialModule_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tutorialSummary_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/tutorial_obj.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/info/ws_16x16.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/plugin.properties"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/sout.gif"
%attr(444,mqm,mqm) "/opt/mqm/doc/zh_tw/wizard_help.xml"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/preinstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2016" 
#   crc="3530070126" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2016 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# 
# Common Preinstallation script for all packages
# 
# Check that this package is not being installed to a location where 
# a different VR exists
# 
#######################################################################################################
# Check the install path does not exceed the MQ maximum length of 256
#######################################################################################################
if [ ${#MQ_INSTALLATION_PATH} -gt 256 ]; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) exceeds MQ maximum length of 256"
  echo ""
  exit 1
fi

#######################################################################################################
# Check the install path does not contain unsupported charaters
#######################################################################################################
echo "${MQ_INSTALLATION_PATH}" | grep "[:%# ]" > /dev/null
if [ $? -eq 0 ] ; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character"
  echo ""
  exit 1
fi
# Trailing blanks 
echo "${MQ_INSTALLATION_PATH}" | grep "\ $" > /dev/null
if [ $? -eq 0 ] ; then
  echo ""
  echo "ERROR:   Specified installation path (${MQ_INSTALLATION_PATH}) contains an unsupported character"
  echo ""
  exit 1
fi


#######################################################################################################
# Runtime checks
#######################################################################################################
echo ${RPM_PACKAGE_NAME} | grep  "MQSeriesRuntime" > /dev/null
if [ $? -eq 0 ] ; then
  #####################################################################################################
  # Check that the install path is empty 
  # ignore lost+found and .snapshots(GPFS) directories
  # The .snapshots directory can also be renamed within GPFS, so we allow an alternate name to be specified with
  # AMQ_IGNORE_SNAPDIRNAME
  #####################################################################################################
  if [ x${AMQ_OVERRIDE_EMPTY_INSTALL_PATH} = x ] ;then 
    if [ -d ${MQ_INSTALLATION_PATH} ] && [ ${MQ_INSTALLATION_PATH} != ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then
      if [ "${AMQ_IGNORE_SNAPDIRNAME}" = "" ] ; then
        SNAPDIR_NAME=".snapshots"
      else
        SNAPDIR_NAME="${AMQ_IGNORE_SNAPDIRNAME}"
      fi
      LS_ALL=`ls -A ${MQ_INSTALLATION_PATH} 2>/dev/null | grep -F -v "lost+found" | grep -F -v "${SNAPDIR_NAME}"`
      if [ "${LS_ALL}" ] ; then
        echo ""
        echo "ERROR:   Specified installation path '${MQ_INSTALLATION_PATH}' is not empty"
        echo ""
        exit 1
     fi
    fi
  fi
#######################################################################################################
# Non Runtime checks
#######################################################################################################
else
  #####################################################################################################
  # Check the version/release of the product already at MQ_INSTALLATION_PATH is the same as this one
  #####################################################################################################
  if [ -x ${MQ_INSTALLATION_PATH}/bin/dspmqver ] ; then
    INSTALLED_VR=$(${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2}')
    PACKAGE_VR=`echo ${RPM_PACKAGE_VERSION} | awk -F. '{print $1 "." $2}'`
    if [ ${INSTALLED_VR} != ${PACKAGE_VR} ] ; then
      echo ""
      echo "ERROR:   This package is not applicable to the MQ installation at ${MQ_INSTALLATION_PATH}"
      echo ""
      exit 1
    fi
  else
    echo ""
    echo "ERROR:   There is no MQSeriesRuntime installed at ${MQ_INSTALLATION_PATH}"
    echo ""
    exit 1
  fi
fi

#######################################################################################################
# Preventing an installation over an existing installation
# Each component has a unique '.cmptag' file.  If this is already present on the filesystem at the
# installation location, then the component must already be installed to this location, so we should
# abort.
#######################################################################################################
case "${RPM_PACKAGE_NAME}" in
  MQSeriesAMS)
      compfile="IBM_WebSphere_MQ_Advanced_Message_Security_Component."
      ;;
  MQSeriesASOAP)
      compfile="DOES_NOT_CONTAIN_A_COMPONENT_FILE"
      ;;
  MQSeriesAMQP)
      compfile="DOES_NOT_CONTAIN_A_COMPONENT_FILE"
      ;;
  MQSeriesClient)
      compfile="IBM_WebSphere_MQ_Client."
      ;;
  MQSeriesExplorer)
      compfile="IBM_WebSphere_MQ_Explorer."
      ;;
  MQSeriesFTAgent)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Agent."
      ;;
  MQSeriesFTBase)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Base."
      ;;
  MQSeriesFTLogger)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Logger."
      ;;
  MQSeriesFTService)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Service."
      ;;
  MQSeriesFTTools)
      compfile="IBM_WebSphere_MQ_Managed_File_Transfer_Tools."
      ;;
  MQSeriesGSKit)
      compfile='IBM_WebSphere_MQ_GSKit.'
      ;;
  MQSeriesJava)
      compfile="IBM_WebSphere_MQ_Java_Messaging."
      ;;
  MQSeriesJRE)
      compfile="IBM_WebSphere_MQ_JRE"
      ;;
  MQSeriesMan)
      compfile="IBM_WebSphere_MQ_Man_Pages."
      ;;
  MQSeriesMsg_cs)
      compfile="IBM_WebSphere_MQ_Messages_Czech."
      ;;
  MQSeriesMsg_de)
      compfile="IBM_WebSphere_MQ_Messages_German."
      ;;
  MQSeriesMsg_es)
      compfile="IBM_WebSphere_MQ_Messages_Spanish."
      ;;
  MQSeriesMsg_fr)
      compfile="IBM_WebSphere_MQ_Messages_French."
      ;;
  MQSeriesMsg_hu)
      compfile="IBM_WebSphere_MQ_Messages_Hungarian."
      ;;
  MQSeriesMsg_it)
      compfile="IBM_WebSphere_MQ_Messages_Italian."
      ;;
  MQSeriesMsg_ja)
      compfile="IBM_WebSphere_MQ_Messages_Japanese."
      ;;
  MQSeriesMsg_ko)
      compfile="IBM_WebSphere_MQ_Messages_Korean."
      ;;
  MQSeriesMsg_pl)
      compfile="IBM_WebSphere_MQ_Messages_Polish."
      ;;
  MQSeriesMsg_pt)
      compfile="IBM_WebSphere_MQ_Messages_Brazilian_Portuguese."
      ;;
  MQSeriesMsg_ru)
      compfile="IBM_WebSphere_MQ_Messages_Russian."
      ;;
  MQSeriesMsg_Zh_CN)
      compfile="IBM_WebSphere_MQ_Messages_Chinese_Simplified."
      ;;
  MQSeriesMsg_Zh_TW)
      compfile="IBM_WebSphere_MQ_Messages_Chinese_Traditional."
      ;;
  MQSeriesRuntime)
      compfile="IBM_WebSphere_MQ_Runtime."
      ;;
  MQSeriesSamples)
      compfile="IBM_WebSphere_MQ_Samples."
      ;;
  MQSeriesSDK)
      compfile="IBM_WebSphere_MQ_SDK."
      ;;
  MQSeriesServer)
      compfile="IBM_WebSphere_MQ_Server."
      ;;
  MQSeriesXRService)
      compfile="IBM_WebSphere_MQ_Telemetry_Service."
      ;;
  *)
      echo "ERROR: Package name ${RPM_PACKAGE_NAME} not recognised, aborting installation."
      exit 1
      ;;
esac

# RPM_PACKAGE_VERSION is of the form 8.0.0
# If the 'compfile' file is present, then the package is already installed on
# the system, and we abort the installation of this package.
# NOTE the careful positioning of the wildcard outside the doublequotes.
if [ -f "${MQ_INSTALLATION_PATH}/properties/version/${compfile}"* ]; then
  echo "ERROR:  The specified installation path (${MQ_INSTALLATION_PATH}) already"
  echo "        has this package (${RPM_PACKAGE_NAME}) installed."
  echo "        Aborting installation."
  exit 1
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="1114153681" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# Preinstallation script
# Check's to see if the license agreement has been accepted

if [ ! -r /tmp/mq_license_${RPM_PACKAGE_VERSION}/license/status.dat ] && [ ! -r "${MQ_INSTALLATION_PATH}/licenses/status.dat" ] ; then

    cat << +++EOM+++
ERROR:  Product cannot be installed until the license
        agreement has been accepted.
        Run the 'mqlicense' script, which is in the root
        directory of the install media, or see the
        installation instructions in the product 
        Infocenter for more information
+++EOM+++

   exit 1
fi

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/server_preinstall.sh

INSTALLROOT=${MQ_INSTALLATION_PATH}

#  Server preinstall script
#  ------------------------------
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="767503690" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 

# If the file "${MQ_INSTALLATION_PATH}/lib/amqpcert.lic" exists and is a link, it should be
# deleted as is it not desirable to have two license files.  Note that the
# license file installed by the server component might be of the same name
# (in which case the symlink would just be overwritten), however it might have
# an alternate name which would be the trial or beta license.
if [ -h "${MQ_INSTALLATION_PATH}/lib/amqpcert.lic" ]; then
  rm -f "${MQ_INSTALLATION_PATH}/lib/amqpcert.lic"
fi
echo > /dev/null 2>/dev/null

%post
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi
if [ ${MQ_INSTALLATION_PATH} !=  ${MQ_DEFAULT_INSTALLATION_PATH} ] ; then 
  if [ -x ${MQ_INSTALLATION_PATH}/bin/amqicrel ] ; then 
     ${MQ_RUNSCRIPT} ${MQ_INSTALLATION_PATH}/bin/amqicrel ${MQ_INSTALLATION_PATH} ${RPM_PACKAGE_NAME}-${RPM_PACKAGE_VERSION}-${RPM_PACKAGE_RELEASE}
  fi
fi
# Linking ${MQ_INSTALLATION_PATH}/bin/runmqbrk to ${MQ_INSTALLATION_PATH}/bin/strmqbrk
if [ ! -d ${MQ_INSTALLATION_PATH}/bin ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/bin
else
    rm -f ${MQ_INSTALLATION_PATH}/bin/strmqbrk
fi
ln -s ${MQ_INSTALLATION_PATH}/bin/runmqbrk ${MQ_INSTALLATION_PATH}/bin/strmqbrk
chown -fh mqm ${MQ_INSTALLATION_PATH}/bin/strmqbrk
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/bin/strmqbrk
# Linking ${MQ_INSTALLATION_PATH}/lib64/amqzfu to ${MQ_INSTALLATION_PATH}/lib/amqzfu
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfu
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/amqzfu ${MQ_INSTALLATION_PATH}/lib/amqzfu
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfu
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfu
# Linking ${MQ_INSTALLATION_PATH}/lib64/amqzfud to ${MQ_INSTALLATION_PATH}/lib/amqzfud
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfud
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/amqzfud ${MQ_INSTALLATION_PATH}/lib/amqzfud
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfud
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/amqzfud
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmzf.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmzf.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmzf.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmzf.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmzf_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmzf_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmzf_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmzf_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqutl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqutl.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqutl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqutl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqutl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqutl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqutl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqutl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmcb.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmcb.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmcb.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmcb.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmcb_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmcb_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmcb_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmcb_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmxa.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmxa.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmxa_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmxa_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmxa64_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmax.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmax.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqmax_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqmax_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax64.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax64.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqmax64_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqmax64_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/server_postinstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2012,2015" 
#   crc="3622503993" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2012, 2015 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 


INSTALLROOT=${MQ_INSTALLATION_PATH}


# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null

# Create a default PAM configuration
if [ -x ${MQ_INSTALLATION_PATH}/bin/security/amqpamcf ] ; then
  ${MQ_INSTALLATION_PATH}/bin/security/amqpamcf 2>&1
fi
   
#  Run the mqconfig tool to analyse the system against  the kernel requirements etc.

if [ -x  ${MQ_INSTALLATION_PATH}/bin/mqconfig ]  ; then
  MQCONFIG_LOGFILE=/tmp/mqconfig.$$.log 
  INSTALL_VR=`${MQ_INSTALLATION_PATH}/bin/dspmqver -f2 -b | awk -F. '{print $1 "." $2}'`
  ${MQ_INSTALLATION_PATH}/bin/mqconfig -v ${INSTALL_VR} > ${MQCONFIG_LOGFILE} 2>&1    
  if [ $?  -ne 0 ] ; then 
    echo "" >&2
    echo "WARNING: System settings for this system do not meet recommendations for this product " >&2
    echo "         See the log file at \"${MQCONFIG_LOGFILE}\" for more information" >&2
    echo "" >&2
  else 
     rm  ${MQCONFIG_LOGFILE}
  fi
fi


%preun
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2016" 
#   crc="122768040" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2016 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre-uninstallation script
# Checks for already running Q Managers, and if it finds one, stops the
# uninstall.

# If amqiclen exists (should do during uninstall) then run it to clean up
# IPCC resources. If amqiclen returns an error then a queue manager is still
# running so stop the uninstall.
if [ -x ${MQ_INSTALLATION_PATH}/bin/amqiclen ] && [ -f /var/mqm/mqs.ini ]
then
    ${MQ_INSTALLATION_PATH}/bin/amqiclen -v -x > /tmp/amqiclen.$$.out 2>&1
    amqiclen_rc=$?
    if [ $amqiclen_rc -ne 0 ] 
    then
        echo " " >&2
        echo "ERROR: MQ shared resources associated with the installation at" >&2
        echo "      '${MQ_INSTALLATION_PATH}' are still in use." >&2
        echo "       You must stop all MQ processing, including applications, Queue Managers" >&2 
        echo "       and Listeners before attempting to install, update or delete" >&2
        echo "       the MQ product." >&2
        echo " " >&2
        echo "       'amqiclen -v -x' return code was: '$amqiclen_rc', output was:" >&2
        cat /tmp/amqiclen.$$.out >&2
        echo " " >&2
        rm -f /tmp/amqiclen.$$.out
        exit 1
    fi
    rm -f /tmp/amqiclen.$$.out
fi 
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="1595222582" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre-uninstallation check script for all components
# A check is performed to see if there are any fixpack filesets applied to
# the base component which is currently being uninstalled.  If the fixpack
# has been applied, the uninstallation of this component is aborted to prevent
# the situation where the base fileset has been uninstalled leaving an
# uninstallable fixpack.

FIXPACK_BACKUPDIR="${MQ_INSTALLATION_PATH}/maintenance"

unset fix_exists

fix_exists=$(find $FIXPACK_BACKUPDIR -type d -maxdepth 2 -print 2>/dev/null | \
while read directory ; do
  component=`basename $directory`
  if [ "$RPM_PACKAGE_NAME" = "$component" ]; then
    # safety check - are there actually files under this directory?
    num_files=`find "$directory" -type f -print 2>/dev/null | wc -l`
    if [ $num_files -gt 0 ]; then
      echo  $num_files
      exit
    fi
  fi
done
)
if [ ! -z $fix_exists ] ; then 
  echo "ERROR:  There appears to be a fixpack installed on this machine for this" >&2
  echo "        component." >&2
  echo "" >&2
  echo "        Please ensure you have removed all fixpacks for the ${RPM_PACKAGE_NAME}" >&2
  echo "        component before trying to remove this package." >&2
  echo "" >&2
  exit 1 
fi
# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/server_preuninstall.sh
#
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="2836959397" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre uninstallation script for Server
#####################################################################################
#
# reset trial license file back to the 'as installed' state    
# 
#####################################################################################
if [ -f ${MQ_INSTALLATION_PATH}/lib/amqpcert.lic ] && [ -f ${MQ_INSTALLATION_PATH}/lib/amqtcert.lic.bak ]
   then 
    rm -f ${MQ_INSTALLATION_PATH}/lib/amqpcert.lic
    mv ${MQ_INSTALLATION_PATH}/lib/amqtcert.lic.bak ${MQ_INSTALLATION_PATH}/lib/amqtcert.lic
fi

echo "Resetting return code to success" > /dev/null

# Removing product links
rm -f ${MQ_INSTALLATION_PATH}/bin/strmqbrk
rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfu
rm -f ${MQ_INSTALLATION_PATH}/lib/amqzfud
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmzf_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmzf_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqutl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqutl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmcb_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmcb_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmxa_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmxa64_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqmax_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqmax64_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqs23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqs23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqs23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqs23gl_r.so

%postun
RPM_PACKAGE_SUMMARY="IBM MQ Server FileSet"
RPM_PACKAGE_NAME="MQSeriesServer"
RPM_PACKAGE_VERSION="9.0.0"
RPM_PACKAGE_RELEASE="0"
PACKAGEPLATFORMS="x86_64"
MQ_DEFAULT_INSTALLATION_PATH=/opt/mqm
if [ -z "${RPM_INSTALL_PREFIX}" ] ; then 
  MQ_INSTALLATION_PATH=${MQ_DEFAULT_INSTALLATION_PATH}
else
  MQ_INSTALLATION_PATH=`echo "${RPM_INSTALL_PREFIX}" | sed s#//#/#g`
fi
MQ_RUNSCRIPT=
echo ${SHELLOPTS} | grep xtrace > /dev/null
if [ $? -eq 0 ] ; then 
  env | sort
  uname -a
  id
  MQ_RUNSCRIPT="sh -x"
fi

#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="2675138520" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# Pre-uninstallation script
if [ -f ${MQ_INSTALLATION_PATH}/lib/amqpcert.lic ]
then
    rm -f ${MQ_INSTALLATION_PATH}/lib/amqpcert.lic
fi
if [ -f /var/mqm/qmgrs/@SYSTEM/nodelock ]
then
    rm -f /var/mqm/qmgrs/@SYSTEM/nodelock
fi
if [ -f /var/mqm/qmgrs/@SYSTEM/amqtrial.inf ]
then
    rm -f /var/mqm/qmgrs/@SYSTEM/amqtrial.inf
fi


