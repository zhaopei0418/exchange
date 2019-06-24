Summary: IBM MQ Managed File Transfer Base Component
Name: MQSeriesFTBase
Version: 9.0.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesRuntime = 9.0.0-0
Requires: MQSeriesJava = 9.0.0-0
Requires: MQSeriesJRE = 9.0.0-0
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
This package provides the common IBM MQ Managed File Transfer
functionality which is used by all the other Managed File Transfer components.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/mqft
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/lib
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/credentials
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/email
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/timeout
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/INSTALL $RPM_BUILD_ROOT/opt/mqm/mqft/ant/INSTALL
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/KEYS $RPM_BUILD_ROOT/opt/mqm/mqft/ant/KEYS
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/LICENSE $RPM_BUILD_ROOT/opt/mqm/mqft/ant/LICENSE
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/NOTICE $RPM_BUILD_ROOT/opt/mqm/mqft/ant/NOTICE
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/README $RPM_BUILD_ROOT/opt/mqm/mqft/ant/README
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/WHATSNEW $RPM_BUILD_ROOT/opt/mqm/mqft/ant/WHATSNEW
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/ant $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/ant.bat $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant.bat
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/ant.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/ant.cmd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antRun $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antRun.bat $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun.bat
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antRun.pl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antRun.pl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/antenv.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/antenv.cmd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/envset.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/envset.cmd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/lcp.bat $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/lcp.bat
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/runant.pl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runant.pl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/runant.py $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runant.py
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/bin/runrc.cmd $RPM_BUILD_ROOT/opt/mqm/mqft/ant/bin/runrc.cmd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/ant-bootstrap.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/ant-bootstrap.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/changelog.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/changelog.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/coverage-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/coverage-frames.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/jdepend-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/jdepend-frames.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/jdepend.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/jdepend.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/junit-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-frames.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/junit-noframes.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/junit-noframes.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/log.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/log.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/maudit-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/maudit-frames.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/etc/tagdiff.xsl $RPM_BUILD_ROOT/opt/mqm/mqft/ant/etc/tagdiff.xsl
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/fetch.xml $RPM_BUILD_ROOT/opt/mqm/mqft/ant/fetch.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/get-m2.xml $RPM_BUILD_ROOT/opt/mqm/mqft/ant/get-m2.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/README $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/README
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-antlr.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-antlr.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-antlr.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-antlr.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-oro.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-oro.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-oro.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-oro.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-logging.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-logging.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-logging.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-logging.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-net.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-net.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-commons-net.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-commons-net.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jai.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jai.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jai.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jai.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-javamail.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-javamail.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-javamail.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-javamail.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jdepend.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jdepend.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jdepend.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jdepend.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jmf.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jmf.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jmf.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jmf.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jsch.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jsch.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-jsch.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-jsch.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit4.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit4.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-junit4.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-junit4.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-launcher.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-launcher.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-launcher.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-launcher.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-netrexx.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-netrexx.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-netrexx.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-netrexx.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-parent.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-parent.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-swing.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-swing.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-swing.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-swing.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-testutil.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-testutil.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant-testutil.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant-testutil.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant.jar $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/ant.pom $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/ant.pom
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/ant/lib/libraries.properties $RPM_BUILD_ROOT/opt/mqm/mqft/ant/lib/libraries.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/logging.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/logging.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVElements.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVElements.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGNVMessages.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGNVMessages.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCElements.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCElements.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/messages/BFGPCMessages.properties $RPM_BUILD_ROOT/opt/mqm/mqft/lib/messages/BFGPCMessages.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib64/libmqmft.so $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/libmqmft.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-beanutils.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-beanutils.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-digester-1.8.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-digester-1.8.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-io-1.4.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-io-1.4.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-lang-2.4.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-lang-2.4.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-logging-1.1.1.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-logging-1.1.1.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/commons-net-3.3.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/commons-net-3.3.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/icu4j-56_1.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-56_1.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/icu4j-charset-56_1.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-charset-56_1.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib/icu4j-localespi-56_1.jar $RPM_BUILD_ROOT/opt/mqm/mqft/lib/icu4j-localespi-56_1.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib64/libmqmftpc.so $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/libmqmftpc.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/lib64/mqmftpc $RPM_BUILD_ROOT/opt/mqm/mqft/lib64/mqmftpc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/email/email.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/email/email.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/timeout/timeout.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/timeout/timeout.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/zip/zip.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip/zip.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml $RPM_BUILD_ROOT/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/basic.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/basic.zip
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/custom1.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/custom1.zip
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/custom2.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/custom2.zip
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/4690/SSL.zip $RPM_BUILD_ROOT/opt/mqm/mqft/samples/4690/SSL.zip
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Trace.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Trace.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/FileTransfer.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/FileTransfer.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Filespace.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Filespace.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Internal.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Internal.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Log.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Log.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Monitor.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Monitor.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/MonitorList.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MonitorList.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/MonitorLog.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MonitorLog.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Notification.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Notification.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/PingAgent.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/PingAgent.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/Reply.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/Reply.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ScheduleList.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ScheduleList.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/ScheduleLog.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/ScheduleLog.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/TransferLog.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/TransferLog.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/TransferStatus.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/TransferStatus.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/UserInfo.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/UserInfo.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/UserSandboxes.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/UserSandboxes.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/fteutils.xjb $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/fteutils.xjb
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/fteutils.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/fteutils.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd $RPM_BUILD_ROOT/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteChangeDefaultConfigurationOptions $RPM_BUILD_ROOT/opt/mqm/bin/fteChangeDefaultConfigurationOptions
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteCommon $RPM_BUILD_ROOT/opt/mqm/bin/fteCommon
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteDisplayVersion $RPM_BUILD_ROOT/opt/mqm/bin/fteDisplayVersion
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteMigrateConfigurationOptions $RPM_BUILD_ROOT/opt/mqm/bin/fteMigrateConfigurationOptions
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteObfuscate $RPM_BUILD_ROOT/opt/mqm/bin/fteObfuscate
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/ftePlatform $RPM_BUILD_ROOT/opt/mqm/bin/ftePlatform
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteSetupCommands $RPM_BUILD_ROOT/opt/mqm/bin/fteSetupCommands
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteSetupCoordination $RPM_BUILD_ROOT/opt/mqm/bin/fteSetupCoordination
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteListAgents $RPM_BUILD_ROOT/opt/mqm/bin/fteListAgents
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteShowAgentDetails $RPM_BUILD_ROOT/opt/mqm/bin/fteShowAgentDetails

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,bin,bin) "/opt/mqm/mqft"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/bin"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/etc"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/ant/lib"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/lib"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/lib/messages"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/lib64"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/credentials"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/email"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/hub"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/timeout"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/fteant/zip"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/4690"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/schema"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Base-9.0.0.mqtag"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/INSTALL"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/KEYS"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/LICENSE"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/NOTICE"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/README"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/WHATSNEW"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/ant"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/ant.bat"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/ant.cmd"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antRun"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antRun.bat"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antRun.pl"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/antenv.cmd"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/complete-ant-cmd.pl"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/envset.cmd"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/lcp.bat"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/runant.pl"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/runant.py"
%attr(555,bin,bin) "/opt/mqm/mqft/ant/bin/runrc.cmd"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/ant-bootstrap.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/changelog.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-text.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/checkstyle/checkstyle-xdoc.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/coverage-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/jdepend-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/jdepend.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/junit-frames-xalan1.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/junit-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/junit-noframes.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/log.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/maudit-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/mmetrics-frames.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/etc/tagdiff.xsl"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/fetch.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/get-m2.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/README"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-antlr.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-antlr.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bcel.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bcel.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bsf.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-bsf.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-log4j.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-log4j.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-oro.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-oro.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-regexp.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-regexp.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-resolver.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-resolver.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-xalan2.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-apache-xalan2.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-logging.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-logging.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-net.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-commons-net.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jai.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jai.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-javamail.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-javamail.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jdepend.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jdepend.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jmf.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jmf.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jsch.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-jsch.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit4.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-junit4.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-launcher.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-launcher.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-netrexx.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-netrexx.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-parent.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-swing.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-swing.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-testutil.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant-testutil.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/ant.pom"
%attr(444,bin,bin) "/opt/mqm/mqft/ant/lib/libraries.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.ant.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.bootstrap.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.cmdline.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.common.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.daemon.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.databaselogger.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.exitroutines.api.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/com.ibm.wmqfte.native.jni.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/logging.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVElements.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGNVMessages.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCElements.properties"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/messages/BFGPCMessages.properties"
%attr(555,bin,bin) %verify(not md5 mtime) "/opt/mqm/mqft/lib64/libmqmft.so"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-beanutils.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-digester-1.8.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-io-1.4.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-lang-2.4.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-logging-1.1.1.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/commons-net-3.3.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/icu4j-56_1.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/icu4j-charset-56_1.jar"
%attr(444,bin,bin) "/opt/mqm/mqft/lib/icu4j-localespi-56_1.jar"
%attr(555,bin,bin) %verify(not md5 mtime) "/opt/mqm/mqft/lib64/libmqmftpc.so"
%attr(555,bin,bin) %verify(not md5 mtime) "/opt/mqm/mqft/lib64/mqmftpc"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/credentials/MQMFTCredentials.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/email/email.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/hub/hubcopy.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/hub/hubprocess.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/timeout/timeout.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/zip/zip.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/fteant/zip/zipfiles.xml"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/basic.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/custom1.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/custom2.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/4690/SSL.zip"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Trace.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/AgentTraceStatus.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ConnectDirectCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ConnectDirectNodeProperties.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ConnectDirectProcessDefinitions.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/FileLoggerFormat.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/FileSpaceInfo.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/FileTransfer.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Filespace.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Internal.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Log.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Monitor.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/MonitorList.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/MonitorLog.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/MQMFTCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Notification.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/PingAgent.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ProtocolBridgeCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ProtocolBridgeProperties.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/Reply.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ScheduleList.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/ScheduleLog.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/TransferLog.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/TransferStatus.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/UserInfo.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/UserSandboxes.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/fteutils.xjb"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/fteutils.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ConnectDirectNodeProperties.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeCredentials.xsd"
%attr(444,bin,bin) "/opt/mqm/mqft/samples/schema/7.0.4/ProtocolBridgeProperties.xsd"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteChangeDefaultConfigurationOptions"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteCommon"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteDisplayVersion"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteMigrateConfigurationOptions"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteObfuscate"
%attr(555,mqm,mqm) "/opt/mqm/bin/ftePlatform"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteSetupCommands"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteSetupCoordination"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteListAgents"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteShowAgentDetails"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Base Component"
RPM_PACKAGE_NAME="MQSeriesFTBase"
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

