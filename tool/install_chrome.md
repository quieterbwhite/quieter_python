# Ubuntu 16.04 install chrome
> https://stackoverflow.com/questions/36825082/cannot-install-chrome-on-ubuntu-16-04  
Update the packages first in Ubuntu by below command.  
```
~$ sudo apt-get update
```
Install Required Dependices for Google Chrome as shown below.  
```
~$ sudo apt-get install libnss3-1d libxss1 libgconf2-4 libappindicator1 libindicator7
```
Download the Google Chrome command using below command.  
```
~$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```
still during installation if you get some error that some dependency is not installed run the below command and it will install all required dependencies.  
```
~$ sudo apt-get -f install
```
Now let's go ahead and install Google Chrome by below command.  
```
~$ sudo dpkg -i google-chrome-stable_current_amd64.deb
```
And its done....  
  
To open it just run below command command  
```
elinuxbook@ubuntu:~$ google-chrome
```
