Summary: IBM MQ Samples FileSet
Name: MQSeriesSamples
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
This package provides the sample applications which can be used to check a
IBM MQ installation using the verification procedures.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/samp
install -d $RPM_BUILD_ROOT/opt/mqm/samp/bin
install -d $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl
install -d $RPM_BUILD_ROOT/opt/mqm/samp/xatm
install -d $RPM_BUILD_ROOT/opt/mqm/samp/dlq
install -d $RPM_BUILD_ROOT/opt/mqm/samp/pubsub
install -d $RPM_BUILD_ROOT/opt/mqm/inc
install -d $RPM_BUILD_ROOT/opt/mqm/samp/soap
install -d $RPM_BUILD_ROOT/opt/mqm/samp/soap/java
install -d $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/server
install -d $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/clients
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/http
install -d $RPM_BUILD_ROOT/opt/mqm/java/http/samples
install -d $RPM_BUILD_ROOT/opt/mqm/java/http/samples/src
install -d $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit
install -d $RPM_BUILD_ROOT/opt/mqm/lib
install -d $RPM_BUILD_ROOT/opt/mqm/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava
install -d $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper
install -d $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple
install -d $RPM_BUILD_ROOT/opt/mqm/samp/pcf
install -d $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Samples-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Samples-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscic0 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscic0
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscicc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscicc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscbf $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscbf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsech $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsech
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsact $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsact
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsinq $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsinq
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsset $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsset
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgbr $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgbr
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsget $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsget
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsreq $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsreq
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsput $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsput
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsapt $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsapt
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssub $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssub
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspub $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspub
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsptl $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsptl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqstrg $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqstrg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsbcg $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsbcg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgrm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgrm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsprm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsprm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsqrm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsqrm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsxrm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsxrm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqswlm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqswlm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsrua $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsrua
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaxe $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaxe
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaxe_r $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaxe_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaem $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaem
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaem_r $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaem_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspse $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspse
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsmon $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmon
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsevt $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsevt
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsstm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsstm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsiqm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsiqm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/amqsvmha.h $RPM_BUILD_ROOT/opt/mqm/inc/amqsvmha.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsgbr0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsgbr0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscbf0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqscbf0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsget0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsget0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsact0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsact0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsinqa.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsinqa.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstrg0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstrg0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsreq0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsreq0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsput0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsput0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsapt0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsapt0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqssuba.c $RPM_BUILD_ROOT/opt/mqm/samp/amqssuba.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqspuba.c $RPM_BUILD_ROOT/opt/mqm/samp/amqspuba.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsptl0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsptl0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsseta.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsseta.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsecha.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsecha.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsvfc0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsvfc0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsbcg0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsbcg0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsgrma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsgrma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsprma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsprma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsqrma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsqrma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsxrma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsxrma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqswlm0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqswlm0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaxe0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaxe0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaem0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaem0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqspse0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqspse0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsmon0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsmon0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsevta.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsevta.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaicq.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaicq.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsaiem.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsaiem.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsailq.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsailq.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsstop.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsstop.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscnxc.c $RPM_BUILD_ROOT/opt/mqm/samp/amqscnxc.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqssslc.c $RPM_BUILD_ROOT/opt/mqm/samp/amqssslc.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsstma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsstma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsiqma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsiqma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscos0.tst $RPM_BUILD_ROOT/opt/mqm/samp/amqscos0.tst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsruaa.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsruaa.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqmechx.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amqmechx.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqmsetx.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amqmsetx.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0gbr0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0gbr0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0get0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0get0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0ptl0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0ptl0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqminqx.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amqminqx.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0put0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0put0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0req0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0req0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqmdefs.tst $RPM_BUILD_ROOT/opt/mqm/samp/amqmdefs.tst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0pub0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0pub0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amq0sub0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/amq0sub0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscic0.ccs $RPM_BUILD_ROOT/opt/mqm/samp/amqscic0.ccs
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscic0.tst $RPM_BUILD_ROOT/opt/mqm/samp/amqscic0.tst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqscih0.h $RPM_BUILD_ROOT/opt/mqm/samp/amqscih0.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqzscix.c $RPM_BUILD_ROOT/opt/mqm/samp/amqzscix.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqzscgx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqzscgx.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/xa.h $RPM_BUILD_ROOT/opt/mqm/samp/xatm/xa.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.sqc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.sqc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.ec $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.ec
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.cp $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.cp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxas0.pc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxas0.pc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxag0.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxag0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxag0.c.inf $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxag0.c.inf
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxab0.sqc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxab0.sqc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxab0.ec $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxab0.ec
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxaf0.sqc $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxaf0.sqc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amqsxaf0.ec $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amqsxaf0.ec
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xas0.sqb $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xas0.sqb
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xag0.cbl $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xag0.cbl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xab0.sqb $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xab0.sqb
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/amq0xaf0.sqb $RPM_BUILD_ROOT/opt/mqm/samp/xatm/amq0xaf0.sqb
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/xaswit.mak $RPM_BUILD_ROOT/opt/mqm/samp/xatm/xaswit.mak
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/db2swit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/db2swit.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/db2swits.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/db2swits.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/oraswit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/oraswit.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/oraswitd.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/oraswitd.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/sybswit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/sybswit.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/xatm/infswit.c $RPM_BUILD_ROOT/opt/mqm/samp/xatm/infswit.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxgx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstxgx.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxpx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstxpx.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxsx.c $RPM_BUILD_ROOT/opt/mqm/samp/amqstxsx.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/ubbstxcx.cfg $RPM_BUILD_ROOT/opt/mqm/samp/ubbstxcx.cfg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxvx.v $RPM_BUILD_ROOT/opt/mqm/samp/amqstxvx.v
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqstxvx.flds $RPM_BUILD_ROOT/opt/mqm/samp/amqstxvx.flds
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqka.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqka.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqla.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqla.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqma.y $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.y
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqna.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqna.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqoa.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqoa.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqpa.l $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqpa.l
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqha.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqha.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodkha.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodkha.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodtha.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodtha.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqpa.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqpa.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqua.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqua.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqx.mk $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqx.mk
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqma.c $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqodqma.h $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqodqma.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/dlq/amqsdlq.msg $RPM_BUILD_ROOT/opt/mqm/samp/dlq/amqsdlq.msg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsdlq $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsdlq
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsputc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsputc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsaptc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsaptc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssubc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssubc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspubc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspubc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsptlc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsptlc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscnxc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscnxc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssslc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssslc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqscbfc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqscbfc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgetc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgetc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgrmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgrmc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsprmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsprmc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqstrgc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqstrgc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgbrc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgbrc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsreqc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsreqc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssetc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssetc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsbcgc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsbcgc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsactc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsactc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsinqc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsinqc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsechc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsechc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsstmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsstmc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsiqmc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsiqmc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsruac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsruac
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqdputs $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqdputs
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsputs $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsputs
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsgets $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsgets
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqwrlds $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqwrlds
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqdputc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqdputc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsputc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsputc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqsgetc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqsgetc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/gl/imqwrldc $RPM_BUILD_ROOT/opt/mqm/samp/bin/gl/imqwrldc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqdput.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqdput.cpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqsget.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqsget.cpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqsput.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqsput.cpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/imqwrld.cpp $RPM_BUILD_ROOT/opt/mqm/samp/imqwrld.cpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsppc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsppc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsspc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsspc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspr1 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspr1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssr1 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssr1
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqspr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqspr2
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssr2
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsrr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsrr2
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgr2 $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgr2
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsgam $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsgam
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsres $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsres
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsspca.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsspca.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqspr1a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspr1a.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqssr1a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqssr1a.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqspr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspr2a.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqssr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqssr2a.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsrr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsrr2a.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsgr2a.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgr2a.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsppca.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsppca.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsgama.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgama.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsgama.tst $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsgama.tst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqspsra.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqspsra.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsresa.c $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsresa.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pubsub/amqsresa.tst $RPM_BUILD_ROOT/opt/mqm/samp/pubsub/amqsresa.tst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqssbxa.c $RPM_BUILD_ROOT/opt/mqm/samp/amqssbxa.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssbx $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssbx
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqssbxc $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqssbxc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/java/server/StockQuoteAxis.java $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/server/StockQuoteAxis.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/java/clients/RunIvt.java $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/clients/RunIvt.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/java/clients/SQAxis2DotNet.java $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/clients/SQAxis2DotNet.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/java/clients/SQAxis2Axis.java $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/clients/SQAxis2Axis.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/java/clients/WsdlClient.java $RPM_BUILD_ROOT/opt/mqm/samp/soap/java/clients/WsdlClient.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/local_settings $RPM_BUILD_ROOT/opt/mqm/samp/soap/local_settings
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/ivttests_unix.txt $RPM_BUILD_ROOT/opt/mqm/samp/soap/ivttests_unix.txt
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/regenDemo.sh $RPM_BUILD_ROOT/opt/mqm/samp/soap/regenDemo.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/runivt.sh $RPM_BUILD_ROOT/opt/mqm/samp/soap/runivt.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/setupWMQSOAP.sh $RPM_BUILD_ROOT/opt/mqm/samp/soap/setupWMQSOAP.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/SOAPCleanup.sh $RPM_BUILD_ROOT/opt/mqm/samp/soap/SOAPCleanup.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/soap/DeployWMQService.java $RPM_BUILD_ROOT/opt/mqm/samp/soap/DeployWMQService.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/http/samples/src/HTTPPOST.java $RPM_BUILD_ROOT/opt/mqm/java/http/samples/src/HTTPPOST.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/http/samples/HTTPPOST.class $RPM_BUILD_ROOT/opt/mqm/java/http/samples/HTTPPOST.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/http/samples/HTTPDELETE.class $RPM_BUILD_ROOT/opt/mqm/java/http/samples/HTTPDELETE.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/http/samples/src/HTTPDELETE.java $RPM_BUILD_ROOT/opt/mqm/java/http/samples/src/HTTPDELETE.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsblst.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsblst.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsblst $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsblst
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqslog0.c $RPM_BUILD_ROOT/opt/mqm/samp/amqslog0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsphac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsphac.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsghac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsghac.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsmhac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsmhac.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsfhac.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsfhac.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsphac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsphac
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsghac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsghac
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsmhac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsmhac
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsfhac $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsfhac
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/amqsclma.c $RPM_BUILD_ROOT/opt/mqm/samp/amqsclma.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqsclm $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqsclm
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/preconnexit/amqlcel0.c $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit/amqlcel0.c
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqlcelp $RPM_BUILD_ROOT/opt/mqm/lib/amqlcelp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib/amqlcelp_r $RPM_BUILD_ROOT/opt/mqm/lib/amqlcelp_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqlcelp $RPM_BUILD_ROOT/opt/mqm/lib64/amqlcelp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/lib64/amqlcelp_r $RPM_BUILD_ROOT/opt/mqm/lib64/amqlcelp_r
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/preconnexit/ibm-amq.schema $RPM_BUILD_ROOT/opt/mqm/samp/preconnexit/ibm-amq.schema
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/mqat.ini $RPM_BUILD_ROOT/opt/mqm/samp/mqat.ini
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/bin/amqauthg.sh $RPM_BUILD_ROOT/opt/mqm/samp/bin/amqauthg.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQIVP.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQIVP.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample\$Subscriber.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample\$Subscriber.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSample.class $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSample.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQIVP.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQIVP.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSample.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSample.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/wmqjava/samples/mqjcivp.properties $RPM_BUILD_ROOT/opt/mqm/samp/wmqjava/samples/mqjcivp.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsBrowser.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsBrowser.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsConsumer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsConsumer.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiBrowser.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiBrowser.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiConsumer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiConsumer.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiProducer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiProducer.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsProducer.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsProducer.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava\$1.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava\$1.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Keys.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Keys.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Literals.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Literals.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Options.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Options.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Keys.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Keys.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Literals.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Literals.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/Options.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/Options.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePTP.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePubSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePubSub.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleRequestor.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRequestor.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleResponder\$SimpleMessageListener.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleResponder\$SimpleMessageListener.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleResponder.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleResponder.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePTP.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimplePubSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimplePubSub.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleRequestor.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRequestor.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleResponder.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleResponder.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsBrowser.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsBrowser.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsConsumer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsConsumer.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiBrowser.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiBrowser.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiConsumer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiConsumer.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsJndiProducer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsJndiProducer.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/jms/samples/JmsProducer.java $RPM_BUILD_ROOT/opt/mqm/samp/jms/samples/JmsProducer.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StartChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StartChannel.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StopChannel.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StopChannel.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StartChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StartChannel.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_StopChannel.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_StopChannel.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java $RPM_BUILD_ROOT/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/bin/gl"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/xatm"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/dlq"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/pubsub"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/soap"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/soap/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/soap/java/server"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/soap/java/clients"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/http"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/http/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/http/samples/src"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/preconnexit"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/wmqjava"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/wmqjava/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/jms/samples/simple"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/pcf"
%dir %attr(555,mqm,mqm) "/opt/mqm/samp/pcf/samples"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Samples-9.0.0.mqtag"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscic0"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscicc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscbf"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsech"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsact"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsinq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsset"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgbr"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsget"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsreq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsput"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsapt"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssub"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspub"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsptl"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqstrg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsbcg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgrm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsprm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsqrm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsxrm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqswlm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsrua"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaxe"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaxe_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaem"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaem_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspse"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsmon"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsevt"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsstm"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsiqm"
%attr(444,mqm,mqm) "/opt/mqm/inc/amqsvmha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsgbr0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscbf0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsget0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsact0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsinqa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstrg0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsreq0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsput0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsapt0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqssuba.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqspuba.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsptl0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsseta.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsecha.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsvfc0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsbcg0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsgrma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsprma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsqrma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsxrma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqswlm0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaxe0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaem0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqspse0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsmon0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsevta.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaicq.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsaiem.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsailq.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsstop.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscnxc.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqssslc.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsstma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsiqma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscos0.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsruaa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqmechx.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqmsetx.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0gbr0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0get0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0ptl0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqminqx.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0put0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0req0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqmdefs.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0pub0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amq0sub0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscic0.ccs"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscic0.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqscih0.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqzscix.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqzscgx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/xa.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.sqc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.ec"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.cp"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxas0.pc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxag0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxag0.c.inf"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxab0.sqc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxab0.ec"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxaf0.sqc"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amqsxaf0.ec"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xas0.sqb"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xag0.cbl"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xab0.sqb"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/amq0xaf0.sqb"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/xaswit.mak"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/db2swit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/db2swits.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/oraswit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/oraswitd.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/sybswit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/xatm/infswit.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxgx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxpx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxsx.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/ubbstxcx.cfg"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxvx.v"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqstxvx.flds"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqka.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqla.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqma.y"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqna.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqoa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqpa.l"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodkha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodtha.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqpa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqua.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqx.mk"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqma.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqodqma.h"
%attr(444,mqm,mqm) "/opt/mqm/samp/dlq/amqsdlq.msg"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsdlq"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsputc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsaptc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssubc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspubc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsptlc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscnxc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssslc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqscbfc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgetc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgrmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsprmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqstrgc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgbrc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsreqc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssetc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsbcgc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsactc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsinqc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsechc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsstmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsiqmc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsruac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqdputs"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsputs"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsgets"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqwrlds"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqdputc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsputc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqsgetc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/gl/imqwrldc"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqdput.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqsget.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqsput.cpp"
%attr(444,mqm,mqm) "/opt/mqm/samp/imqwrld.cpp"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsppc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsspc"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspr1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssr1"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqspr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsrr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgr2"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsgam"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsres"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsspca.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqspr1a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqssr1a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqspr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqssr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsrr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsgr2a.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsppca.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsgama.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsgama.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqspsra.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsresa.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/pubsub/amqsresa.tst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqssbxa.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssbx"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqssbxc"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/java/server/StockQuoteAxis.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/java/clients/RunIvt.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/java/clients/SQAxis2DotNet.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/java/clients/SQAxis2Axis.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/java/clients/WsdlClient.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/local_settings"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/ivttests_unix.txt"
%attr(555,mqm,mqm) "/opt/mqm/samp/soap/regenDemo.sh"
%attr(555,mqm,mqm) "/opt/mqm/samp/soap/runivt.sh"
%attr(555,mqm,mqm) "/opt/mqm/samp/soap/setupWMQSOAP.sh"
%attr(555,mqm,mqm) "/opt/mqm/samp/soap/SOAPCleanup.sh"
%attr(444,mqm,mqm) "/opt/mqm/samp/soap/DeployWMQService.java"
%attr(444,mqm,mqm) "/opt/mqm/java/http/samples/src/HTTPPOST.java"
%attr(444,mqm,mqm) "/opt/mqm/java/http/samples/HTTPPOST.class"
%attr(444,mqm,mqm) "/opt/mqm/java/http/samples/HTTPDELETE.class"
%attr(444,mqm,mqm) "/opt/mqm/java/http/samples/src/HTTPDELETE.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsblst.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsblst"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqslog0.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsphac.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsghac.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsmhac.c"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsfhac.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsphac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsghac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsmhac"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsfhac"
%attr(444,mqm,mqm) "/opt/mqm/samp/amqsclma.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/samp/bin/amqsclm"
%attr(444,mqm,mqm) "/opt/mqm/samp/preconnexit/amqlcel0.c"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqlcelp"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib/amqlcelp_r"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqlcelp"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/lib64/amqlcelp_r"
%attr(444,mqm,mqm) "/opt/mqm/samp/preconnexit/ibm-amq.schema"
%attr(444,mqm,mqm) "/opt/mqm/samp/mqat.ini"
%attr(555,mqm,mqm) "/opt/mqm/samp/bin/amqauthg.sh"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQIVP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample$Subscriber.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSample.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/IMSBridgeSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQIVP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQMessagePropertiesSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQPubSubApiSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSample.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/MQSampleMessageManager.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/wmqjava/samples/mqjcivp.properties"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsBrowser.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsConsumer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiBrowser.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiConsumer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiProducer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsProducer.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava$1.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/MyContext.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Keys.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsGreaterThanOrEqualZero.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsOneWord.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidDestination.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidICConnFactName.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidICDestName.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidInitialContextURI.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidNumberOfMessages.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidPortNumber.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidRTTDestination.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Literals.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Options.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/BaseOptions.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/IsValidType.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/JmsApp.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Keys.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Literals.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/MyContext.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/Options.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/helper/OptionsPresenter.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleConsumerJava.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/interactive/SampleProducerJava.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePubSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleRequestor.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleResponder$SimpleMessageListener.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleResponder.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleAsyncPutPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleDurableSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleJNDILookup.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDRead.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleMQMDWrite.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimplePubSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleReadAheadPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleRequestor.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleResponder.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleRetainedPub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPTP.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/simple/SimpleWMQJMSPubSub.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsBrowser.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsConsumer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiBrowser.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiConsumer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsJndiProducer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/jms/samples/JmsProducer.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CommonMethods.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ClearQueue.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateQueue.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StartChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StopChannel.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.class"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ChannelStatus.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ClearQueue.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CommonMethods.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_CreateQueue.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DeleteQueue.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalChannels.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayActiveLocalQueues.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_DisplayConnections.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_ListQueueNames.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StartChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_StopChannel.java"
%attr(444,mqm,mqm) "/opt/mqm/samp/pcf/samples/PCF_WalkThroughQueueManagerAttributes.java"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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

echo > /dev/null 2>/dev/null

%post
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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

%preun
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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

# Removing product links

%postun
RPM_PACKAGE_SUMMARY="IBM MQ Samples FileSet"
RPM_PACKAGE_NAME="MQSeriesSamples"
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

