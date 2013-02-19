##Installation

- Install the RPM

  ```bash
  rpm -ivh http://migrantgeek-yum.s3.amazonaws.com/rhel/6/noarch/yubikey-ssh-0.1-1.noarch.rpm
  ```

- Add your API key to /etc/yubikey.conf  

- Add following line to SSH and restart

  ```bash
  echo "ForceCommand /usr/sbin/yubikey-ssh.py" >> /etc/ssh/sshd_config
  service sshd restart
  ```
  


