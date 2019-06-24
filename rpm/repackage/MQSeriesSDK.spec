Summary: IBM MQ SDK FileSet
Name: MQSeriesSDK
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
This package provides sample source files and bindings (header files and
libraries) which are used to develop applications for use with IBM MQ.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/inc
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32
install -d $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_SDK-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_SDK-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqec.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqec.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqcfc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqcfc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqxc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqxc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqbc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqbc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqpsc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqpsc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqzc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqzc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cmqstrc.h $RPM_BUILD_ROOT/opt/mqm/inc/cmqstrc.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqair.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqair.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqbin.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqbin.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqcac.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqcac.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqchl.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqchl.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqcih.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqcih.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqdlh.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqdlh.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqdst.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqdst.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqerr.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqerr.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqgmo.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqgmo.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqhdr.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqhdr.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqi.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqi.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqiih.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqiih.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqitm.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqitm.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqmgr.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqmgr.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqmsg.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqmsg.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqmtr.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqmtr.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqnml.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqnml.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqobj.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqobj.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqpmo.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqpmo.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqpro.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqpro.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqque.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqque.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqrfh.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqrfh.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqstr.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqstr.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqtrg.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqtrg.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqtype.h $RPM_BUILD_ROOT/opt/mqm/inc/imqtype.h
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/imqwih.hpp $RPM_BUILD_ROOT/opt/mqm/inc/imqwih.hpp
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQBOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQBOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQBOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQBOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCIHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCIHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCIHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCIHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCNOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCNOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCNOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCNOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDLHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDLHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDLHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDLHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQGMOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQGMOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQGMOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQGMOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQIEPL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQIEPL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQIEPV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQIEPV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQIIHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQIIHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQIIHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQIIHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMDEL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMDEL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMDEV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMDEV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMD1L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMD1L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMD1V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMD1V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQODL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQODL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQODV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQODV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQORL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQORL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQORV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQORV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQPMOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQPMOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQPMOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQPMOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRFHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRFHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRFHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRFHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRMHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRMHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRMHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRMHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRRL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRRL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRRV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRRV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQTMC2L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQTMC2L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQTMC2V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQTMC2V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQTML $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQTML
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQTMV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQTMV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQWIHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQWIHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQWIHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQWIHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQXQHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQXQHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQXQHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQXQHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQXV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQXV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFILL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFILL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFILV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFILV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFINL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFINL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFINV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFINV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFSLL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFSLL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFSLV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFSLV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFSTL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFSTL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFSTV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFSTV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQPSV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQPSV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRFH2L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRFH2L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQRFH2V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQRFH2V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQEPHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQEPHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFBSV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFBSV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFGRV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFGRV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFSFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFSFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFXNV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFXNV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFXLV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFXLV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFIFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFIFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMD2V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMD2V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCSPV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCSPV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFBSL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFBSL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFGRL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFGRL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQEPHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQEPHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFSFL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFSFL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFXNL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFXNL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFXLL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFXLL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFIFL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFIFL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMD2L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMD2L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCSPL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCSPL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFBFL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFBFL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCFBFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCFBFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQAIRV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQAIRV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQAIRL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQAIRL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSCOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSCOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSCOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSCOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQBMHOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQBMHOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQBMHOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQBMHOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCBCV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCBCV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCBCL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCBCL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCBDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCBDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCBDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCBDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCHRVV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCHRVV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCHRVL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCHRVL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCMHOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCMHOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCMHOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCMHOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCTLOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCTLOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQCTLOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQCTLOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDMHOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDMHOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDMHOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDMHOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDMPOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDMPOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQDMPOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQDMPOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQIMPOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQIMPOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQIMPOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQIMPOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMHBOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMHBOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQMHBOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQMHBOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQPDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQPDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQPDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQPDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSMPOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSMPOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSMPOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSMPOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSROV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSROV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSROL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSROL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSTSV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSTSV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy32/CMQSTSL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy32/CMQSTSL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQBOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQBOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQBOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQBOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCIHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCIHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCIHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCIHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCNOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCNOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCNOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCNOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDLHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDLHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDLHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDLHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQGMOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQGMOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQGMOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQGMOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQIEPL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQIEPL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQIEPV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQIEPV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQIIHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQIIHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQIIHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQIIHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMDEL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMDEL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMDEV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMDEV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMD1L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMD1L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMD1V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMD1V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQODL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQODL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQODV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQODV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQORL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQORL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQORV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQORV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQPMOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQPMOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQPMOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQPMOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRFHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRFHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRFHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRFHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRMHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRMHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRMHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRMHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRRL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRRL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRRV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRRV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQTMC2L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQTMC2L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQTMC2V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQTMC2V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQTML $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQTML
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQTMV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQTMV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQWIHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQWIHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQWIHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQWIHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQXQHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQXQHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQXQHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQXQHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQXV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQXV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFILL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFILL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFILV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFILV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFINL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFINL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFINV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFINV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFSLL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFSLL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFSLV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFSLV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFSTL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFSTL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFSTV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFSTV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQPSV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQPSV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRFH2L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRFH2L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQRFH2V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQRFH2V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQEPHV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQEPHV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFGRV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFGRV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFSFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFSFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFXNV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFXNV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFXLV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFXLV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFIFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFIFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMD2V $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMD2V
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCSPV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCSPV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQAIRL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQAIRL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQAIRV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQAIRV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSCOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSCOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSCOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSCOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFGRL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFGRL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFBSL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFBSL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFBSV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFBSV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQEPHL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQEPHL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFSFL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFSFL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFXNL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFXNL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFXLL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFXLL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFIFL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFIFL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMD2L $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMD2L
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCSPL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCSPL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFBFL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFBFL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCFBFV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCFBFV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQBMHOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQBMHOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQBMHOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQBMHOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCBCV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCBCV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCBCL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCBCL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCBDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCBDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCBDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCBDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCHRVV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCHRVV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCHRVL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCHRVL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCMHOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCMHOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCMHOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCMHOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCTLOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCTLOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQCTLOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQCTLOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDMHOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDMHOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDMHOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDMHOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDMPOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDMPOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQDMPOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQDMPOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQIMPOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQIMPOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQIMPOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQIMPOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMHBOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMHBOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQMHBOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQMHBOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQPDV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQPDV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQPDL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQPDL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSMPOV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSMPOV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSMPOL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSMPOL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSROV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSROV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSROL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSROL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSTSV $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSTSV
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/inc/cobcpy64/CMQSTSL $RPM_BUILD_ROOT/opt/mqm/inc/cobcpy64/CMQSTSL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/crtmqcvx $RPM_BUILD_ROOT/opt/mqm/bin/crtmqcvx

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc/cobcpy32"
%dir %attr(555,mqm,mqm) "/opt/mqm/inc/cobcpy64"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_SDK-9.0.0.mqtag"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqec.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqcfc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqxc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqbc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqpsc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqzc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/cmqstrc.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqair.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqbin.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqcac.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqchl.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqcih.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqdlh.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqdst.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqerr.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqgmo.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqhdr.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqi.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqiih.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqitm.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqmgr.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqmsg.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqmtr.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqnml.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqobj.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqpmo.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqpro.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqque.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqrfh.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqstr.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqtrg.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqtype.h"
%attr(444,mqm,mqm) "/opt/mqm/inc/imqwih.hpp"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQBOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQBOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCIHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCIHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCNOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCNOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDLHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDLHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQGMOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQGMOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQIEPL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQIEPV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQIIHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQIIHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMDEL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMDEV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMD1L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMD1V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQODL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQODV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQORL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQORV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQPMOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQPMOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRFHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRFHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRMHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRMHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRRL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRRV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQTMC2L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQTMC2V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQTML"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQTMV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQWIHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQWIHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQXQHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQXQHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQXV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFILL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFILV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFINL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFINV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFSLL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFSLV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFSTL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFSTV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQPSV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRFH2L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQRFH2V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQEPHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFBSV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFGRV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFSFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFXNV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFXLV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFIFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMD2V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCSPV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFBSL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFGRL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQEPHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFSFL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFXNL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFXLL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFIFL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMD2L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCSPL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFBFL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCFBFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQAIRV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQAIRL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSCOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSCOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQBMHOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQBMHOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCBCV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCBCL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCBDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCBDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCHRVV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCHRVL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCMHOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCMHOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCTLOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQCTLOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDMHOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDMHOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDMPOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQDMPOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQIMPOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQIMPOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMHBOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQMHBOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQPDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQPDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSMPOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSMPOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSROV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSROL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSTSV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy32/CMQSTSL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQBOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQBOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCIHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCIHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCNOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCNOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDLHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDLHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQGMOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQGMOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQIEPL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQIEPV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQIIHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQIIHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMDEL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMDEV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMD1L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMD1V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQODL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQODV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQORL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQORV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQPMOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQPMOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRFHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRFHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRMHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRMHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRRL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRRV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQTMC2L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQTMC2V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQTML"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQTMV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQWIHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQWIHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQXQHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQXQHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQXV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFILL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFILV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFINL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFINV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFSLL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFSLV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFSTL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFSTV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQPSV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRFH2L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQRFH2V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQEPHV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFGRV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFSFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFXNV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFXLV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFIFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMD2V"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCSPV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQAIRL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQAIRV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSCOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSCOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFGRL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFBSL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFBSV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQEPHL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFSFL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFXNL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFXLL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFIFL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMD2L"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCSPL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFBFL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCFBFV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQBMHOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQBMHOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCBCV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCBCL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCBDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCBDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCHRVV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCHRVL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCMHOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCMHOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCTLOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQCTLOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDMHOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDMHOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDMPOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQDMPOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQIMPOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQIMPOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMHBOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQMHBOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQPDV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQPDL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSMPOV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSMPOL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSROV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSROL"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSTSV"
%attr(444,mqm,mqm) "/opt/mqm/inc/cobcpy64/CMQSTSL"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/bin/crtmqcvx"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ SDK FileSet"
RPM_PACKAGE_NAME="MQSeriesSDK"
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
RPM_PACKAGE_SUMMARY="IBM MQ SDK FileSet"
RPM_PACKAGE_NAME="MQSeriesSDK"
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
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBOL to ${MQ_INSTALLATION_PATH}/inc/CMQBOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBOL ${MQ_INSTALLATION_PATH}/inc/CMQBOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBOV to ${MQ_INSTALLATION_PATH}/inc/CMQBOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBOV ${MQ_INSTALLATION_PATH}/inc/CMQBOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCIHL to ${MQ_INSTALLATION_PATH}/inc/CMQCIHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCIHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCIHL ${MQ_INSTALLATION_PATH}/inc/CMQCIHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCIHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCIHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCIHV to ${MQ_INSTALLATION_PATH}/inc/CMQCIHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCIHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCIHV ${MQ_INSTALLATION_PATH}/inc/CMQCIHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCIHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCIHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCNOL to ${MQ_INSTALLATION_PATH}/inc/CMQCNOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCNOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCNOL ${MQ_INSTALLATION_PATH}/inc/CMQCNOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCNOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCNOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCNOV to ${MQ_INSTALLATION_PATH}/inc/CMQCNOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCNOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCNOV ${MQ_INSTALLATION_PATH}/inc/CMQCNOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCNOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCNOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDHL to ${MQ_INSTALLATION_PATH}/inc/CMQDHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDHL ${MQ_INSTALLATION_PATH}/inc/CMQDHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDHV to ${MQ_INSTALLATION_PATH}/inc/CMQDHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDHV ${MQ_INSTALLATION_PATH}/inc/CMQDHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDLHL to ${MQ_INSTALLATION_PATH}/inc/CMQDLHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDLHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDLHL ${MQ_INSTALLATION_PATH}/inc/CMQDLHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDLHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDLHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDLHV to ${MQ_INSTALLATION_PATH}/inc/CMQDLHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDLHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDLHV ${MQ_INSTALLATION_PATH}/inc/CMQDLHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDLHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDLHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQGMOL to ${MQ_INSTALLATION_PATH}/inc/CMQGMOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQGMOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQGMOL ${MQ_INSTALLATION_PATH}/inc/CMQGMOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQGMOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQGMOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQGMOV to ${MQ_INSTALLATION_PATH}/inc/CMQGMOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQGMOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQGMOV ${MQ_INSTALLATION_PATH}/inc/CMQGMOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQGMOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQGMOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIEPL to ${MQ_INSTALLATION_PATH}/inc/CMQIEPL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIEPL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIEPL ${MQ_INSTALLATION_PATH}/inc/CMQIEPL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIEPL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIEPL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIEPV to ${MQ_INSTALLATION_PATH}/inc/CMQIEPV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIEPV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIEPV ${MQ_INSTALLATION_PATH}/inc/CMQIEPV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIEPV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIEPV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIIHL to ${MQ_INSTALLATION_PATH}/inc/CMQIIHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIIHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIIHL ${MQ_INSTALLATION_PATH}/inc/CMQIIHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIIHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIIHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIIHV to ${MQ_INSTALLATION_PATH}/inc/CMQIIHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIIHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIIHV ${MQ_INSTALLATION_PATH}/inc/CMQIIHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIIHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIIHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDEL to ${MQ_INSTALLATION_PATH}/inc/CMQMDEL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDEL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDEL ${MQ_INSTALLATION_PATH}/inc/CMQMDEL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDEL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDEL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDEV to ${MQ_INSTALLATION_PATH}/inc/CMQMDEV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDEV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDEV ${MQ_INSTALLATION_PATH}/inc/CMQMDEV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDEV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDEV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDL to ${MQ_INSTALLATION_PATH}/inc/CMQMDL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDL ${MQ_INSTALLATION_PATH}/inc/CMQMDL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDV to ${MQ_INSTALLATION_PATH}/inc/CMQMDV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMDV ${MQ_INSTALLATION_PATH}/inc/CMQMDV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMDV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD1L to ${MQ_INSTALLATION_PATH}/inc/CMQMD1L
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD1L
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD1L ${MQ_INSTALLATION_PATH}/inc/CMQMD1L
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD1L
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD1L
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD1V to ${MQ_INSTALLATION_PATH}/inc/CMQMD1V
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD1V
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD1V ${MQ_INSTALLATION_PATH}/inc/CMQMD1V
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD1V
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD1V
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQODL to ${MQ_INSTALLATION_PATH}/inc/CMQODL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQODL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQODL ${MQ_INSTALLATION_PATH}/inc/CMQODL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQODL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQODL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQODV to ${MQ_INSTALLATION_PATH}/inc/CMQODV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQODV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQODV ${MQ_INSTALLATION_PATH}/inc/CMQODV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQODV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQODV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQORL to ${MQ_INSTALLATION_PATH}/inc/CMQORL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQORL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQORL ${MQ_INSTALLATION_PATH}/inc/CMQORL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQORL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQORL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQORV to ${MQ_INSTALLATION_PATH}/inc/CMQORV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQORV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQORV ${MQ_INSTALLATION_PATH}/inc/CMQORV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQORV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQORV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPMOL to ${MQ_INSTALLATION_PATH}/inc/CMQPMOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPMOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPMOL ${MQ_INSTALLATION_PATH}/inc/CMQPMOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPMOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPMOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPMOV to ${MQ_INSTALLATION_PATH}/inc/CMQPMOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPMOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPMOV ${MQ_INSTALLATION_PATH}/inc/CMQPMOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPMOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPMOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFHL to ${MQ_INSTALLATION_PATH}/inc/CMQRFHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFHL ${MQ_INSTALLATION_PATH}/inc/CMQRFHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFHV to ${MQ_INSTALLATION_PATH}/inc/CMQRFHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFHV ${MQ_INSTALLATION_PATH}/inc/CMQRFHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRMHL to ${MQ_INSTALLATION_PATH}/inc/CMQRMHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRMHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRMHL ${MQ_INSTALLATION_PATH}/inc/CMQRMHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRMHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRMHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRMHV to ${MQ_INSTALLATION_PATH}/inc/CMQRMHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRMHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRMHV ${MQ_INSTALLATION_PATH}/inc/CMQRMHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRMHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRMHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRRL to ${MQ_INSTALLATION_PATH}/inc/CMQRRL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRRL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRRL ${MQ_INSTALLATION_PATH}/inc/CMQRRL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRRL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRRL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRRV to ${MQ_INSTALLATION_PATH}/inc/CMQRRV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRRV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRRV ${MQ_INSTALLATION_PATH}/inc/CMQRRV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRRV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRRV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTMC2L to ${MQ_INSTALLATION_PATH}/inc/CMQTMC2L
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTMC2L
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTMC2L ${MQ_INSTALLATION_PATH}/inc/CMQTMC2L
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTMC2L
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTMC2L
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTMC2V to ${MQ_INSTALLATION_PATH}/inc/CMQTMC2V
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTMC2V
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTMC2V ${MQ_INSTALLATION_PATH}/inc/CMQTMC2V
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTMC2V
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTMC2V
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTML to ${MQ_INSTALLATION_PATH}/inc/CMQTML
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTML
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTML ${MQ_INSTALLATION_PATH}/inc/CMQTML
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTML
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTML
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTMV to ${MQ_INSTALLATION_PATH}/inc/CMQTMV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTMV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQTMV ${MQ_INSTALLATION_PATH}/inc/CMQTMV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTMV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQTMV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQWIHL to ${MQ_INSTALLATION_PATH}/inc/CMQWIHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQWIHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQWIHL ${MQ_INSTALLATION_PATH}/inc/CMQWIHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQWIHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQWIHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQWIHV to ${MQ_INSTALLATION_PATH}/inc/CMQWIHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQWIHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQWIHV ${MQ_INSTALLATION_PATH}/inc/CMQWIHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQWIHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQWIHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQXQHL to ${MQ_INSTALLATION_PATH}/inc/CMQXQHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQXQHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQXQHL ${MQ_INSTALLATION_PATH}/inc/CMQXQHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQXQHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQXQHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQXQHV to ${MQ_INSTALLATION_PATH}/inc/CMQXQHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQXQHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQXQHV ${MQ_INSTALLATION_PATH}/inc/CMQXQHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQXQHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQXQHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQV to ${MQ_INSTALLATION_PATH}/inc/CMQV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQV ${MQ_INSTALLATION_PATH}/inc/CMQV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCDL to ${MQ_INSTALLATION_PATH}/inc/CMQCDL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCDL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCDL ${MQ_INSTALLATION_PATH}/inc/CMQCDL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCDL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCDL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCDV to ${MQ_INSTALLATION_PATH}/inc/CMQCDV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCDV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCDV ${MQ_INSTALLATION_PATH}/inc/CMQCDV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCDV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCDV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQXV to ${MQ_INSTALLATION_PATH}/inc/CMQXV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQXV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQXV ${MQ_INSTALLATION_PATH}/inc/CMQXV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQXV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQXV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFHL to ${MQ_INSTALLATION_PATH}/inc/CMQCFHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFHL ${MQ_INSTALLATION_PATH}/inc/CMQCFHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFHV to ${MQ_INSTALLATION_PATH}/inc/CMQCFHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFHV ${MQ_INSTALLATION_PATH}/inc/CMQCFHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFILL to ${MQ_INSTALLATION_PATH}/inc/CMQCFILL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFILL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFILL ${MQ_INSTALLATION_PATH}/inc/CMQCFILL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFILL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFILL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFILV to ${MQ_INSTALLATION_PATH}/inc/CMQCFILV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFILV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFILV ${MQ_INSTALLATION_PATH}/inc/CMQCFILV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFILV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFILV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFINL to ${MQ_INSTALLATION_PATH}/inc/CMQCFINL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFINL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFINL ${MQ_INSTALLATION_PATH}/inc/CMQCFINL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFINL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFINL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFINV to ${MQ_INSTALLATION_PATH}/inc/CMQCFINV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFINV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFINV ${MQ_INSTALLATION_PATH}/inc/CMQCFINV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFINV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFINV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSLL to ${MQ_INSTALLATION_PATH}/inc/CMQCFSLL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSLL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSLL ${MQ_INSTALLATION_PATH}/inc/CMQCFSLL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSLL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSLL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSLV to ${MQ_INSTALLATION_PATH}/inc/CMQCFSLV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSLV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSLV ${MQ_INSTALLATION_PATH}/inc/CMQCFSLV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSLV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSLV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSTL to ${MQ_INSTALLATION_PATH}/inc/CMQCFSTL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSTL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSTL ${MQ_INSTALLATION_PATH}/inc/CMQCFSTL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSTL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSTL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSTV to ${MQ_INSTALLATION_PATH}/inc/CMQCFSTV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSTV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSTV ${MQ_INSTALLATION_PATH}/inc/CMQCFSTV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSTV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSTV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFV to ${MQ_INSTALLATION_PATH}/inc/CMQCFV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFV ${MQ_INSTALLATION_PATH}/inc/CMQCFV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPSV to ${MQ_INSTALLATION_PATH}/inc/CMQPSV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPSV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPSV ${MQ_INSTALLATION_PATH}/inc/CMQPSV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPSV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPSV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFH2L to ${MQ_INSTALLATION_PATH}/inc/CMQRFH2L
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFH2L
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFH2L ${MQ_INSTALLATION_PATH}/inc/CMQRFH2L
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFH2L
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFH2L
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFH2V to ${MQ_INSTALLATION_PATH}/inc/CMQRFH2V
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFH2V
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQRFH2V ${MQ_INSTALLATION_PATH}/inc/CMQRFH2V
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFH2V
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQRFH2V
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQEPHV to ${MQ_INSTALLATION_PATH}/inc/CMQEPHV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQEPHV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQEPHV ${MQ_INSTALLATION_PATH}/inc/CMQEPHV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQEPHV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQEPHV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBSV to ${MQ_INSTALLATION_PATH}/inc/CMQCFBSV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBSV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBSV ${MQ_INSTALLATION_PATH}/inc/CMQCFBSV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBSV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBSV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFGRV to ${MQ_INSTALLATION_PATH}/inc/CMQCFGRV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFGRV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFGRV ${MQ_INSTALLATION_PATH}/inc/CMQCFGRV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFGRV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFGRV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSFV to ${MQ_INSTALLATION_PATH}/inc/CMQCFSFV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSFV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSFV ${MQ_INSTALLATION_PATH}/inc/CMQCFSFV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSFV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSFV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXNV to ${MQ_INSTALLATION_PATH}/inc/CMQCFXNV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXNV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXNV ${MQ_INSTALLATION_PATH}/inc/CMQCFXNV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXNV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXNV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXLV to ${MQ_INSTALLATION_PATH}/inc/CMQCFXLV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXLV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXLV ${MQ_INSTALLATION_PATH}/inc/CMQCFXLV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXLV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXLV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFIFV to ${MQ_INSTALLATION_PATH}/inc/CMQCFIFV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFIFV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFIFV ${MQ_INSTALLATION_PATH}/inc/CMQCFIFV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFIFV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFIFV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD2V to ${MQ_INSTALLATION_PATH}/inc/CMQMD2V
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD2V
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD2V ${MQ_INSTALLATION_PATH}/inc/CMQMD2V
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD2V
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD2V
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCSPV to ${MQ_INSTALLATION_PATH}/inc/CMQCSPV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCSPV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCSPV ${MQ_INSTALLATION_PATH}/inc/CMQCSPV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCSPV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCSPV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBSL to ${MQ_INSTALLATION_PATH}/inc/CMQCFBSL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBSL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBSL ${MQ_INSTALLATION_PATH}/inc/CMQCFBSL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBSL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBSL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFGRL to ${MQ_INSTALLATION_PATH}/inc/CMQCFGRL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFGRL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFGRL ${MQ_INSTALLATION_PATH}/inc/CMQCFGRL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFGRL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFGRL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQEPHL to ${MQ_INSTALLATION_PATH}/inc/CMQEPHL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQEPHL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQEPHL ${MQ_INSTALLATION_PATH}/inc/CMQEPHL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQEPHL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQEPHL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSFL to ${MQ_INSTALLATION_PATH}/inc/CMQCFSFL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSFL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFSFL ${MQ_INSTALLATION_PATH}/inc/CMQCFSFL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSFL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFSFL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXNL to ${MQ_INSTALLATION_PATH}/inc/CMQCFXNL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXNL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXNL ${MQ_INSTALLATION_PATH}/inc/CMQCFXNL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXNL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXNL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXLL to ${MQ_INSTALLATION_PATH}/inc/CMQCFXLL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXLL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFXLL ${MQ_INSTALLATION_PATH}/inc/CMQCFXLL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXLL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFXLL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFIFL to ${MQ_INSTALLATION_PATH}/inc/CMQCFIFL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFIFL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFIFL ${MQ_INSTALLATION_PATH}/inc/CMQCFIFL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFIFL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFIFL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD2L to ${MQ_INSTALLATION_PATH}/inc/CMQMD2L
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD2L
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMD2L ${MQ_INSTALLATION_PATH}/inc/CMQMD2L
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD2L
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMD2L
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCSPL to ${MQ_INSTALLATION_PATH}/inc/CMQCSPL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCSPL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCSPL ${MQ_INSTALLATION_PATH}/inc/CMQCSPL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCSPL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCSPL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBFL to ${MQ_INSTALLATION_PATH}/inc/CMQCFBFL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBFL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBFL ${MQ_INSTALLATION_PATH}/inc/CMQCFBFL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBFL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBFL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBFV to ${MQ_INSTALLATION_PATH}/inc/CMQCFBFV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBFV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCFBFV ${MQ_INSTALLATION_PATH}/inc/CMQCFBFV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBFV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCFBFV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQAIRV to ${MQ_INSTALLATION_PATH}/inc/CMQAIRV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQAIRV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQAIRV ${MQ_INSTALLATION_PATH}/inc/CMQAIRV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQAIRV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQAIRV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQAIRL to ${MQ_INSTALLATION_PATH}/inc/CMQAIRL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQAIRL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQAIRL ${MQ_INSTALLATION_PATH}/inc/CMQAIRL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQAIRL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQAIRL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSCOV to ${MQ_INSTALLATION_PATH}/inc/CMQSCOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSCOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSCOV ${MQ_INSTALLATION_PATH}/inc/CMQSCOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSCOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSCOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSCOL to ${MQ_INSTALLATION_PATH}/inc/CMQSCOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSCOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSCOL ${MQ_INSTALLATION_PATH}/inc/CMQSCOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSCOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSCOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSDV to ${MQ_INSTALLATION_PATH}/inc/CMQSDV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSDV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSDV ${MQ_INSTALLATION_PATH}/inc/CMQSDV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSDV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSDV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSDL to ${MQ_INSTALLATION_PATH}/inc/CMQSDL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSDL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSDL ${MQ_INSTALLATION_PATH}/inc/CMQSDL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSDL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSDL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBMHOV to ${MQ_INSTALLATION_PATH}/inc/CMQBMHOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBMHOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBMHOV ${MQ_INSTALLATION_PATH}/inc/CMQBMHOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBMHOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBMHOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBMHOL to ${MQ_INSTALLATION_PATH}/inc/CMQBMHOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBMHOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQBMHOL ${MQ_INSTALLATION_PATH}/inc/CMQBMHOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBMHOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQBMHOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBCV to ${MQ_INSTALLATION_PATH}/inc/CMQCBCV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBCV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBCV ${MQ_INSTALLATION_PATH}/inc/CMQCBCV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBCV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBCV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBCL to ${MQ_INSTALLATION_PATH}/inc/CMQCBCL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBCL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBCL ${MQ_INSTALLATION_PATH}/inc/CMQCBCL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBCL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBCL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBDV to ${MQ_INSTALLATION_PATH}/inc/CMQCBDV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBDV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBDV ${MQ_INSTALLATION_PATH}/inc/CMQCBDV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBDV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBDV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBDL to ${MQ_INSTALLATION_PATH}/inc/CMQCBDL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBDL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCBDL ${MQ_INSTALLATION_PATH}/inc/CMQCBDL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBDL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCBDL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCHRVV to ${MQ_INSTALLATION_PATH}/inc/CMQCHRVV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCHRVV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCHRVV ${MQ_INSTALLATION_PATH}/inc/CMQCHRVV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCHRVV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCHRVV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCHRVL to ${MQ_INSTALLATION_PATH}/inc/CMQCHRVL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCHRVL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCHRVL ${MQ_INSTALLATION_PATH}/inc/CMQCHRVL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCHRVL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCHRVL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCMHOV to ${MQ_INSTALLATION_PATH}/inc/CMQCMHOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCMHOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCMHOV ${MQ_INSTALLATION_PATH}/inc/CMQCMHOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCMHOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCMHOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCMHOL to ${MQ_INSTALLATION_PATH}/inc/CMQCMHOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCMHOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCMHOL ${MQ_INSTALLATION_PATH}/inc/CMQCMHOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCMHOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCMHOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCTLOV to ${MQ_INSTALLATION_PATH}/inc/CMQCTLOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCTLOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCTLOV ${MQ_INSTALLATION_PATH}/inc/CMQCTLOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCTLOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCTLOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCTLOL to ${MQ_INSTALLATION_PATH}/inc/CMQCTLOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCTLOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQCTLOL ${MQ_INSTALLATION_PATH}/inc/CMQCTLOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCTLOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQCTLOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMHOV to ${MQ_INSTALLATION_PATH}/inc/CMQDMHOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMHOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMHOV ${MQ_INSTALLATION_PATH}/inc/CMQDMHOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMHOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMHOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMHOL to ${MQ_INSTALLATION_PATH}/inc/CMQDMHOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMHOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMHOL ${MQ_INSTALLATION_PATH}/inc/CMQDMHOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMHOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMHOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMPOV to ${MQ_INSTALLATION_PATH}/inc/CMQDMPOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMPOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMPOV ${MQ_INSTALLATION_PATH}/inc/CMQDMPOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMPOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMPOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMPOL to ${MQ_INSTALLATION_PATH}/inc/CMQDMPOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMPOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQDMPOL ${MQ_INSTALLATION_PATH}/inc/CMQDMPOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMPOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQDMPOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIMPOV to ${MQ_INSTALLATION_PATH}/inc/CMQIMPOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIMPOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIMPOV ${MQ_INSTALLATION_PATH}/inc/CMQIMPOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIMPOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIMPOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIMPOL to ${MQ_INSTALLATION_PATH}/inc/CMQIMPOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIMPOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQIMPOL ${MQ_INSTALLATION_PATH}/inc/CMQIMPOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIMPOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQIMPOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMHBOV to ${MQ_INSTALLATION_PATH}/inc/CMQMHBOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMHBOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMHBOV ${MQ_INSTALLATION_PATH}/inc/CMQMHBOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMHBOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMHBOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMHBOL to ${MQ_INSTALLATION_PATH}/inc/CMQMHBOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMHBOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQMHBOL ${MQ_INSTALLATION_PATH}/inc/CMQMHBOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMHBOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQMHBOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPDV to ${MQ_INSTALLATION_PATH}/inc/CMQPDV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPDV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPDV ${MQ_INSTALLATION_PATH}/inc/CMQPDV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPDV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPDV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPDL to ${MQ_INSTALLATION_PATH}/inc/CMQPDL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPDL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQPDL ${MQ_INSTALLATION_PATH}/inc/CMQPDL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPDL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQPDL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSMPOV to ${MQ_INSTALLATION_PATH}/inc/CMQSMPOV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSMPOV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSMPOV ${MQ_INSTALLATION_PATH}/inc/CMQSMPOV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSMPOV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSMPOV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSMPOL to ${MQ_INSTALLATION_PATH}/inc/CMQSMPOL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSMPOL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSMPOL ${MQ_INSTALLATION_PATH}/inc/CMQSMPOL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSMPOL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSMPOL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSROV to ${MQ_INSTALLATION_PATH}/inc/CMQSROV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSROV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSROV ${MQ_INSTALLATION_PATH}/inc/CMQSROV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSROV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSROV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSROL to ${MQ_INSTALLATION_PATH}/inc/CMQSROL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSROL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSROL ${MQ_INSTALLATION_PATH}/inc/CMQSROL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSROL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSROL
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSTSV to ${MQ_INSTALLATION_PATH}/inc/CMQSTSV
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSTSV
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSTSV ${MQ_INSTALLATION_PATH}/inc/CMQSTSV
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSTSV
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSTSV
# Linking ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSTSL to ${MQ_INSTALLATION_PATH}/inc/CMQSTSL
if [ ! -d ${MQ_INSTALLATION_PATH}/inc ]
then
    mkdir -p ${MQ_INSTALLATION_PATH}/inc
else
    rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSTSL
fi
ln -s ${MQ_INSTALLATION_PATH}/inc/cobcpy32/CMQSTSL ${MQ_INSTALLATION_PATH}/inc/CMQSTSL
chown -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSTSL
chgrp -fh mqm ${MQ_INSTALLATION_PATH}/inc/CMQSTSL

%preun
RPM_PACKAGE_SUMMARY="IBM MQ SDK FileSet"
RPM_PACKAGE_NAME="MQSeriesSDK"
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
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCIHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCIHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCNOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCNOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDLHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDLHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQGMOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQGMOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIEPL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIEPV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIIHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIIHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDEL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDEV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMDV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD1L
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD1V
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQODL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQODV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQORL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQORV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPMOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPMOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRMHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRMHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRRL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRRV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTMC2L
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTMC2V
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTML
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQTMV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQWIHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQWIHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQXQHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQXQHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCDL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCDV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQXV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFILL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFILV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFINL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFINV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSLL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSLV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSTL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSTV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPSV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFH2L
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQRFH2V
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQEPHV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBSV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFGRV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSFV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXNV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXLV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFIFV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD2V
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCSPV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBSL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFGRL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQEPHL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFSFL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXNL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFXLL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFIFL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMD2L
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCSPL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBFL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCFBFV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQAIRV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQAIRL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSCOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSCOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSDV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSDL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBMHOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQBMHOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBCV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBCL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBDV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCBDL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCHRVV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCHRVL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCMHOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCMHOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCTLOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQCTLOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMHOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMHOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMPOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQDMPOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIMPOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQIMPOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMHBOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQMHBOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPDV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQPDL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSMPOV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSMPOL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSROV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSROL
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSTSV
rm -f ${MQ_INSTALLATION_PATH}/inc/CMQSTSL

%postun
RPM_PACKAGE_SUMMARY="IBM MQ SDK FileSet"
RPM_PACKAGE_NAME="MQSeriesSDK"
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

