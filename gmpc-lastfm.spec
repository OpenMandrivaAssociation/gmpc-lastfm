Summary:	A Last.FM artist art provider plugin for gmpc
Name:		gmpc-lastfm
Version:	0.16.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
Url:		http://www.sarine.nl//gmpc-plugins-lastfm
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/gmpc-last.fm-%{version}.tar.gz
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

%if "%_libdir" != "%_prefix/lib"
mv %buildroot%_prefix/lib %buildroot%_libdir
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/gmpc/plugins/lastfmplugin.la
%{_libdir}/gmpc/plugins/lastfmplugin.so
