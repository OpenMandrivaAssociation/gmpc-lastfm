Summary:	A Last.FM artist art provider plugin for gmpc
Name:		gmpc-lastfm
Version:	0.20.0
Release:	3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-lastfm
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/gmpc-last-fm-%{version}.tar.gz
BuildRequires:	libmpd-devel >= 0.15.98
BuildRequires:	libxml2-devel 
BuildRequires:	gtk+2-devel >= 2.8
BuildRequires:	gmpc-devel >= 0.16.2
BuildRequires:	intltool
Requires:	gmpc

%description
The last.fm plugin can fetch artist images, from last.fm.
This plugin doesn't scrobble your music, use a dedicated 
client like mpdscribble for this.

%prep
%setup -qn gmpc-last-fm-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/lastfmplugin.so


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2mdv2011.0
+ Revision: 610904
- rebuild

* Mon Apr 05 2010 Funda Wang <fwang@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 531605
- update to new version 0.20.0

* Mon Dec 28 2009 Funda Wang <fwang@mandriva.org> 0.19.0-1mdv2010.1
+ Revision: 482928
- new version 0.19.0

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 379387
- New version 0.18.0

* Sun Jan 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.17.0-1mdv2009.1
+ Revision: 324713
- update to new version 0.17.0
- update to new version 0.17.0

* Wed Dec 03 2008 Funda Wang <fwang@mandriva.org> 0.16.1-2mdv2009.1
+ Revision: 309571
- move plugins into libdir
- new version 0.16.1

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - fix file list
    - update to new version 0.16.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.15.5.0-3mdv2009.0
+ Revision: 246278
- rebuild

* Wed Jan 30 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.15.5.0-1mdv2008.1
+ Revision: 160365
- add spec file
- add source
- Created package structure for gmpc-lastfm.

