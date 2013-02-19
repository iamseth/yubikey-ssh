Name:           yubikey-ssh
Version:        0.1
Release:	1
BuildArch:	noarch
Source:		%{name}.tgz
Summary:        Code to provide 2 factor support to SSH
Group:		System Environment/Libraries
License:        Whatever you want
URL:            https://github.com/migrantgeek/yubikey-ssh

%description
Code to provide 2 factor support to SSH

%install
mkdir -p $RPM_BUILD_ROOT/etc/
mkdir -p $RPM_BUILD_ROOT/usr/sbin
tar xzf %{_topdir}/SOURCES/%{name}.tgz -C $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/sbin/yubikey-ssh.py
%attr(644, root, root) /etc/yubikey.conf

%changelog
* Mon Feb 18 2013 Seth Miller <seth@migrantgeek.com>
- Initial release
