%define _name Tribler

Name: tribler
Summary: Privacy enhanced BitTorrent client with P2P content discovery
Version: 6.6.0
Release: 0.exp1.2
License: MIT
Group: Productivity/Networking/Other
URL: http://www.tribler.org/
Source0: https://github.com/Tribler/tribler/releases/download/v%{version}-exp1/%{_name}-v%{version}-exp1.tar.xz
Patch1: https://raw.githubusercontent.com/UnitedRPMs/tribler/master/setup.py.patch
BuildRequires: python-devel
Requires: openssl-full
Requires: swig
Requires: wxPython
Requires: m2crypto
Requires: vlc
Requires: python-apsw
Requires: libsodium python-cryptography python-plyvel
Requires: scons python-netifaces python-igraph python-pyasn1 gmpy
Requires: rb_libtorrent-python python-twisted
Requires: python-cherrypy python-configobj
#Requires: python-libnacl 
Requires: python-decorator

BuildArch: noarch

%description
Tribler is an application that enables its users to find,
enjoy and share content. With content we mean video,
audio, pictures, and much more.
Tribler has three goals in helping you, the user:
1. Find content
2. Consume content
3. share content

%prep
%setup -q -n %{name}
%patch1 -p1 

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%__install -Dm755 Tribler/Main/tribler.py $RPM_BUILD_ROOT%{_bindir}/%{name}
%__install -Dm644 Tribler/Main/Build/Ubuntu/tribler.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__install -pm644 Tribler/Main/Build/Ubuntu/tribler_big.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%__install -pm644 Tribler/Main/Build/Ubuntu/tribler.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/tribler
%__install -pm644 logger.conf $RPM_BUILD_ROOT%{_datadir}/tribler/

%files
%doc *.rst doc
%{_bindir}/%{name}
%{python_sitelib}/%{_name}
%{python_sitelib}/libtribler-*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}_big.xpm
%{_datadir}/tribler/

%changelog
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
