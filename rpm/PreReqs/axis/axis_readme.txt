axis.jar installation instructions
==================================

Please refer to the "IBM MQ Transport for SOAP" book for information
regarding the axis.jar file.  Installation instructions are provided below.


To install the axis.jar file, follow the appropriate instructions for your
platform:

AIX
---
Copy the file axis.jar from the install media's directory "PreReqs/axis" to
the "java/lib/soap" sub-directory of the location you installed IBM MQ
into e.g. "/usr/mqm/java/lib/soap".

The file's ownership should then be changed to be owned by the mqm user and
group id.  The files mode should be set to 444.

This can be achieved with the following commands (the commands
assume the user's current working directory is the root of the install media,
and that the user is currently logged in as the system root user):

cp -f PreReqs/axis/axis.jar /usr/mqm/java/lib/soap/axis.jar
chown mqm:mqm /usr/mqm/java/lib/soap/axis.jar
chmod 444 /usr/mqm/java/lib/soap/axis.jar


HP-UX, Solaris, Linux (x86, Power or zSeries platforms)
-------------------------------------------------------
Copy the file axis.jar from the install media's directory "PreReqs/axis" to
the "java/lib/soap" sub-directory of the location you installed IBM MQ
into e.g "/opt/mqm/java/lib/soap".

The file's ownership should then be changed to be owned by the mqm user and
group id.  The files mode should be set to 444.

This can be achieved with the following commands (the commands
assume the user's current working directory is the root of the install media,
and that the user is currently logged in as the system root user):

cp -f PreReqs/axis/axis.jar /opt/mqm/java/lib/soap/axis.jar
chown mqm:mqm /opt/mqm/java/lib/soap/axis.jar
chmod 444 /opt/mqm/java/lib/soap/axis.jar


Windows
-------
Copy the file axis.jar from the install media's directory "PreReqs/axis" to
the "java\lib\soap" sub-directory of the location you installed IBM MQ
into e.g. "C:\Program Files\IBM\IBM MQ\java\lib\soap".

