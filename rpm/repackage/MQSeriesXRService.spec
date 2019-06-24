Summary: IBM MQ Telemetry Service
Name: MQSeriesXRService
Version: 9.0.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesJava = 9.0.0-0
Requires: MQSeriesJRE = 9.0.0-0
Requires: MQSeriesServer = 9.0.0-0
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
This package adds support for the IBM MQ Telemetry Transport (MQTT)
protocol to a IBM MQ queue manager.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/bin
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/config
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/lib
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/samples
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/samples
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/scraper
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/class-use
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/resources
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols
install -d $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/src
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/bin/controlMQXRChannel.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/bin/controlMQXRChannel.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/bin/controlMQXR_mqm.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/bin/controlMQXR_mqm.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/bin/endMQXRService.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/bin/endMQXRService.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/bin/runMQXRService.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/bin/runMQXRService.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/config/jaas.config $RPM_BUILD_ROOT/opt/mqm/mqxr/config/jaas.config
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/config/java.properties $RPM_BUILD_ROOT/opt/mqm/mqxr/config/java.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/config/mqxr_unix.properties $RPM_BUILD_ROOT/opt/mqm/mqxr/config/mqxr_unix.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/config/mqxrtraceOn.properties $RPM_BUILD_ROOT/opt/mqm/mqxr/config/mqxrtraceOn.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/config/mqxrtraceOff.properties $RPM_BUILD_ROOT/opt/mqm/mqxr/config/mqxrtraceOff.properties
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/config/trace.config $RPM_BUILD_ROOT/opt/mqm/mqxr/config/trace.config
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/lib/MQXRListener.jar $RPM_BUILD_ROOT/opt/mqm/mqxr/lib/MQXRListener.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/lib/com.ibm.micro.xr.jar $RPM_BUILD_ROOT/opt/mqm/mqxr/lib/com.ibm.micro.xr.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/lib/com.ibm.mq.mqxr.utils.jar $RPM_BUILD_ROOT/opt/mqm/mqxr/lib/com.ibm.mq.mqxr.utils.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/lib/nonBlockingTrace.jar $RPM_BUILD_ROOT/opt/mqm/mqxr/lib/nonBlockingTrace.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/lib/objectManager.utils.jar $RPM_BUILD_ROOT/opt/mqm/mqxr/lib/objectManager.utils.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/CleanupMQM.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/CleanupMQM.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/samples/JAASLoginModule.java $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/samples/JAASLoginModule.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/samples/JAASPrincipal.java $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/samples/JAASPrincipal.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/SampleMQM.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/SampleMQM.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/installMQXRService_unix.mqsc $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/installMQXRService_unix.mqsc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/samples/JAASLoginModule.class $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/samples/JAASLoginModule.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/samples/JAASPrincipal.class $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/samples/JAASPrincipal.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/scraper/ScraperService\$Feed.class $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/scraper/ScraperService\$Feed.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/scraper/ScraperService.class $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/scraper/ScraperService.class
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/scraper/ScraperService.java $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/scraper/ScraperService.java
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/scraper/installScraperService_unix.mqsc $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/scraper/installScraperService_unix.mqsc
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/samples/scraper/runScraperService.sh $RPM_BUILD_ROOT/opt/mqm/mqxr/samples/scraper/runScraperService.sh
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/MQXR.jar $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/MQXR.jar
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/allclasses-frame.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/allclasses-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/allclasses-noframe.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/allclasses-noframe.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/script.js $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/script.js
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/AuthCallback.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/AuthCallback.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/class-use/AuthCallback.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/class-use/AuthCallback.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-frame.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-frame.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-summary.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-summary.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-tree.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-use.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-use.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/constant-values.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/constant-values.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/deprecated-list.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/deprecated-list.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/help-doc.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/help-doc.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/index-all.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/index-all.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/index.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/index.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/overview-tree.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/overview-tree.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/package-list $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/package-list
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/MQServer/javadoc/stylesheet.css $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/MQServer/javadoc/stylesheet.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/CommunityButton.gif $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/CommunityButton.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/EnterperiseMessagingButton.gif $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/EnterperiseMessagingButton.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/IBMMessagingBanner.gif $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/IBMMessagingBanner.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/Links.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/Links.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/PlayButton.gif $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/PlayButton.gif
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/References.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/References.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_CompleteWebPage.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_CompleteWebPage.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Connecting.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Connecting.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Diagnostics.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Diagnostics.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_HighAvailability.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_HighAvailability.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Messages.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Messages.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Start.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Start.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Subscribe.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Subscribe.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/WebMessagingUtility.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/WebMessagingUtility.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/files.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/files.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/index.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/index.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/mqttws31.js $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/mqttws31.js
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.Client.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.Client.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.Message.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.Message.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/_global_.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/_global_.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/src/mqttws31.js.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/src/mqttws31.js.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/WebSocket/tutorial.js $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/WebSocket/tutorial.js
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/core.js $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/core.js
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/index.html $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/index.html
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/mqttLogo.png $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/mqttLogo.png
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/structure.svg $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/structure.svg
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/style.css $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/style.css
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqxr/SDK/WebContent/websphere-brandmark.gif $RPM_BUILD_ROOT/opt/mqm/mqxr/SDK/WebContent/websphere-brandmark.gif

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(550,mqm,mqm) "/opt/mqm/mqxr/bin"
%dir %attr(550,mqm,mqm) "/opt/mqm/mqxr/config"
%dir %attr(550,mqm,mqm) "/opt/mqm/mqxr/lib"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/samples/samples"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/samples/scraper"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/class-use"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/resources"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols"
%dir %attr(555,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/src"
%attr(550,mqm,mqm) "/opt/mqm/mqxr/bin/controlMQXRChannel.sh"
%attr(550,mqm,mqm) "/opt/mqm/mqxr/bin/controlMQXR_mqm.sh"
%attr(550,mqm,mqm) "/opt/mqm/mqxr/bin/endMQXRService.sh"
%attr(550,mqm,mqm) "/opt/mqm/mqxr/bin/runMQXRService.sh"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/config/jaas.config"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/config/java.properties"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/config/mqxr_unix.properties"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/config/mqxrtraceOn.properties"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/config/mqxrtraceOff.properties"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/config/trace.config"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/lib/MQXRListener.jar"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/lib/com.ibm.micro.xr.jar"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/lib/com.ibm.mq.mqxr.utils.jar"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/lib/nonBlockingTrace.jar"
%attr(440,mqm,mqm) "/opt/mqm/mqxr/lib/objectManager.utils.jar"
%attr(555,mqm,mqm) "/opt/mqm/mqxr/samples/CleanupMQM.sh"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/samples/JAASLoginModule.java"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/samples/JAASPrincipal.java"
%attr(555,mqm,mqm) "/opt/mqm/mqxr/samples/SampleMQM.sh"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/installMQXRService_unix.mqsc"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/samples/JAASLoginModule.class"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/samples/JAASPrincipal.class"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/scraper/ScraperService$Feed.class"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/scraper/ScraperService.class"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/scraper/ScraperService.java"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/samples/scraper/installScraperService_unix.mqsc"
%attr(555,mqm,mqm) "/opt/mqm/mqxr/samples/scraper/runScraperService.sh"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/MQXR.jar"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/allclasses-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/allclasses-noframe.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/script.js"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/AuthCallback.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/class-use/AuthCallback.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-frame.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-summary.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/com/ibm/mq/mqxr/package-use.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/constant-values.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/deprecated-list.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/help-doc.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/index-all.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/index.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/overview-tree.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/package-list"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/MQServer/javadoc/stylesheet.css"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/CommunityButton.gif"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/EnterperiseMessagingButton.gif"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/IBMMessagingBanner.gif"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/Links.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/PlayButton.gif"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/References.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_CompleteWebPage.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Connecting.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Diagnostics.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_HighAvailability.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Messages.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Start.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/Tutorial31_Subscribe.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/WebMessagingUtility.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/files.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/index.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/mqttws31.js"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.Client.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.Message.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/Messaging.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/_global_.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/symbols/src/mqttws31.js.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/WebSocket/tutorial.js"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/core.js"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/index.html"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/mqttLogo.png"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/structure.svg"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/style.css"
%attr(444,mqm,mqm) "/opt/mqm/mqxr/SDK/WebContent/websphere-brandmark.gif"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Telemetry Service"
RPM_PACKAGE_NAME="MQSeriesXRService"
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

# @(#) MQMBID sn=p900-L160520.DE su=_6zq1EB58Eearh6Qyg9d9Dg pn=install/unix/linux_2/xrservice_preinstall.sh
# Pre-install script for the mqxr package
# This script checks whether xr701 is installed using the existence
# of a directory specific to that release to do so. The user must uninstall
# 7.0.1 before installing 7.1 in the same location if this is the default
# location.
#   <copyright 
#   notice="lm-source-program" 
#   pids="5724-H72," 
#   years="2010,2012" 
#   crc="608018138" > 
#   Licensed Materials - Property of IBM  
#    
#   5724-H72, 
#    
#   (C) Copyright IBM Corp. 2010, 2012 All Rights Reserved.  
#    
#   US Government Users Restricted Rights - Use, duplication or  
#   disclosure restricted by GSA ADP Schedule Contract with  
#   IBM Corp.  
#   </copyright> 
MQXR_ROOT=${MQ_INSTALLATION_PATH}/mqxr
if [ \( ${MQ_INSTALLATION_PATH} = ${MQ_DEFAULT_INSTALLATION_PATH} \) -a  \( -x ${MQXR_ROOT}/license \) ]
then
 echo "You appear to have WebSphere MQ Telemetry v.7.0.1 installed \
 at the following location: ${MQXR_ROOT}."
 echo "Please uninstall it before continuing with this installation."
 exit 1
fi
echo > /dev/null 2>/dev/null

%post
RPM_PACKAGE_SUMMARY="IBM MQ Telemetry Service"
RPM_PACKAGE_NAME="MQSeriesXRService"
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
RPM_PACKAGE_SUMMARY="IBM MQ Telemetry Service"
RPM_PACKAGE_NAME="MQSeriesXRService"
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
RPM_PACKAGE_SUMMARY="IBM MQ Telemetry Service"
RPM_PACKAGE_NAME="MQSeriesXRService"
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

