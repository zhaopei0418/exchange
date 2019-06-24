Summary: IBM MQ Java, JMS and Web Services support
Name: MQSeriesJava
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
This package provides the IBM MQ classes for Java and JMS application
programming interfaces, as well as Java Web Services support.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/java
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib64
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/jca
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi
install -d $RPM_BUILD_ROOT/opt/mqm/java/bin
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/jmscc
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/java/lib/soap
install -d $RPM_BUILD_ROOT/opt/mqm/java/http
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi
install -d $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/libmqjexitstub02.so $RPM_BUILD_ROOT/opt/mqm/java/lib/libmqjexitstub02.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib64/libmqjexitstub02.so $RPM_BUILD_ROOT/opt/mqm/java/lib64/libmqjexitstub02.so
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/bcprov-jdk15on-152.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/bcprov-jdk15on-152.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/bcpkix-jdk15on-152.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/bcpkix-jdk15on-152.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.headers.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.headers.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.pcf.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.pcf.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.jmqi.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jmqi.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mqjms.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mqjms.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.traceControl.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.traceControl.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.allclient.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.allclient.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/fscontext.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/fscontext.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/providerutil.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/providerutil.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jms.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/jms.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jca/wmq.jmsra.rar $RPM_BUILD_ROOT/opt/mqm/java/lib/jca/wmq.jmsra.rar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.0.0.0.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.0.0.0.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/IVTRun $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTRun
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/IVTSetup $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTSetup
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/IVTTidy $RPM_BUILD_ROOT/opt/mqm/java/bin/IVTTidy
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/JMSAdmin $RPM_BUILD_ROOT/opt/mqm/java/bin/JMSAdmin
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/PSIVTRun $RPM_BUILD_ROOT/opt/mqm/java/bin/PSIVTRun
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/Cleanup $RPM_BUILD_ROOT/opt/mqm/java/bin/Cleanup
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/runjms $RPM_BUILD_ROOT/opt/mqm/java/bin/runjms
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/setjmsenv $RPM_BUILD_ROOT/opt/mqm/java/bin/setjmsenv
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/setjmsenv64 $RPM_BUILD_ROOT/opt/mqm/java/bin/setjmsenv64
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/MQJMS_PSQ.mqsc $RPM_BUILD_ROOT/opt/mqm/java/bin/MQJMS_PSQ.mqsc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/JMSAdmin.config $RPM_BUILD_ROOT/opt/mqm/java/bin/JMSAdmin.config
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/jms.config $RPM_BUILD_ROOT/opt/mqm/java/bin/jms.config
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/formatLog $RPM_BUILD_ROOT/opt/mqm/java/bin/formatLog
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/bin/PSReportDump.class $RPM_BUILD_ROOT/opt/mqm/java/bin/PSReportDump.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.axis2.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.axis2.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.soap.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.soap.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/com.ibm.mq.jms.Nojndi.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/com.ibm.mq.jms.Nojndi.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/soap/wsdl4j-1.5.1.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/soap/wsdl4j-1.5.1.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/soap/jaxrpc.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/soap/jaxrpc.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/soap/servlet.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/soap/servlet.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/soap/commons-discovery-0.2.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/soap/commons-discovery-0.2.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/soap/commons-logging-1.0.4.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/soap/commons-logging-1.0.4.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/lib/soap/saaj.jar $RPM_BUILD_ROOT/opt/mqm/java/lib/soap/saaj.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwclientTransport.wsdd $RPM_BUILD_ROOT/opt/mqm/bin/amqwclientTransport.wsdd
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwclientConfig.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqwclientConfig.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwdeployWMQService.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqwdeployWMQService.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwCleanSideQueue.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqwCleanSideQueue.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwsetcp.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqwsetcp.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/amqwstartwin.sh $RPM_BUILD_ROOT/opt/mqm/bin/amqwstartwin.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/http/WMQHTTP.war $RPM_BUILD_ROOT/opt/mqm/java/http/WMQHTTP.war
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/package-list $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/package-list
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/constant-values.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/constant-values.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/index-all.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/index-all.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/index.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/index.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/help-doc.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/help-doc.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/script.js $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/script.js
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/package-list $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/package-list
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/constant-values.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/constant-values.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/index-all.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/index-all.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/index.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/index.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/help-doc.html $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/help-doc.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/java/doc/WMQJavaClasses/script.js $RPM_BUILD_ROOT/opt/mqm/java/doc/WMQJavaClasses/script.js

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/java"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib64"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/jca"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/OSGi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/jmscc"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/lib/soap"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/http"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi"
%dir %attr(555,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Java_Messaging-9.0.0.mqtag"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib/libmqjexitstub02.so"
%attr(555,mqm,mqm) %verify(not md5 mtime) "/opt/mqm/java/lib64/libmqjexitstub02.so"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/bcprov-jdk15on-152.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/bcpkix-jdk15on-152.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.headers.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.pcf.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.jmqi.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mqjms.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.traceControl.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.allclient.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/fscontext.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/providerutil.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jms.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jca/wmq.jmsra.ivt.ear"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jca/wmq.jmsra.rar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.java_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclient_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.mq.osgi.allclientprereqs_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.commonservices.j2se_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms.prereq_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.jms_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.nls_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.nls_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq.prereq_9.0.0.0.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/OSGi/com.ibm.msg.client.osgi.wmq_9.0.0.0.jar"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/IVTRun"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/IVTSetup"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/IVTTidy"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/JMSAdmin"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/PSIVTRun"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/Cleanup"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/runjms"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/setjmsenv"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/setjmsenv64"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/MQJMS_PSQ.mqsc"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/JMSAdmin.config"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/jms.config"
%attr(555,mqm,mqm) "/opt/mqm/java/bin/formatLog"
%attr(444,mqm,mqm) "/opt/mqm/java/bin/PSReportDump.class"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.axis2.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/jmscc/com.ibm.msg.client.commonservices.wmq.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.soap.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/com.ibm.mq.jms.Nojndi.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/soap/wsdl4j-1.5.1.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/soap/jaxrpc.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/soap/servlet.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/soap/commons-discovery-0.2.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/soap/commons-logging-1.0.4.jar"
%attr(444,mqm,mqm) "/opt/mqm/java/lib/soap/saaj.jar"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwclientTransport.wsdd"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwclientConfig.sh"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwdeployWMQService.sh"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwCleanSideQueue.sh"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwsetcp.sh"
%attr(555,mqm,mqm) "/opt/mqm/bin/amqwstartwin.sh"
%attr(444,mqm,mqm) "/opt/mqm/java/http/WMQHTTP.war"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCSP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/MQCXP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/WMQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/exits/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/JmqiException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jmqi/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/BrokerCommandFailedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/Cleanup.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldNameException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/FieldTypeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/IntErrorException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/ISSLException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSInvalidParameterException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSListenerSetException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSMessageQueueOverflowException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotActiveException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSNotSupportedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/JMSParameterIsNullException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionFactory.ConnectionFactoryProperty.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQConnectionMetaData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSAbstractIVT.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQJMSLevel.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQMessageProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueBrowser.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueEnumeration.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueReceiver.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSender.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQRoot.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTemporaryTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicPublisher.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQTopicSubscriber.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXAQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXASession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/MQXATopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/NoBrokerResponseException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SessionClosedException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/SyntaxException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/MQException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/QmgrSplCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/constants/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/mq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedIllegalStateRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidClientIDRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidDestinationRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedInvalidSelectorRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedJMSSecurityRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageEOFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageFormatRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotReadableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedMessageNotWriteableRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedResourceAllocationRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionInProgressRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/DetailedTransactionRolledBackRuntimeException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsCapabilityContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConnectionMetaData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsConvertableException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsExceptionDetail.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsFactoryFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageConsumer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsMessageProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsProducer.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsPropertyContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueBrowser.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueReceiver.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSender.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsReadablePropertyContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTemporaryTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicPublisher.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsTopicSubscriber.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXAQueueSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXASession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnection.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicConnectionFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/JmsXATopicSession.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Trace.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/Version.Component.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/services/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/CommonConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/common/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/WMQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/msg/client/wmq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSBytesMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMapMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSObjectMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSStreamMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/JMSTextMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/com/ibm/jms/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/package-list"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/overview-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/constant-values.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/serialized-form.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/overview-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/index-all.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/deprecated-list.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/allclasses-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/allclasses-noframe.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/index.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/overview-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/help-doc.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/stylesheet.css"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/script.js"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJMSClasses/errorcodes.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFBS.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFGR.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIL64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFIN64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFSL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/MQCFST.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFContent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFFilterParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeader.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFHeaderFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFMessageAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/PCFParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/pcf/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCSP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/MQCXP.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/WMQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/exits/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CCSID.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFBS.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFGR.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIL64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFIN64.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSF.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFSL.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQCFST.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/MQEPH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFContent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFFilterParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeader.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFHeaderFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFMessageAgentResponseTracker.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/PCFParameter.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/pcf/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CCSID.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/Charsets.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQChainable.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQCIH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQData.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDataException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQDLH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeader.Field.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderContext.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderFactory.Registry.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderIterator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderList.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQHeaderRegistry.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQIIH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMD1.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQMDE.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH.NameValuePair.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRFH2.Element.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQRMH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQSAPH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTM2.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQTMC2.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQWIH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/MQXQH.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/headers/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/JmqiException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/jmqi/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/JmqiSESSION.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQAsyncStatus.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelDefinition.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQChannelExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQConnectionSecurityParameters.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDestination.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionList.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQDistributionListItem.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQEnvironment.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQException.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExitChain.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQExternalUserExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQGetMessageOptions.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaComponent.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQJavaLevel.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQManagedObject.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQMessage.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQOD.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPoolToken.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQProcess.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPropertyDescriptor.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQPutMessageOptions.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueue.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQQueueManager.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQReceiveExitChain.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSecurityExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExit.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSendExitChain.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSimpleConnectionManager.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQSubscription.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/MQTopic.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQBC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQCFC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQPSC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQXC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/CMQZC.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.FieldValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQConstants.ValueValueComparator.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/MQPropertyIdentifiers.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/QmgrSplCapability.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/constants/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/com/ibm/mq/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/package-list"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/overview-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/constant-values.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/serialized-form.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/overview-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/index-all.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/deprecated-list.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/allclasses-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/allclasses-noframe.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/index.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/overview-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/help-doc.html"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/stylesheet.css"
%attr(444,mqm,mqm) "/opt/mqm/java/doc/WMQJavaClasses/script.js"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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
RPM_PACKAGE_SUMMARY="IBM MQ Java, JMS and Web Services support"
RPM_PACKAGE_NAME="MQSeriesJava"
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

