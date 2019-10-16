Name     : cni-plugins
Version  : 0.7.5
Release  : 8
URL      : https://github.com/containernetworking/plugins/
Source0  : https://github.com/containernetworking/plugins/archive/v0.7.5.tar.gz
Summary  : Container Network Interface
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT MPL-2.0-no-copyleft-exception

BuildRequires : go

# don't strip, these are not ordinary object files
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

%description
The CNI (Container Network Interface) project consists of
a specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number
of supported plugins.

%prep
%setup -q -n plugins-0.7.5

%build
./build.sh

%install
# these binaries are not supposed to be run by users
install -d  %{buildroot}/usr/libexec/cni
for f in $(ls ./bin); do
    install -p -m 0755 "./bin/${f}" %{buildroot}/usr/libexec/cni
done

%files
%defattr(-,root,root,-)
/usr/libexec/cni/bridge
/usr/libexec/cni/dhcp
/usr/libexec/cni/flannel
/usr/libexec/cni/host-device
/usr/libexec/cni/host-local
/usr/libexec/cni/ipvlan
/usr/libexec/cni/loopback
/usr/libexec/cni/macvlan
/usr/libexec/cni/portmap
/usr/libexec/cni/ptp
/usr/libexec/cni/tuning
/usr/libexec/cni/vlan
/usr/libexec/cni/sample