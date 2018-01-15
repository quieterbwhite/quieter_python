# Install Maven On Ubuntu
> http://maven.apache.org/download.cgi   
> http://maven.apache.org/install.html  

Installing Apache Maven
The installation of Apache Maven is a simple process of extracting the archive and adding the bin folder with the mvn command to the PATH.

Detailed steps are:
```
Ensure JAVA_HOME environment variable is set and points to your JDK installation

Extract distribution archive in any directory

unzip apache-maven-3.5.0-bin.zip

or

tar xzvf apache-maven-3.5.0-bin.tar.gz

Alternatively use your preferred archive extraction tool.

Add the bin directory of the created directory apache-maven-3.5.0 to the PATH environment variable
```

Confirm with mvn -v in a new shell. The result should look similar to
```
Apache Maven 3.3.3 (7994120775791599e205a5524ec3e0dfe41d4a06; 2015-04-22T04:57:37-07:00)
Maven home: /opt/apache-maven-3.3.3
Java version: 1.8.0_45, vendor: Oracle Corporation
Java home: /Library/Java/JavaVirtualMachines/jdk1.8.0_45.jdk/Contents/Home/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "mac os x", version: "10.8.5", arch: "x86_64", family: "mac"
```
