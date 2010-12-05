Summary:	A Last.FM artist art provider plugin for gmpc
Name:		gmpc-lastfm
Version:	0.20.0
Release:	%mkrel 2
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%find_lang %name

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/lastfmplugin.la
%{_libdir}/gmpc/plugins/lastfmplugin.so
