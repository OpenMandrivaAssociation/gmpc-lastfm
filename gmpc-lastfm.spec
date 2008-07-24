Summary:	A Last.FM artist art provider plugin for gmpc
Name:		gmpc-lastfm
Version:	0.15.5.0
Release:	%mkrel 3
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-lastfm
Source0:	http://download.sarine.nl/download/gmpc-0.15.5/gmpc-last.fm-%{version}.tar.bz2
BuildRequires:	libmpd-devel
BuildRequires:	libxml2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gmpc-devel
Requires:	gmpc
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The last.fm plugin can fetch artist images, from last.fm.
This plugin doesn't scrobble your music, use a dedicated 
client like mpdscribble for this.

%prep
%setup -qn gmpc-last.fm-%{version}

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/gmpc/plugins/lastfmplugin.la
%{_datadir}/gmpc/plugins/lastfmplugin.so
