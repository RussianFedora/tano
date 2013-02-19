Summary:	Open-source cross-platform IP TV player
Name:		tano
Version:	1.2.1
Release:	1%{?dist}

URL:		http://sourceforge.net/projects/tano
Group:		Applications/Multimedia
License:	GPLv3
Source:		http://downloads.sourceforge.net/project/%{name}/Tano%20Player/1.2.1/%{name}_%{version}_src.tar.gz

BuildRequires:	qt-devel
BuildRequires:	vlc-devel
BuildRequires:	cmake
BuildRequires:	vlc-qt-devel

Requires:	vlc-qt >= 0.6.1

%description
Tano is an open-source cross-platform IP TV player. It is combining 
Qt and Videolan libraries. Project started because of a need of a 
simple IP TV player on Linux providing EPG.

%prep
%setup -q

%build
%cmake
export CFLAGS="$RPM_OPT_FLAGS -ffast-math"
make

%install
make DESTDIR=%{buildroot} install

strip %{buildroot}%{_libdir}/libtanocore.so.1
strip %{buildroot}%{_libdir}/libtanowidgets.so.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS
%{_bindir}/%{name}
%{_libdir}/*so.*
%exclude %{_libdir}/*.so
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png


%changelog
* Tue Feb 19 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 1.2.1-1.R
- initial build
