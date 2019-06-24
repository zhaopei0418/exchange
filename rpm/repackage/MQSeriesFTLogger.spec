Summary: IBM MQ Managed File Transfer Logger
Name: MQSeriesFTLogger
Version: 9.0.0
Release: 0
License: Commercial
ExclusiveArch: x86_64
Group: Applications/Networking
AutoReqProv: no
Vendor: IBM
Prefix: /opt/mqm
Requires: MQSeriesFTBase = 9.0.0-0
Requires: MQSeriesServer = 9.0.0-0
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
This package provides the IBM MQ Managed File Transfer Logger capability,
which provides the capability to log transfer audit related data to a database
or file.
%clean
rm -rf $RPM_BUILD_ROOT

%install
install -d $RPM_BUILD_ROOT/opt/mqm
install -d $RPM_BUILD_ROOT/opt/mqm/swidtag
install -d $RPM_BUILD_ROOT/opt/mqm/bin
install -d $RPM_BUILD_ROOT/opt/mqm/mqft
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/sql
install -d $RPM_BUILD_ROOT/opt/mqm/mqft/web
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Logger-9.0.0.mqtag $RPM_BUILD_ROOT/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Logger-9.0.0.mqtag
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2_701-702.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2_701-702.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2_702-703.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2_702-703.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2_703-704.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2_703-704.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2_704-750.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2_704-750.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2_750-7502.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2_750-7502.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_db2_7502-800.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_db2_7502-800.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle_701-702.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle_701-702.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle_702-703.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle_702-703.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle_703-704.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle_703-704.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle_704-750.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle_704-750.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle_750-7502.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle_750-7502.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_oracle_7502-800.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_oracle_7502-800.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_701-702.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_701-702.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_702-703.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_702-703.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_703-704.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_703-704.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_704-750.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_704-750.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_704-800.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_704-800.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_750-7502.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_750-7502.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_7502-800.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_7502-800.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_bigint.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_bigint.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/sql/ftelog_tables_zos_bigint_int-bigint.sql $RPM_BUILD_ROOT/opt/mqm/mqft/sql/ftelog_tables_zos_bigint_int-bigint.sql
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/web/com.ibm.wmqfte.databaselogger.jee.ear $RPM_BUILD_ROOT/opt/mqm/mqft/web/com.ibm.wmqfte.databaselogger.jee.ear
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/mqft/web/com.ibm.wmqfte.databaselogger.jee.oracle.ear $RPM_BUILD_ROOT/opt/mqm/mqft/web/com.ibm.wmqfte.databaselogger.jee.oracle.ear
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteCreateLogger $RPM_BUILD_ROOT/opt/mqm/bin/fteCreateLogger
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteDeleteLogger $RPM_BUILD_ROOT/opt/mqm/bin/fteDeleteLogger
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteMigrateLogger $RPM_BUILD_ROOT/opt/mqm/bin/fteMigrateLogger
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteSetLoggerTraceLevel $RPM_BUILD_ROOT/opt/mqm/bin/fteSetLoggerTraceLevel
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteShowLoggerDetails $RPM_BUILD_ROOT/opt/mqm/bin/fteShowLoggerDetails
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteStartLogger $RPM_BUILD_ROOT/opt/mqm/bin/fteStartLogger
install /build/slot2/p900_P/obj/amd64_linux_2/ship/opt/mqm/bin/fteStopLogger $RPM_BUILD_ROOT/opt/mqm/bin/fteStopLogger

%files
%dir %attr(555,mqm,mqm) "/opt/mqm"
%dir %attr(555,mqm,mqm) "/opt/mqm/swidtag"
%dir %attr(555,mqm,mqm) "/opt/mqm/bin"
%dir %attr(555,bin,bin) "/opt/mqm/mqft"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/sql"
%dir %attr(555,bin,bin) "/opt/mqm/mqft/web"
%attr(444,mqm,mqm) "/opt/mqm/swidtag/IBM_MQ_Managed_File_Transfer_Logger-9.0.0.mqtag"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2_701-702.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2_702-703.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2_703-704.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2_704-750.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2_750-7502.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_db2_7502-800.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle_701-702.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle_702-703.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle_703-704.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle_704-750.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle_750-7502.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_oracle_7502-800.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_701-702.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_702-703.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_703-704.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_704-750.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_704-800.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_750-7502.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_7502-800.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_bigint.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/sql/ftelog_tables_zos_bigint_int-bigint.sql"
%attr(444,bin,bin) "/opt/mqm/mqft/web/com.ibm.wmqfte.databaselogger.jee.ear"
%attr(444,bin,bin) "/opt/mqm/mqft/web/com.ibm.wmqfte.databaselogger.jee.oracle.ear"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteCreateLogger"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteDeleteLogger"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteMigrateLogger"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteSetLoggerTraceLevel"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteShowLoggerDetails"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteStartLogger"
%attr(555,mqm,mqm) "/opt/mqm/bin/fteStopLogger"

%pre
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Logger"
RPM_PACKAGE_NAME="MQSeriesFTLogger"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Logger"
RPM_PACKAGE_NAME="MQSeriesFTLogger"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Logger"
RPM_PACKAGE_NAME="MQSeriesFTLogger"
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
RPM_PACKAGE_SUMMARY="IBM MQ Managed File Transfer Logger"
RPM_PACKAGE_NAME="MQSeriesFTLogger"
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

