yubikey-ssh
===========

#Installation

* Install the RPM
* 
  rpm -ivh http://migrantgeek-yum.s3.amazonaws.com/rhel/6/noarch/yubikey-ssh-0.1-1.noarch.rpm

* Add following line to SSH

  ForceCommand /usr/sbin/yubikey-ssh.py
  

