%define _name Tribler

%global gitdate 20180629
%global commit0 f133147a4af593b511acc846780449f78026aecf
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}


Name: tribler
Summary: Privacy enhanced BitTorrent client with P2P content discovery
Version: 7.1.0exp3
Release: 1%{?dist}
License: MIT
Group: Productivity/Networking/Other
URL: http://www.tribler.org/
Source0: https://github.com/Tribler/tribler/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: tribler
#Patch1: https://raw.githubusercontent.com/UnitedRPMs/tribler/master/setup.py.patch
BuildRequires: python-devel
BuildRequires: python-setuptools
BuildRequires: git
Requires: openssl-freeworld
Requires: swig
Requires: wxPython
Requires: m2crypto
Requires: vlc
Requires: python-apsw
Requires: libsodium
Requires: python-cryptography
Requires: python-plyvel
Requires: scons
Requires: python-netifaces
Requires: python-igraph
Requires: python-pyasn1
Requires: gmpy
Requires: rb_libtorrent-python
Requires: python-twisted
Requires: python-cherrypy
Requires: python-configobj
Requires: python-libnacl
Requires: python-decorator
Requires: python-qt5
Requires: python2-libnacl
Requires: python-matplotlib
Requires: python2-matplotlib-qt5
Requires: python-feedparser
Requires: python2-psutil
Requires: python2-meliae

BuildArch: noarch

%description
Tribler is an application that enables its users to find,
enjoy and share content. With content we mean video,
audio, pictures, and much more.
Tribler has three goals in helping you, the user:
1. Find content
2. Consume content
3. Share content

%prep
%autosetup -n %{name}-%{commit0}
#patch1 -p1
# Our trick; the tarball doesn't download completely the source; tribler needs some some sub-modules
pushd Tribler/
rm -rf dispersy/
git clone --depth=1 https://github.com/Tribler/dispersy.git
popd

pushd Tribler/dispersy
rm -rf libnacl/
git clone --depth=1 https://github.com/saltstack/libnacl.git
popd

pushd Tribler/Core/DecentralizedTracking/
rm -rf pymdht/
git clone --depth=1 https://github.com/Tribler/pymdht.git
popd

%build
python setup.py build

%install
# python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
python setup.py install --root=%{buildroot} --optimize=1

install -d %{buildroot}/usr/{bin,share/tribler}
cp -r Tribler %{buildroot}/usr/share/tribler
cp -r TriblerGUI %{buildroot}/usr/share/tribler
cp Tribler/schema_sdb_v*.sql %{buildroot}/usr/share/tribler/Tribler
install -d %{buildroot}/usr/share/{applications,pixmaps}
install -m644 Tribler/Main/Build/Ubuntu/tribler.desktop %{buildroot}/usr/share/applications
install -m644 Tribler/Main/Build/Ubuntu/tribler.xpm %{buildroot}/usr/share/pixmaps
install -m644 Tribler/Main/Build/Ubuntu/tribler_big.xpm %{buildroot}/usr/share/pixmaps
install -m755 debian/bin/tribler %{buildroot}/usr/bin
mv %{buildroot}/usr/bin/tribler %{buildroot}/usr/bin/tribler-gui
install -dm755 %{buildroot}/usr/bin/
install -m755 %{SOURCE1} %{buildroot}/usr/bin/
install -m644 logger.conf %{buildroot}/usr/share/tribler/
install -m644 run_tribler.py %{buildroot}/usr/share/tribler/
install -m644 check_os.py %{buildroot}/usr/share/tribler/
cp -r twisted %{buildroot}/usr/share/tribler

%files
%doc *.rst doc
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{python_sitelib}/%{_name}
%{python_sitelib}/libtribler-*.egg-info
%{python_sitelib}/TriblerGUI/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}_big.xpm
%{_datadir}/tribler/

%changelog
* Mon Jul 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.1.0exp3-1
- Update to 7.1.0exp3

* Sun May 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.0.2-4
- Relies on openssl-freeworld to add missing curve

* Sat May 05 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.0.2-3
- Add missing dependencies python2-psutil and python2-meliae
- Known issue : "AssertionError: Elliptic curve sect233k1 is not available on this system."

* Tue May 01 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.0.2-2
- Add missing check_os module installation

* Fri Apr 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.0.2-1
- Updated to 7.0.2

* Fri Feb 16 2018 David Vásquez <davidva AT tutanota DOT com> 7.0.1-1
- Updated to 7.0.1

* Wed May 17 2017 David Vásquez <davidva AT tutanota DOT com> 7.0.0-3.rc2
- Updated to 7.0.0-3.rc2

* Sun May 07 2017 David Vásquez <davidva AT tutanota DOT com> 7.0.0-2.rc1
- Updated to 7.0.0-2.rc1

* Thu Apr 20 2017 David Vásquez <davidva AT tutanota DOT com> 7.0.0-1.b
- Mitigation for openssl-full
- Updated to 7.0.0-1.b

* Wed Nov 30 2016 Pavlo Rudyi <paulcarroty at riseup.net> - 6.6.0-1.exp1.2
- Added openssl-full as depends

* Thu Aug 04 2016 Sérgio Basto <sergio@serjux.com> - 6.6.0-0.exp1.2
- build with libnacl

* Thu Aug 04 2016 Sérgio Basto <sergio@serjux.com> - 6.6.0-0.exp1.1
- with wxPython3 support

* Thu Jun 30 2016 Huaren Zhong <huaren.zhong@gmail.com> 6.5.2
- Rebuild for Fedora

* Fri Jan 08 2016 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.2.rc6
- Update localsnapshot

* Tue Dec 15 2015 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.rc6.2
- master

* Tue Dec 15 2015 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.rc6.1
- wx3_fixes

* Sat May 23 2015 Sérgio Basto <sergio@serjux.com> - 6.5-1
- Update to Tribler-v6.5.tar.xz pre-version

* Sat May 23 2015 Sérgio Basto <sergio@serjux.com> - 6.4.3-2
- Use released sources, fixes  Github's .zip archives don't contain the repo's
  submodules #1077

* Sat May 23 2015 Sérgio Basto <sergio@serjux.com> - 6.4.3-1
- Update 6.4.3 .
- add dist tag.
- update SOURCE0 url

* Mon Dec 22 2014 Huaren Zhong <huaren.zhong@gmail.com> - 6.4.0
- Rebuild for Fedora

* Sat Sep 06 2008 - Andrea Florio <andrea@links2linux.de>
- new package
