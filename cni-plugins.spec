#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cni-plugins
Version  : 0.9.0
Release  : 20
URL      : https://github.com/containernetworking/plugins/archive/v0.9.0.tar.gz
Source0  : https://github.com/containernetworking/plugins/archive/v0.9.0.tar.gz
Source1  : 60-ip4-lxc-filter.conf
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT MPL-2.0
Requires: cni-plugins-config = %{version}-%{release}
Requires: cni-plugins-libexec = %{version}-%{release}
Requires: cni-plugins-license = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: build.patch

%description
This repository holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.

%package config
Summary: config components for the cni-plugins package.
Group: Default

%description config
config components for the cni-plugins package.


%package libexec
Summary: libexec components for the cni-plugins package.
Group: Default
Requires: cni-plugins-config = %{version}-%{release}
Requires: cni-plugins-license = %{version}-%{release}

%description libexec
libexec components for the cni-plugins package.


%package license
Summary: license components for the cni-plugins package.
Group: Default

%description license
license components for the cni-plugins package.


%prep
%setup -q -n plugins-0.9.0
cd %{_builddir}/plugins-0.9.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607642802
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  GOFLAGS="-buildmode=pie -v"


%install
export SOURCE_DATE_EPOCH=1607642802
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cni-plugins
cp %{_builddir}/plugins-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/plugins-0.9.0/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/plugins-0.9.0/vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/56b820712432e458f05f883566ca8cd85dcdaad5
cp %{_builddir}/plugins-0.9.0/vendor/github.com/alexflint/go-filemutex/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/2bcfd941d61a7c61e4cfc79353bbbb3109b4165c
cp %{_builddir}/plugins-0.9.0/vendor/github.com/buger/jsonparser/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/c58c331bb2225ba2c11040abafd1f41e11476661
cp %{_builddir}/plugins-0.9.0/vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/plugins-0.9.0/vendor/github.com/coreos/go-iptables/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/plugins-0.9.0/vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/plugins-0.9.0/vendor/github.com/d2g/dhcp4/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/dfdb3a8b15d99543c4f00758e777ac16a30c49e9
cp %{_builddir}/plugins-0.9.0/vendor/github.com/d2g/dhcp4client/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/523489384296f403da31edf8edf6f9023d328517
cp %{_builddir}/plugins-0.9.0/vendor/github.com/d2g/dhcp4server/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/523489384296f403da31edf8edf6f9023d328517
cp %{_builddir}/plugins-0.9.0/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
cp %{_builddir}/plugins-0.9.0/vendor/github.com/godbus/dbus/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/994658c265db5dbf456fa6163905cc9c0b3bda46
cp %{_builddir}/plugins-0.9.0/vendor/github.com/j-keck/arping/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/16e0a1137e783866c7e6f927ab26be26a7fc769f
cp %{_builddir}/plugins-0.9.0/vendor/github.com/mattn/go-shellwords/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/f7f33fde14de785a3ac53f250bb746ba30844639
cp %{_builddir}/plugins-0.9.0/vendor/github.com/nxadm/tail/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/a792f3e236631b46c9ea1a9f86ab3a6c24b17c89
cp %{_builddir}/plugins-0.9.0/vendor/github.com/nxadm/tail/ratelimiter/Licence %{buildroot}/usr/share/package-licenses/cni-plugins/15e225f105ead05a4d06cdf7723bb6ec11e92304
cp %{_builddir}/plugins-0.9.0/vendor/github.com/onsi/ginkgo/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
cp %{_builddir}/plugins-0.9.0/vendor/github.com/onsi/ginkgo/reporters/stenographer/support/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/plugins-0.9.0/vendor/github.com/onsi/ginkgo/reporters/stenographer/support/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/5b53018d7f0706e49275a92d36b54cfbfbb71367
cp %{_builddir}/plugins-0.9.0/vendor/github.com/onsi/gomega/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
cp %{_builddir}/plugins-0.9.0/vendor/github.com/safchain/ethtool/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/plugins-0.9.0/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/plugins-0.9.0/vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/plugins-0.9.0/vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/plugins-0.9.0/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/plugins-0.9.0/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/plugins-0.9.0/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/plugins-0.9.0/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/plugins-0.9.0/vendor/golang.org/x/xerrors/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
cp %{_builddir}/plugins-0.9.0/vendor/gopkg.in/tomb.v1/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/178b27feb961b28990b377da59e9d43d868a0a6f
cp %{_builddir}/plugins-0.9.0/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/cni-plugins/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/plugins-0.9.0/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/cni-plugins/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/plugins-0.9.0/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/cni-plugins/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
%make_install
mkdir -p %{buildroot}/usr/lib/sysctl.d
install  %{_sourcedir}/60-ip4-lxc-filter.conf %{buildroot}/usr/lib/sysctl.d/60-ip4-lxc-filter.conf

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/sysctl.d/60-ip4-lxc-filter.conf

%files libexec
%defattr(-,root,root,-)
/usr/libexec/cni/bandwidth
/usr/libexec/cni/bridge
/usr/libexec/cni/dhcp
/usr/libexec/cni/firewall
/usr/libexec/cni/flannel
/usr/libexec/cni/host-device
/usr/libexec/cni/host-local
/usr/libexec/cni/ipvlan
/usr/libexec/cni/loopback
/usr/libexec/cni/macvlan
/usr/libexec/cni/portmap
/usr/libexec/cni/ptp
/usr/libexec/cni/sbr
/usr/libexec/cni/static
/usr/libexec/cni/tuning
/usr/libexec/cni/vlan
/usr/libexec/cni/vrf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cni-plugins/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/cni-plugins/15e225f105ead05a4d06cdf7723bb6ec11e92304
/usr/share/package-licenses/cni-plugins/16e0a1137e783866c7e6f927ab26be26a7fc769f
/usr/share/package-licenses/cni-plugins/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/cni-plugins/178b27feb961b28990b377da59e9d43d868a0a6f
/usr/share/package-licenses/cni-plugins/2bcfd941d61a7c61e4cfc79353bbbb3109b4165c
/usr/share/package-licenses/cni-plugins/523489384296f403da31edf8edf6f9023d328517
/usr/share/package-licenses/cni-plugins/56b820712432e458f05f883566ca8cd85dcdaad5
/usr/share/package-licenses/cni-plugins/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/cni-plugins/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/cni-plugins/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/cni-plugins/7b421b3d8f9fe9dc8158b5e6efed1c448605ba92
/usr/share/package-licenses/cni-plugins/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
/usr/share/package-licenses/cni-plugins/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/cni-plugins/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/cni-plugins/994658c265db5dbf456fa6163905cc9c0b3bda46
/usr/share/package-licenses/cni-plugins/9f1b6690bcfc732123ae209c90c62f2ba80dfcb0
/usr/share/package-licenses/cni-plugins/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/cni-plugins/a792f3e236631b46c9ea1a9f86ab3a6c24b17c89
/usr/share/package-licenses/cni-plugins/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/cni-plugins/c58c331bb2225ba2c11040abafd1f41e11476661
/usr/share/package-licenses/cni-plugins/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/cni-plugins/dfdb3a8b15d99543c4f00758e777ac16a30c49e9
/usr/share/package-licenses/cni-plugins/f7f33fde14de785a3ac53f250bb746ba30844639
/usr/share/package-licenses/cni-plugins/f88291c879c4ee329bfa341b54eaedd29d3058cf
