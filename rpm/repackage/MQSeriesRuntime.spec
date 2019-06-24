Summary: IBM MQ Runtime FileSet
Name: MQSeriesRuntime
Version: 9.0.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Conflicts: 	                  MQSeriesHtml_base = 5.2.0-0
Conflicts:  	                  MQSeriesDMQRuntime = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_en = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_de = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_es = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_fr = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_it = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_ja = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_ko = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_pt = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_Zh_CN = 5.2.0-0
Conflicts:  	                  MQSeriesDMQDoc_Zh_TW = 5.2.0-0
Conflicts:  	                  MQSeriesClient < 7.0.0-0
Conflicts:  	                  MQSeriesJava <  7.0.0-0
Conflicts:  	                  MQSeriesKeyMan  < 7.0.0-0
Conflicts: 	                  MQSeriesGSKit  < 7.0.0-0
Conflicts:  	                  MQSeriesMan < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_de < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_es < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_fr < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_it < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_ja < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_ko < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_pt < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_Zh_CN < 7.0.0-0
Conflicts:  	                  MQSeriesMsg_Zh_TW < 7.0.0-0
Conflicts:  	                  MQSeriesSamples < 7.0.0-0
Conflicts:  	                  MQSeriesSDK < 7.0.0-0
Conflicts:  	                  MQSeriesServer < 7.0.0-0
Conflicts:  	                  MQSeriesRuntime < 7.0.0-0
Conflicts:  			  MQSeriesXRService < 7.0.0-0
Provides: /bin/sh
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
This package provides the common files to both IBM MQ client and server
installations, and is a prerequisite package of all other IBM MQ
packages.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/lib
install -d $RPM_BUILD_ROOT/opt/mqm/lib/compat
install -d $RPM_BUILD_ROOT/opt/mqm/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/lib64/compat
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib
install -d $RPM_BUILD_ROOT/opt/mqm/samp
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/lib/iconv
install -d $RPM_BUILD_ROOT/opt/mqm/msg
install -d $RPM_BUILD_ROOT/opt/mqm/msg/en_US
install -d $RPM_BUILD_ROOT/opt/mqm/READMES
install -d $RPM_BUILD_ROOT/opt/mqm/licenses
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/samp/mqccred
install -d $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib
install -d $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqm.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqm.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqm.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqm.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcs.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcs.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcs.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcs.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqe.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqe.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqe.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqe.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqecs.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqecs.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqecs.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqecs.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqxzu.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqxzu.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqxzu.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqxzu.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzsd.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzsd.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzsd.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzsd.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqz.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqz.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqz.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqz.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqm_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqm_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqm_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqm_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmcs_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmcs_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmcs_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmcs_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqe_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqe_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqe_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqe_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqecs_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqecs_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqecs_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqecs_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqxzu_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqxzu_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqxzu_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqxzu_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqzsd_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqzsd_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqzsd_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqzsd_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqz_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqz_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqz_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqz_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjx_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjx_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjx_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjx_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqjxx_r.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqjxx_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqjxx_r.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqjxx_r.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqltmc0 $RPM_BUILD_ROOT/opt/mqm/bin/amqltmc0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqb23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqb23gl.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libimqb23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib/libimqb23gl_r.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqb23gl.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqb23gl.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libimqb23gl_r.so.4.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libimqb23gl_r.so.4.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/ccsid.tbl $RPM_BUILD_ROOT/opt/mqm/samp/ccsid.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/ccsid_part2.tbl $RPM_BUILD_ROOT/opt/mqm/samp/ccsid_part2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/ccsid.new $RPM_BUILD_ROOT/opt/mqm/samp/ccsid.new
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqs.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqs.ini
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqclient.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqclient.ini
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/service.env $RPM_BUILD_ROOT/opt/mqm/samp/service.env
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/strmqtrc $RPM_BUILD_ROOT/opt/mqm/bin/strmqtrc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/endmqtrc $RPM_BUILD_ROOT/opt/mqm/bin/endmqtrc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqras $RPM_BUILD_ROOT/opt/mqm/bin/dspmqras
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqtrc $RPM_BUILD_ROOT/opt/mqm/bin/dspmqtrc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqtrc.fmt $RPM_BUILD_ROOT/opt/mqm/lib/amqtrc.fmt
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqxdbg $RPM_BUILD_ROOT/opt/mqm/bin/amqxdbg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqxmsg0 $RPM_BUILD_ROOT/opt/mqm/bin/amqxmsg0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicdir $RPM_BUILD_ROOT/opt/mqm/bin/amqicdir
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libmqmzse.so $RPM_BUILD_ROOT/opt/mqm/lib/libmqmzse.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libmqmzse.so $RPM_BUILD_ROOT/opt/mqm/lib64/libmqmzse.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/msg/en_US/amq.cat $RPM_BUILD_ROOT/opt/mqm/msg/en_US/amq.cat
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002501B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002501B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250388.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250388.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250413.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250413.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025045A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011101B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011101B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011104E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011104E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011104FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011104FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011501B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011501B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011504E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011504FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011601B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011601B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011604E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011604E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011604FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011604FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011801B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011801B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011804E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011804E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011804FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011804FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D0381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D0381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01220381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01220411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012901B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012901B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01290333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01290352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01290381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01290381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012904E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012904E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012904FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012904FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C012D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C03AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C03AD.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D012C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D03AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D03AD.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A40360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A40416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A40441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A40441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A404E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A404E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A80358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A8035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A8035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A80394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A804E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A804E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B501F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B501F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F401B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F404E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F404E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F404FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D0365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D04E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D04E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D0500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033301B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033301B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033301F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033301F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0341037B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0341037B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03410410.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410410.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03410440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410440.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0342039E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0342039E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034203B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034203B7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0343039F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0343039F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034303B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034303B3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03440387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03440387.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03440412.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03440412.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0344045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0344045A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0344045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0344045B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034503A0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034503A0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03450564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03450564.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03450569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03450569.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0346036A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0346036A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/034634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/034634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035201B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035201B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035201F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035201F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035204E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035204FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035404E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035404E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035704E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035704E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035801A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035801A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0358035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0358035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03580394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03580394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035804E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035804E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590402.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035904E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035904E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E01A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E01A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E0358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E0394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E04E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E04E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036001A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036001A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03600416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03600441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036004E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036004E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036101B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036101B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036101F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036101F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036104E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036104E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036204E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036204E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03640396.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03640396.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036403EE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036403EE.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0365032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0365032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0365036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0365036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036504E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036504E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03650500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03650500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03660354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03660390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036604E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036604E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03660502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03660502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036701B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036701B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03670333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03670333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03670352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03670352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036704E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036704E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036704FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036704FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036A0346.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036A0346.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036A34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B0365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B0365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B04E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B04E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B0500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B0500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037004E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037004E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03700503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03700503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037B0341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B0341.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037B0440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B0440.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037B34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0381011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0381011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0381011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0381011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038101B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038101B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038101F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038101F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03810411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03810411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038104E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038104E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03870344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03870344.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03870412.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03870412.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0387045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0387045B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03880025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03880025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0388045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0388045A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039004E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039004E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0393046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0393046B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039304E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039401A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039401A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03940358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0394035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0394035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039404E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039404E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03960364.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03960364.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039603EE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039603EE.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980402.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039804E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039804E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03990458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03990458.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039904E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039904E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A0462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A0462.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A04E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A04E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039E0342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039E0342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039E03B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039E03B7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039F0343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F0343.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039F03B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F03B3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039F34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039F34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A00345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A00345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A00564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A00564.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A213BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A213BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A413BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A413BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A503CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A503CA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A70567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A70567.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A903C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A903C4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AA34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AB13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AB13BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AB34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AB34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD012C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD012D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE13BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF13BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B30343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B30343.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B3039F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B3039F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B403C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B403C4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B503CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B503CA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B603C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B603C4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B70342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B70342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B7039E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B7039E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C403A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C403B4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403B4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C403B6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C403B6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03C434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03C434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA03A5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA03A5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA03B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA03B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03EE0364.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE0364.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03EE0396.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE0396.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03EE34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03EE34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0401046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0401046B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040104E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040104E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04010503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04010503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04020359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04020398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040204E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040204E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04020501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04020501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04030381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04030411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04100341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04100341.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04100440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04100440.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04110403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04110403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04120344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04120344.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04120387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04120387.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04130025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04130025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0413045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0413045A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041601A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041601A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04160360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04160360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04160441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04160441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041604E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041604E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041701B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041701B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04400341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400341.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0440037B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0440037B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04400410.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400410.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044101A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044101A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04410360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04410416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044104E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044104E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0449044A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0449044A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044A0449.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044A0449.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044A34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04580399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04580399.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045804E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045804E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0344.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0388.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0388.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A0413.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A0413.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A045B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045A34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B0344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B0344.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B0387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B0387.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B045A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045B34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045B34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0462039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0462039A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046204E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046204E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04630464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04630464.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046304E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04640463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04640463.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04640465.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04640465.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046404E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046404E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04650464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04650464.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B0393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B0393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B0401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B0401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B04E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B04E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30463.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30464.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E3046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E3046B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E401B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E401F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E401F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E404FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E5032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E5032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E50365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E5036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E5036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E50500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60402.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E701A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E701A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E7035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E7035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E801A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E801A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E80360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E80416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E80441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E80441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E834B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E834B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90399.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E9039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E9039A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90458.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90462.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0500032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0500032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05000365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05000365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0500036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0500036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050004E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050004E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010402.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050104E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050104E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050204E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050204E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050234B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050234B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050304E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050334B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050334B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05640345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05640345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056403A0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056403A0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05640569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05640569.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05641345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05641345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05650567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05650567.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056534B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056534B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056703A7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056703A7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05670565.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05670565.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0567056A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0567056A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0567056C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0567056C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05690345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05690345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05690564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05690564.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05691345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05691345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056A0567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A0567.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056C0567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C0567.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13450564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13450564.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13450569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13450569.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03A2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03A2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03AB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03AE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AE.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA03AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA03AF.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0012C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0012D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B001F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B001F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00341.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00343.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00344.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00344.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00346.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00346.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00364.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00364.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0036A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0037B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0037B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00387.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00387.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00388.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00388.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00396.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00396.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00399.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0039A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0039F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0039F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AD.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003C4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003C4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003CA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003EE.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003EE.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00402.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00410.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00410.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00412.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00412.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00413.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00413.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00440.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00449.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00449.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0044A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0044A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00458.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0045A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0045A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0045B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0045B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00462.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00463.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00464.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00564.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00564.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00565.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00565.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00567.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00567.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0056A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0056A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0056C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0056C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B013BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B013BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/readme.ccs $RPM_BUILD_ROOT/opt/mqm/lib/iconv/readme.ccs
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035214E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035214E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E404E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E404E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011514E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D14E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B514E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E7035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E7035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01150476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01150476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011614E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011614E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E401B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01180478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01180478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046414E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046414E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036014E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036014E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A814E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033314E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033314E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039814E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039814E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011314E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011314E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20505.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20505.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/045814E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/045814E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046214E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046214E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40113.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40113.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036614E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036614E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E50365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E50365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA0469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA0469.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046914EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046914EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E14E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E14E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035714E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035714E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30463.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30463.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046314E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036514E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036514E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E3046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E3046B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B14E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B14E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035C0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035C0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035F14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035F14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050014E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050014E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036214E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036214E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035814E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035914E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035914E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047904FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047904FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B14E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E80360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E204E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E204E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039914E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039914E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA14EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA14EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0118047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0118047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01160477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01160477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E714E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E714E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E814E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E814E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040114E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040114E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA046A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050414E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050414E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050314E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011114E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011114E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30464.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30464.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041614E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041614E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E80416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90462.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E514E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E514E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E801A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E801A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039014E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039014E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474035C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474035C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047404E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047404E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A14EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A14EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047404FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011C039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011C039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E214E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E214E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047801F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047801F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047414E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047414E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B5047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B5047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30465.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30465.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047504FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047504FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90458.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036114E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036114E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047514E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E701A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E701A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047604E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047604E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036714E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036714E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047604FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047604FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050514E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050514E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047601F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047601F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039314E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047614E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047614E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047704E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047704E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046514E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046514E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047704FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047704FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047901F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047901F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047714E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047714E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047804E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047804E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047814E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047814E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047501F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047501F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047901B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047901B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0474041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0474041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047914E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047914E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA04EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA04EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E50500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E50500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E414E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E414E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4011C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4011C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4035F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4035F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E504E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E504E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E404FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E404FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0116047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0116047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E4047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E4047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A14E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A14E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047601B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047601B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20504.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20504.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E70394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E70358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E704E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E704E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E804E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E804E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E304E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047401F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047401F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047804FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047804FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039414E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039414E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047701F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047701F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F40477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F40477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0115039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0115039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0115.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0115.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012914E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012914E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03610477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03610477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01110475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01110475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0476039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0476039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D04E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D04E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047401B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047401B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E9039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E9039A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011D14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011D14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/011814E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/011814E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E4011D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E4011D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E60402.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E60402.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035D14E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035D14E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B035D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B035D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04750417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04750417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90399.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050114E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050114E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/040214E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/040214E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E40479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E40479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047904E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047904E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770116.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770116.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A04FB.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A04FB.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0477047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0477047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04FB047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04FB047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035414E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035414E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E80441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E80441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0417047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0417047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04770352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04770352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E314E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E314E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0479047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0479047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0361039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0361039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03520477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03520477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B01B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B01B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044114E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044114E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047504E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047504E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0475039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0475039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047701B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047701B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0025047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0025047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0478039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0478039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04760417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04760417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B50475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B50475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047501B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047501B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04790417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04790417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A0025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A0025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0111039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0111039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0111.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0111.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0118.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0118.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0129039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0129039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0129.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0129.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/037014E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/037014E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E30357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E30357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002514E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002514E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E604E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E604E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E904E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E904E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050214E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050214E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C0477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C0477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E40367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E40367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E614E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E614E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B0417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B0417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A414E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A414E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E914E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E914E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04780417.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04780417.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04170478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04170478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/00250474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/00250474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0361.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0361.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04740352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04740352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B0479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B0479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047801B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047801B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0367047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0367047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D0367.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D0367.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E644B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E644B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E344B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E244B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E244B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E944B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047A44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047B44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047C44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047C44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047D44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047D44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047444B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E844B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047544B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E744B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E744B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047644B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047644B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047744B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047744B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047844B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047944B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E444B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0047D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0047D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00474.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00474.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00475.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00475.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00476.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00476.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00477.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00477.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00478.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00478.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00479.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00479.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14EA44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14EA44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039C44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039C44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0039C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0039C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B014E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B014E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E544B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B01323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B01323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13AF34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13AF34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/054703AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/054703AD.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD0547.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B031A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B031A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00363.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B02358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00553.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C0547.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0547012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547012C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00554.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00554.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23580363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23580363.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E731A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E731A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235814E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23581323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23581323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A814E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A814E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A81323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A81323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235831A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235831A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235844B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A80363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A80363.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E72358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E72358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E71323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E71323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E70363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E70363.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A82358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A82358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055303CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055303CA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B004EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B004EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/31A844B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/31A844B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00469.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0046D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0046C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B0046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B0046A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055444B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13230363.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13230363.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B013AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B013AF.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13420342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13420342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/134203B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/134203B7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13420552.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13420552.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132331A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132331A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132344B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132314E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132314E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13232358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13232358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E3036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E3036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D0547.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA13AF.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA13AF.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0547012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547012D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13AF13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13AF13BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A80323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A80323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F4041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F4041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01220403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01220403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B70552.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B70552.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B71342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B71342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA0553.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA0553.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032301A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032301A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0323035E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0323035E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03230358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03230358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03230394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03230394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03410466.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03410466.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03420552.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03420552.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03421342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03421342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035A041B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035A041B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035E0323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035E0323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0357036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0357036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03580323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03580323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0370.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0370.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E04E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E04E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0401.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0401.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E046B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E046B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E0503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E0503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E14E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E14E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036E34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036E34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0362036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0362036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03631323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03631323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036314E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036314E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03632358.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03632358.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036331A8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036331A8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036344B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036344B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0370036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0370036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0393036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0393036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03940323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA046A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA0469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA0469.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E3036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E3036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0401036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0401036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04030122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04030122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B01F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B01F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041B035A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041B035A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04400466.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04400466.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A04EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A04EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A0469.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A0469.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046A34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046A34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046B036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046B036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046C046D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046C046D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046C34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046C34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046D046C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046D046C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046D34B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046D34B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04660341.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04660341.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04660440.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04660440.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046904EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046904EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0469046A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0469046A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046934B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046934B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0503036E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0503036E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055203B7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055203B7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05520342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05520342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05521342.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05521342.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B002E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B002E1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/050002E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/050002E1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E10500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E10500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E104E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E104E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036B02E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036B02E1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E502E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E502E1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E1032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E1032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E1036B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E1036B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02E10365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02E10365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036502E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036502E1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D02E1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D02E1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01F414E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01F414E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E401F4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E401F4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032304E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032304E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0352039B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0352039B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039B0352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039B0352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70323.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70323.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03CA0554.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03CA0554.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055403CA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055403CA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/057744B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057744B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00577.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0056E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0056E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056E44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21221403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21221403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14032122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14032122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA0577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA0577.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/057713BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057713BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/13BA056E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/13BA056E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056E13BA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E13BA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0547412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0547412C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C0547.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C0547.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012C412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012C412C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C012D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C012D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/012D412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/012D412C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01221403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01221403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04111403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04111403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03811403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03811403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01222122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01222122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03812122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03812122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220381.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220381.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220411.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220411.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04112122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04112122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14030403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14030403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04031403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04031403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21220403.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21220403.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04032122.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04032122.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C012C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C012C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D136B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D14E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D2365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D2365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B132D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B14E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B14E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B2365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B2365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5132D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E5136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E5136B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E52365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E52365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/2365132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/2365132D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/2365136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/2365136B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/236514E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236514E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/136B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/136B44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0136B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0136B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/236544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236544B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B02365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/132D44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/132D44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0132D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0132D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A402D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A402D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A902D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A902D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A90360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A904E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A904E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A90416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A90441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A90441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01A944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01A944B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D001A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D001A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D001A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D001A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D00360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D00360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D004E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D004E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D00416.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D00416.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/02D034B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/02D034B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/030704E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/030704E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03070458.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03070458.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03070462.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03070462.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/030734B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/030734B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036001A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036001A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/036002D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/036002D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E801A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E801A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E802D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E802D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90307.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041601A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041601A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/041602D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/041602D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/044101A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/044101A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04580307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04580307.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04620307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04620307.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B002D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B002D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00307.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00307.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B001A9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B001A9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03260471.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03260471.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04710326.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04710326.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/047134B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/047134B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00471.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00471.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032634B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032634B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B00326.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B00326.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AD412C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AD412C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/412C03AD.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/412C03AD.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056C1570.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056C1570.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1570056C_1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1570056C_2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1570056C_4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1570056C_4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B01570.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B01570.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/157034B0_1.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_1.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/157034B0_2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/157034B0_4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/157034B0_4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A434B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03A434B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03A434B0.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE34B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AE34B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AE34B0.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF34B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03AF34B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03AF34B0.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B534B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03B534B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03B534B0.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055344B0.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055344B0.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055344B0.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A4.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003A4.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003A4.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AE.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AE.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AE.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AF.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003AF.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003AF.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B5.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B003B5.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B003B5.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00553.glyph $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.glyph
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00553.syn $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00553.syn
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/234353B3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/234353B3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0487145A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0487145A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/145A0487.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/145A0487.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/53B32343.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/53B32343.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0055A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0055A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055A44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0055B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0055B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055B44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055B44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/21A434B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/21A434B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/34B021A4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/34B021A4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30465.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30465.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/046504E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/046504E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039144B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039144B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00391.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00391.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/032D0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/032D0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333032D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333032D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330357.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330357.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330359.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330359.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330360.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330360.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330362.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330362.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330365.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330365.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330393.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330393.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330394.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330394.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330398.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330398.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330399.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330399.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0333039A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0333039A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330441.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330441.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E3.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E3.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E6.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E6.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E7.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E7.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/033304EA.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/033304EA.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330500.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330500.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330501.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330501.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330503.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330503.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03570333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03570333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03590333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03590333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03600333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03600333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03620333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03620333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03650333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03650333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03930333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03930333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03940333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03940333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03980333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03980333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03990333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03990333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/039A0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/039A0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04410333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04410333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E20333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E20333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E30333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E30333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E50333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E50333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E60333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E60333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E70333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E70333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04E90333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04E90333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04EA0333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04EA0333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05000333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05000333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05010333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05010333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05030333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05030333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330484.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03330485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03330485.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03540481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03540481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03662354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03662354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03850484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03850484.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038514E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038514E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038544B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03860485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03860485.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038614E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038614E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/038644B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/038644B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/03900481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/03900481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810390.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810390.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04810502.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04810502.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048114E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048114E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04812354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04812354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048144B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048144B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04840333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04840333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04840385.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04840385.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048414E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048414E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048444B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04850333.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04850333.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04850386.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04850386.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048514E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048514E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/048544B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/048544B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/05020481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/05020481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E20481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E20481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E22354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E22354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90385.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90385.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90386.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90386.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90484.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14E90485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14E90485.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23540366.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23540366.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/23540481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/23540481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235414E2.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235414E2.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/235444B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/235444B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E944B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00385.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00385.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00386.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00386.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00481.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00481.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00484.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00484.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00485.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00485.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B02354.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B02354.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B024E9.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B024E9.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/0497B4B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/0497B4B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B024E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B024E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04D00561.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D00561.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055EF204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055EF204.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055FF204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055FF204.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056104D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056104D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056E54B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056E54B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/11A554B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/11A554B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/1471A4B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/1471A4B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/14D0612C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/14D0612C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/155EF204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/155EF204.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/232D54B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/232D54B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/236B54B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/236B54B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24D02561.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24D02561.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E404B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E404B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E4F204.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E4F204.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/24E854B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/24E854B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/256124D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/256124D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/356154D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356154D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B0056E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0056E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B011A5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B011A5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B0232D.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0232D.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B0236B.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B0236B.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B024E8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B024E8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/612C14D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/612C14D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/A4B01471.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/A4B01471.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/B4B00497.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/B4B00497.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F20424E4.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F20424E4.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F204055E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204055E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F204055F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204055F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/F204155E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/F204155E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/01B504B8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/01B504B8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B801B5.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B801B5.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/035204B8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/035204B8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B80352.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B80352.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04B80025.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04B80025.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/002504B8.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/002504B8.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D03561.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D03561.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/04D0055F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/04D0055F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/055F04D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/055F04D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056944B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056944B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/056A44B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/056A44B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/156274D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/156274D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/156374D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/156374D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/355E54D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/355E54D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/355F54D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/355F54D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/356054D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/356054D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B00569.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B00569.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/44B0056A.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/44B0056A.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D0355E.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D0355E.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D0355F.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D0355F.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54D03560.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54D03560.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/556C84D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/556C84D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/734584D0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/734584D0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/74D01562.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/74D01562.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/74D01563.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/74D01563.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/84D0556C.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/84D0556C.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/84D07345.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/84D07345.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/057754B0.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/057754B0.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/iconv/54B00577.tbl $RPM_BUILD_ROOT/opt/mqm/lib/iconv/54B00577.tbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_zh_TW $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_TW
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ru_RU $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ru_RU
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_es_ES $RPM_BUILD_ROOT/opt/mqm/READMES/readme_es_ES
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_pt_BR $RPM_BUILD_ROOT/opt/mqm/READMES/readme_pt_BR
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_pl_PL $RPM_BUILD_ROOT/opt/mqm/READMES/readme_pl_PL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_zh_TW.BIG5 $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_TW.BIG5
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ja_JP.PCK $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ja_JP.PCK
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ko_KR $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ko_KR
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_zh_CN $RPM_BUILD_ROOT/opt/mqm/READMES/readme_zh_CN
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_en_US $RPM_BUILD_ROOT/opt/mqm/READMES/readme_en_US
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_it_IT $RPM_BUILD_ROOT/opt/mqm/READMES/readme_it_IT
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_de_DE $RPM_BUILD_ROOT/opt/mqm/READMES/readme_de_DE
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_hu_HU $RPM_BUILD_ROOT/opt/mqm/READMES/readme_hu_HU
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_cs_CZ $RPM_BUILD_ROOT/opt/mqm/READMES/readme_cs_CZ
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_fr_FR $RPM_BUILD_ROOT/opt/mqm/READMES/readme_fr_FR
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/READMES/readme_ja_JP $RPM_BUILD_ROOT/opt/mqm/READMES/readme_ja_JP
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dmpmqcfg $RPM_BUILD_ROOT/opt/mqm/bin/dmpmqcfg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqver $RPM_BUILD_ROOT/opt/mqm/bin/dspmqver
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqenv $RPM_BUILD_ROOT/opt/mqm/bin/crtmqenv
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqenv $RPM_BUILD_ROOT/opt/mqm/bin/setmqenv
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqrc $RPM_BUILD_ROOT/opt/mqm/bin/mqrc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.commonservices.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.commonservices.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqiclen $RPM_BUILD_ROOT/opt/mqm/bin/amqiclen
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqinst $RPM_BUILD_ROOT/opt/mqm/bin/crtmqinst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dltmqinst $RPM_BUILD_ROOT/opt/mqm/bin/dltmqinst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/dspmqinst $RPM_BUILD_ROOT/opt/mqm/bin/dspmqinst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/setmqinst $RPM_BUILD_ROOT/opt/mqm/bin/setmqinst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Runtime-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Runtime-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.0.0.swidtag $RPM_BUILD_ROOT/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.0.0.swidtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqras $RPM_BUILD_ROOT/opt/mqm/bin/runmqras
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/isa.xml $RPM_BUILD_ROOT/opt/mqm/bin/isa.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqiclib $RPM_BUILD_ROOT/opt/mqm/bin/amqiclib
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicvar $RPM_BUILD_ROOT/opt/mqm/bin/amqicvar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicrel $RPM_BUILD_ROOT/opt/mqm/bin/amqicrel
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqicfil $RPM_BUILD_ROOT/opt/mqm/bin/amqicfil
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/mqconfig $RPM_BUILD_ROOT/opt/mqm/bin/mqconfig
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/instinfo.tsk $RPM_BUILD_ROOT/opt/mqm/instinfo.tsk
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqpatch.dat $RPM_BUILD_ROOT/opt/mqm/mqpatch.dat
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/runmqsc $RPM_BUILD_ROOT/opt/mqm/bin/runmqsc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/libcurl.so $RPM_BUILD_ROOT/opt/mqm/lib/libcurl.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libcurl.so $RPM_BUILD_ROOT/opt/mqm/lib64/libcurl.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libicudata.so.55.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libicudata.so.55.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libicuuc.so.55.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libicuuc.so.55.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libicui18n.so.55.1 $RPM_BUILD_ROOT/opt/mqm/lib64/libicui18n.so.55.1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/runmqccred $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/runmqccred
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/mqccred.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/mqccred.ini
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib/mqccred $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib/mqccred
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib/mqccred_r $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib/mqccred_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib64/mqccred $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64/mqccred
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqccred/lib64/mqccred_r $RPM_BUILD_ROOT/opt/mqm/samp/mqccred/lib64/mqccred_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/libedit.so $RPM_BUILD_ROOT/opt/mqm/lib64/libedit.so

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64/compat"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib/iconv"
%dir %attr(555,mqm,mqm) "/opt/mqm/msg"
%dir %attr(555,mqm,mqm) "/opt/mqm/msg/en_US"
%dir %attr(555,mqm,mqm) "/opt/mqm/READMES"
%dir %attr(555,mqm,mqm) "/opt/mqm/licenses"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/mqccred"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/mqccred/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/mqccred/lib64"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqm.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqm.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqe.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqe.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqecs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqecs.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqxzu.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqxzu.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzsd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzsd.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqz.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqz.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqm_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqm_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmcs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmcs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqe_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqe_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqecs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqecs_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqxzu_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqxzu_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqzsd_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqzsd_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqz_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqz_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjx_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjx_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqjxx_r.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqjxx_r.so"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqltmc0"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqb23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libimqb23gl_r.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqb23gl.so.4.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libimqb23gl_r.so.4.1"
%attr(444,mqm,mqm) "/opt/mqm/samp/ccsid.tbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/ccsid_part2.tbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/ccsid.new"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqs.ini"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqclient.ini"
%attr(444,mqm,mqm) "/opt/mqm/samp/service.env"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/strmqtrc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/endmqtrc"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqras"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqtrc"
%attr(444,mqm,mqm) "/opt/mqm/lib/amqtrc.fmt"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqxdbg"
%attr(6555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqxmsg0"
%attr(550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqicdir"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libmqmzse.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libmqmzse.so"
%attr(444,mqm,mqm) "/opt/mqm/msg/en_US/amq.cat"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002501B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250388.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250413.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011101B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011104E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011104FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011501B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011601B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011604E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011604FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011801B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011804E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011804FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D0381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01220381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01220411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012901B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01290333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01290352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01290381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012904E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012904FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C03AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D03AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A40360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A40416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A40441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A404E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A80358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A8035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A80394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A804E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B501F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F404E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D0365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D04E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D0500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033301B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033301F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0341037B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03410410.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03410440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0342039E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034203B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0343039F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034303B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03440387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03440412.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0344045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0344045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034503A0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03450564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03450569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0346036A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/034634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035201B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035201F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035204E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035204FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035404E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035704E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035801A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0358035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03580394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035804E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035904E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E01A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E0358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E0394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E04E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036001A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03600416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03600441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036004E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036101B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036101F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036104E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036204E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03640396.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036403EE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0365032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0365036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036504E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03650500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03660354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03660390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036604E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03660502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036701B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03670333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03670352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036704E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036704FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036A0346.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B0365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B04E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B0500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037004E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03700503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037B0341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037B0440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0381011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0381011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038101B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038101F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03810411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038104E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03870344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03870412.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0387045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03880025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0388045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039004E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0393046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039401A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03940358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0394035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039404E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03960364.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039603EE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039804E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03990458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039904E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A0462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A04E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039E0342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039E03B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039F0343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039F03B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039F34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A00345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A00564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A213BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A413BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A503CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A70567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A903C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AB13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AB34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B30343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B3039F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B403C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B503CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B603C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B70342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B7039E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C403A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C403B4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C403B6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03C434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA03A5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA03B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03EE0364.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03EE0396.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03EE34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0401046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040104E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04010503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04020359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04020398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040204E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04020501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04030381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04030411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04100341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04100440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04110403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04120344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04120387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04130025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0413045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041601A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04160360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04160441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041604E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041701B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04400341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0440037B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04400410.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044101A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04410360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04410416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044104E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0449044A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044A0449.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04580399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045804E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0388.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A0413.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B0344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B0387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045B34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0462039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046204E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04630464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04640463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04640465.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046404E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04650464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B0393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B0401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B04E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E3046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E401F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E5032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E50365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E5036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E50500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E701A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E7035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E801A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E80360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E80416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E80441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E834B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E9039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0500032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05000365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0500036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050004E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050104E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050204E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050234B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050334B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05640345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056403A0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05640569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05641345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05650567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056534B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056703A7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05670565.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0567056A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0567056C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05690345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05690564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05691345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056A0567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056C0567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13450564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13450569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03A2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03AB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03AE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA03AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B001F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00344.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00346.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00364.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0036A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0037B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00387.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00388.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00396.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0039F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003C4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003EE.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00410.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00412.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00413.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00449.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0044A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0045A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0045B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00564.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00565.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00567.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0056A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0056C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B013BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/readme.ccs"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035214E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E404E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E7035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01150476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011614E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01180478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046414E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036014E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033314E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039814E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011314E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20505.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/045814E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046214E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40113.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036614E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E50365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA0469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046914EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E14E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035714E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30463.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036514E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E3046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B14E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035C0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035F14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050014E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036214E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035914E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047904FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E80360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E204E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039914E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA14EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0118047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01160477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E714E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E814E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040114E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050414E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011114E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30464.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041614E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E80416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E514E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E801A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039014E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474035C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047404E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A14EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011C039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E214E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047801F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047414E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B5047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30465.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047504FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036114E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E701A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047604E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036714E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047604FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050514E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047601F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047614E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047704E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046514E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047704FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047901F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047714E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047804E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047814E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047501F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047901B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0474041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047914E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA04EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E50500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E414E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4011C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4035F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E504E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E404FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0116047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E4047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A14E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047601B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20504.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E70394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E70358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E704E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E804E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047401F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047804FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039414E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047701F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F40477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0115039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0115.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012914E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03610477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01110475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0476039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D04E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047401B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E9039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011D14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/011814E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E4011D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E60402.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035D14E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B035D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04750417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050114E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/040214E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E40479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047904E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770116.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A04FB.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0477047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04FB047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035414E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E80441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0417047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04770352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E314E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0479047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0361039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03520477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B01B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044114E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047504E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0475039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047701B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0025047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0478039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04760417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B50475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047501B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04790417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A0025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0111039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0111.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0118.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0129039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0129.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/037014E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E30357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002514E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E604E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E904E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050214E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C0477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E40367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E614E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B0417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A414E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E914E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04780417.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04170478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/00250474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0361.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04740352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B0479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047801B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0367047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D0367.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E644B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E244B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047C44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047D44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E744B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047644B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047744B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0047D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00474.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00475.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00476.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00477.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00478.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00479.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14EA44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039C44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0039C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B014E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B01323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13AF34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/054703AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B031A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B02358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00553.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0547012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00554.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23580363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E731A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23581323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A814E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A81323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235831A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A80363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E72358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E71323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E70363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A82358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055303CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B004EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/31A844B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0046D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0046C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B0046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13230363.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B013AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13420342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/134203B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13420552.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132331A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132314E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13232358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E3036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA13AF.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0547012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13AF13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A80323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F4041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01220403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B70552.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B71342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA0553.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032301A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0323035E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03230358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03230394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03410466.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03420552.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03421342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035A041B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035E0323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0357036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03580323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0370.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E04E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0401.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E046B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E0503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E14E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036E34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0362036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03631323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036314E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03632358.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036331A8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036344B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0370036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0393036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03940323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA0469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E3036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0401036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04030122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B01F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041B035A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04400466.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A04EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A0469.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046A34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046B036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046C046D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046C34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046D046C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046D34B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04660341.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04660440.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046904EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0469046A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046934B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0503036E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055203B7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05520342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05521342.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B002E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/050002E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E10500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E104E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036B02E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E502E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E1032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E1036B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02E10365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036502E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D02E1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01F414E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E401F4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032304E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0352039B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039B0352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70323.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03CA0554.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055403CA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/057744B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00577.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0056E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056E44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21221403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14032122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA0577.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/057713BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/13BA056E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056E13BA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0547412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C0547.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012C412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C012D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/012D412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01221403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04111403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03811403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01222122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03812122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220381.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220411.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04112122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14030403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04031403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21220403.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04032122.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C012C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D2365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B14E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B2365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E5136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E52365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/2365132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/2365136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/236514E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/136B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0136B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/236544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B02365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/132D44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0132D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A402D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A902D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A90360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A904E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A90416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A90441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01A944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D001A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D001A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D00360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D004E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D00416.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/02D034B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/030704E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03070458.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03070462.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/030734B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036001A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/036002D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E801A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E802D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041601A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/041602D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/044101A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04580307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04620307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B002D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00307.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B001A9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03260471.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04710326.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/047134B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00471.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032634B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B00326.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AD412C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/412C03AD.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056C1570.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1570056C_1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1570056C_2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1570056C_4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B01570.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/157034B0_1.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/157034B0_2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/157034B0_4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A434B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03A434B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE34B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AE34B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF34B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03AF34B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B534B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03B534B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055344B0.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055344B0.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A4.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003A4.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AE.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AE.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AF.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003AF.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B5.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B003B5.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00553.glyph"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00553.syn"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/234353B3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0487145A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/145A0487.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/53B32343.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0055A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0055B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055B44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/21A434B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/34B021A4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30465.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/046504E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039144B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00391.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/032D0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333032D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330357.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330359.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330360.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330362.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330365.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330393.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330394.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330398.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330399.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0333039A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330441.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E3.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E6.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E7.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/033304EA.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330500.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330501.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330503.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03570333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03590333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03600333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03620333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03650333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03930333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03940333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03980333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03990333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/039A0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04410333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E20333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E30333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E50333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E60333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E70333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04E90333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04EA0333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05000333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05010333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05030333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03330485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03540481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03662354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03850484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038514E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03860485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038614E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/038644B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/03900481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810390.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04810502.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048114E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04812354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048144B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04840333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04840385.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048414E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04850333.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04850386.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048514E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/048544B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/05020481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E20481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E22354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90385.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90386.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14E90485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23540366.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/23540481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235414E2.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/235444B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00385.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00386.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00481.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00484.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00485.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B02354.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B024E9.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/0497B4B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B024E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04D00561.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055EF204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055FF204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056104D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056E54B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/11A554B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/1471A4B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/14D0612C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/155EF204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/232D54B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/236B54B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24D02561.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E404B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E4F204.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/24E854B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/256124D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/356154D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B0056E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B011A5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B0232D.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B0236B.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B024E8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/612C14D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/A4B01471.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/B4B00497.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F20424E4.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F204055E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F204055F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/F204155E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/01B504B8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B801B5.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/035204B8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B80352.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04B80025.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/002504B8.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D03561.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/04D0055F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/055F04D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056944B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/056A44B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/156274D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/156374D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/355E54D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/355F54D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/356054D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B00569.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/44B0056A.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D0355E.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D0355F.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54D03560.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/556C84D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/734584D0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/74D01562.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/74D01563.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/84D0556C.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/84D07345.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/057754B0.tbl"
%attr(444,bin,bin) "/opt/mqm/lib/iconv/54B00577.tbl"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_zh_TW"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ru_RU"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_es_ES"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_pt_BR"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_pl_PL"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_zh_TW.BIG5"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ja_JP.PCK"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ko_KR"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_zh_CN"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_en_US"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_it_IT"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_de_DE"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_hu_HU"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_cs_CZ"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_fr_FR"
%attr(444,mqm,mqm) "/opt/mqm/READMES/readme_ja_JP"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dmpmqcfg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqver"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqenv"
%attr(555,mqm,mqm) "/opt/mqm/bin/setmqenv"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/mqrc"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.commonservices.jar"
%attr(6550,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqiclen"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqinst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dltmqinst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/dspmqinst"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/setmqinst"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ-9.0.0.mqtag"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Runtime-9.0.0.mqtag"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/ibm.com_IBM_MQ_Advanced_for_Developers_Non-Warranted-9.0.0.swidtag"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.tools.ras.jar"
%attr(555,mqm,mqm) "/opt/mqm/bin/runmqras"
%attr(444,bin,mqm) "/opt/mqm/bin/isa.xml"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqiclib"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/amqicvar"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqicrel"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqicfil"
%attr(555,mqm,mqm) "/opt/mqm/bin/mqconfig"
%attr(444,mqm,mqm) "/opt/mqm/instinfo.tsk"
%attr(444,mqm,mqm) "/opt/mqm/mqpatch.dat"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/runmqsc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/libcurl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libcurl.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libicudata.so.55.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libicuuc.so.55.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libicui18n.so.55.1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/runmqccred"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqccred/mqccred.ini"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib/mqccred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib/mqccred_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib64/mqccred"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/mqccred/lib64/mqccred_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/libedit.so"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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
#   years="2005,2014" 
#   crc="935548272" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2014 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# 
# Preinstallation script for MQSeriesRuntime package
# 
# Check for mqm group and user
# 
# Set up environment variables
TMPDIR="/tmp"
RC=0
DUMMY=""

create_mqm_group()
{
  echo "Creating group mqm"
  ErrorText=`groupadd mqm 2>&1`
  RC=$?
  if [ $RC -ne 0 ]; then
    echo "ERROR:  Failed to add 'mqm' group:" >&2
    echo $ErrorText >&2
    exit $RC
  fi
}
# Determine if the group exists on the system.  The solution used here is to
# create a file in the temporary location, attempt to change its group id to
# mqm.  This method should work independent of the multitude of ways groups can
# be defined across distributions and network environments
TMPFILE="${TMPDIR}/amq_grouptest"
touch $TMPFILE 2>/dev/null
if [ -f "$TMPFILE" ]; then
  chown :mqm $TMPFILE 2>/dev/null
  if [ $? -ne 0 ]; then
    create_mqm_group
  fi
  rm -f $TMPFILE
else  # Unable to create temporary file.  This is also needed by other install
      # processes - so it is fair to abort the install at this point
  echo "ERROR: Unable to write to ${TMPDIR} - aborting install"
  exit 1
fi

# Determine if the user id "mqm" exists, and is in the group mqm
ErrorText=`id -u mqm 2>&1`
RC=$?
if [ $RC -ne 0 ]; then
  echo "Creating user mqm"
  ErrorText=`useradd -r -d /var/mqm -g mqm mqm 2>&1`
  RC=$?
  if [ $RC -ne 0 ]; then
    echo "ERROR:  Failed to add 'mqm' user:" >&2
    echo $ErrorText >&2
    exit $RC
  fi
else    # Check the user mqm is in the group mqm
  ErrorText=`id -Gn mqm | grep -w mqm 2>&1`
  if [ $? -ne 0 ]; then
    ErrorText=`usermod -G mqm mqm 2>&1`
    if [ $RC -ne 0 ]; then
      echo "ERROR:  Failed to add user mqm to group mqm:" >&2
      echo $ErrorText >&1
      echo $RC
    fi
  fi
fi
echo > /dev/null 2>/dev/null

%post
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqm.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqm.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqm.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqm.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libmqm_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libmqm_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libmqm_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libmqm_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so.4.1 to ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so.4.1 ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so to ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so to ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64/compat ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64/compat
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55.1 to ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55.1 ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55
# Linking ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55.1 to ${MQ_INSTALLATION_PATH}/lib64/libicudata.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libicudata.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55.1 ${MQ_INSTALLATION_PATH}/lib64/libicudata.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicudata.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicudata.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55.1 to ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55.1 ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55
# Linking ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55.1 to ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55.1 ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so
# Linking ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55.1 to ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55.1 ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55
# Linking ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55.1 to ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so
if [ ! -d ${MQ_INSTALLATION_PATH}/lib64 ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/lib64
else
    rm -f ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so
fi
ln -s ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55.1 ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so
chown -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/runtime_postinstall.sh
#
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2016" 
#   crc="1956258177" > 
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
# Postinstallation script for MQ

#
# Create the top-level data files / directories required for MQ
#
LANG=C
LC_MESSAGES=C
export LANG
export LC_MESSAGES

amqicdir_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/amqicdir -i -f 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from amqicdir for \"-i -f\", output is:" >&2
  echo "       ${amqicdir_out}" >&2
fi
# Some Debian based systems do not have a /usr/lib64 but 
# setminst -i will fail without it 
if [ ! -d /usr/lib64 ]  ; then 
  mkdir /usr/lib64
  chown 755 /usr/lib64
fi 
# Ensure that /usr/lib64 is in the default library search path 
if [ -d /etc/ld.so.conf.d ] ; then 
  echo "/usr/lib64" > /etc/ld.so.conf.d/mqm.conf
  ldconfig_out=`ldconfig -v 2>&1`
  rc=$?
  if [ $rc -ne 0 ] ; then
    echo "WARNING: Return code \"$rc\" from ldconfig, output is:" >&2
    echo "       ${ldconfig_out}" >&2
  fi
fi 

#
# Record the installation in the mqinst.ini file
#
crtmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/crtmqinst -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
 case $rc in 
  10)
    echo "WARNING: Return code \"$rc\" from crtmqinst for \"-p ${MQ_INSTALLATION_PATH} \", output is:" >&2
    echo "         ${crtmqinst_out}" >&2
  ;;
  *)
    echo "ERROR:   Return code \"$rc\" from crtmqinst for \"-p ${MQ_INSTALLATION_PATH} \", output is:" >&2
    echo "         ${crtmqinst_out}" >&2
  ;;
 esac
fi

#
# Create the installation specific files / directories.
# This must happen AFTER recording the installation in mqinst.ini
#
amqicdir_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/amqicdir -s -f 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from amqicdir for \"-s -f\", output is:" >&2
  echo "       ${amqicdir_out}" >&2
fi

# May want to get kernel parameters updated here. For now, don't do it.
kernel_mods=0
if [ $kernel_mods -eq 1 ]
then
echo "  Updating kernel parameters..."
  # Shared memory
  # Semaphores
  # If this worked, indicate that the kernel needs to be rebuilt and
  # the system rebooted.
fi

# Create the ssl directory for migrated queue managers
DefaultPrefix=`grep DefaultPrefix /var/mqm/mqs.ini | cut -f2 -d'='`
find $DefaultPrefix/qmgrs/* -type d -prune > /dev/null 2>&1
if [ $? = 0 ]; then
  for i  in $DefaultPrefix/qmgrs/* ; do
    qm_name=`basename $i`

    if [ "$qm_name" != "@SYSTEM" ]; then

      # Only operate on directory entries
      if [ -d "$DefaultPrefix/$qm_name" ]; then
        if [ ! -d  $DefaultPrefix/qmgrs/$qm_name/ssl ]; then
          mkdir $DefaultPrefix/qmgrs/$qm_name/ssl
          chown mqm:mqm  $DefaultPrefix/qmgrs/$qm_name/ssl
          chmod 2775  $DefaultPrefix/qmgrs/$qm_name/ssl
        fi
      fi

    fi
  done
fi

# Invoke setmqinst to refresh symlinks if this installation is the primary
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -r -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-r -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi
echo > /dev/null

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/copy_license.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2012" 
#   crc="512007515" > 
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

# If the license agreement was accepted, the license text in 16 national languages should have been
# installed into /tmp/mq_license_${RPM_PACKAGE_VERSION}.
# These need to be copied to ${MQ_INSTALLATION_PATH}/license.

if [ -d /tmp/mq_license_${RPM_PACKAGE_VERSION}/license ]
then
  mkdir -p ${MQ_INSTALLATION_PATH}/licenses 2>/dev/null
  cp  /tmp/mq_license_${RPM_PACKAGE_VERSION}/license/* ${MQ_INSTALLATION_PATH}/licenses 2>/dev/null
  chown -R mqm ${MQ_INSTALLATION_PATH}/licenses  2>/dev/null
  chgrp -R mqm ${MQ_INSTALLATION_PATH}/licenses 2>/dev/null
  chmod 444 ${MQ_INSTALLATION_PATH}/licenses/*.* 2>/dev/null
  rm -Rf /tmp/mq_license_${RPM_PACKAGE_VERSION}
fi


%preun
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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
# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/runtime_preuninstall.sh
#
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72" 
#   years="2005,2015" 
#   crc="598641773" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72 
#    
#   (C) Copyright IBM Corp. 2005, 2015 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
#
# Pre uninstallation script
#####################################################################################
# Remove the mqccred exits from /var/mqm
#####################################################################################
rm -f /var/mqm/exits/`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b`/mqccred*
rm -f /var/mqm/exits64/`${MQ_INSTALLATION_PATH}/bin/dspmqver -f512 -b`/mqccred*


# If this installation is currently the primary remove any symlinks.
setmqinst_out=`LD_LIBRARY_PATH="" ${MQ_INSTALLATION_PATH}/bin/setmqinst -U -p ${MQ_INSTALLATION_PATH} 2>&1`
rc=$?
if [ $rc -ne 0 ] ; then
  echo "ERROR: Return code \"$rc\" from setmqinst for \"-U -p ${MQ_INSTALLATION_PATH}\", output is:" >&2
  echo "       ${setmqinst_out}" >&2
fi

# Removes the license text files

find ${MQ_INSTALLATION_PATH}/licenses -type f | grep -v REDIST | xargs rm

echo "Resetting return code to success" > /dev/null

# Removing product links
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libmqm_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libmqm_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib/compat/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/compat/libimqb23gl_r.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libicudata.so.55
rm -f ${MQ_INSTALLATION_PATH}/lib64/libicudata.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so.55
rm -f ${MQ_INSTALLATION_PATH}/lib64/libicuuc.so
rm -f ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so.55
rm -f ${MQ_INSTALLATION_PATH}/lib64/libicui18n.so

%postun
RPM_PACKAGE_SUMMARY="IBM MQ Runtime FileSet"
RPM_PACKAGE_NAME="MQSeriesRuntime"
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

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/runtime_postuninstall.sh
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2005,2015" 
#   crc="632453442" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2005, 2015 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
# Post uninstallation script
FILE='@(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/runtime_postuninstall.sh'
MYENV=`env`

# Remove any interim fix backup directories

backups_count=`ls -1d  ${MQ_INSTALLATION_PATH}/fix-backups.* 2> /dev/null | wc -l` 
if [ $backups_count -ne 0 ] ; then 
  rm -rf ${MQ_INSTALLATION_PATH}/fix-backups.*
  rm -rf ${MQ_INSTALLATION_PATH}/mqpatch.log
  rm -rf ${MQ_INSTALLATION_PATH}/mqpatch.dat
fi

# Remove any remaining empty directories (except lost+found and .snapshots (GPFS),
# also honour AMQ_IGNORE_SNAPDIRNAME which allows user to supply location to ignore if .snapshots has been renamed)

if [ "${AMQ_IGNORE_SNAPDIRNAME}" = "" ] ; then
  SNAPDIR_NAME=".snapshots"
else
  SNAPDIR_NAME="${AMQ_IGNORE_SNAPDIRNAME}"
fi

find ${MQ_INSTALLATION_PATH} -depth -type d ! -name lost+found ! -name "${SNAPDIR_NAME}" -exec rmdir {} > /dev/null 2>&1 \;


echo "Resetting return code to success" > /dev/null

