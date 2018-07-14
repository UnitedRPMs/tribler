%define _name Tribler

%global gitdate 20180702
%global commit0 22d2630fa28dcff9405e2be91e349ce08abf8a9e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0


Name: tribler
Summary: Privacy enhanced BitTorrent client with P2P content discovery
Version: 7.1.0
Release: 2.exp3%{?dist}
License: MIT
Group: Productivity/Networking/Other
URL: http://www.tribler.org/
Source0: https://github.com/Tribler/tribler/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: tribler
Source2: tribler-snapshot
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: git
Requires: openssl-freeworld
Requires: swig
Requires: python2-wxpython
#Requires: python-wxpython
Requires: m2crypto
Requires: vlc
Requires: python2-pillow
#Requires: python3-pillow
#Requires: python-apsw
Requires: python2-apsw
Requires: libsodium
#Requires: python-cryptography
Requires: python2-cryptography
#Requires: python-plyvel
Requires: python2-plyvel
Requires: scons
#Requires: python-netifaces
Requires: python2-netifaces
#Requires: python-igraph
Requires: python2-igraph
#Requires: python-pyasn1
Requires: python2-pyasn1
Requires: gmpy
#Requires: rb_libtorrent-python
Requires: rb_libtorrent-python2
#Requires: python-twisted
Requires: python2-twisted
#Requires: python-cherrypy
Requires: python2-cherrypy
#Requires: python-configobj
Requires: python2-configobj
#Requires: python-libnacl
Requires: python2-libnacl
#Requires: python-decorator
Requires: python2-decorator
#Requires: python-qt5
Requires: python2-qt5
Requires: python2-libnacl
#Requires: python-matplotlib
Requires: python2-matplotlib
Requires: python2-matplotlib-qt5
#Requires: python-feedparser
Requires: python2-feedparser
Requires: python2-psutil
Requires: python2-meliae
Requires: python2-pillow-qt
Requires: python2-chardet
Requires: python2-requests
Requires: rb_libtorrent
Requires: python2-service-identity
Requires: python2-keyring
Requires: python2-dns
Requires: python2-ecdsa
Requires: python2-jsonrpclib
Requires: python2-plyvel
Requires: python2-pbkdf2
Requires: python2-protobuf
Requires: python2-pysocks
Requires: python2-scipy
Requires: python2-networkx
Requires: python2-keyrings-alt

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
# Our trick; the tarball doesn't download completely the source code; tribler needs some submodules
# the script makes it for us.

%{S:2} -c %{commit0}
%autosetup -T -D -n %{name}-%{shortcommit0} 

%build
%py2_build

%install
%py2_install

install -d %{buildroot}/usr/{bin,share/tribler}
cp -r Tribler %{buildroot}/usr/share/tribler
cp -r TriblerGUI %{buildroot}/usr/share/tribler
cp Tribler/Core/CacheDB/schema_sdb_v*.sql %{buildroot}/usr/share/tribler/Tribler
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

# We don't need it
rm -f %{buildroot}/%{_datadir}/tribler/Tribler/Core/DecentralizedTracking/pymdht/.git
rm -f %{buildroot}/%{_datadir}/tribler/Tribler/dispersy/.git

%files
%doc *.rst doc
%{_bindir}/%{name}
%{_bindir}/%{name}-gui
%{python2_sitelib}/%{_name}
%{python2_sitelib}/libtribler-*.egg-info
%{python2_sitelib}/TriblerGUI/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}_big.xpm
%{_datadir}/tribler/

%changelog

* Fri Jul 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.1.0-2.exp3
- Rebuilt for Python 3.7

* Mon Jul 02 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 7.1.0-1.exp3
- Update to 7.1.0-1.exp3
- spec file modernized

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
