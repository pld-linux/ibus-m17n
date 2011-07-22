#
# Conditional build:
%bcond_with	bridge_hotkey		# enable the engine hotkeys
#
Summary:	The M17N engine for IBus platform
Name:		ibus-m17n
Version:	1.3.2
Release:	1
License:	GPL v2+
Group:		Libraries
URL:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4c406147318f94e5e805c408c4be075e
Patch0:		%{name}-HEAD.patch
Patch1:		%{name}-iok.patch
Patch2:		%{name}-xkb-options.patch
Patch3:		%{name}-xx-icon-symbol.patch
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	libtool
BuildRequires:	m17n-lib-devel
BuildRequires:	pkgconfig
BuildRequires:	gtk+3-devel
BuildRequires:	ibus-devel >= 1.3.0
BuildRequires:	libxklavier-devel
Requires:	ibus >= 1.3.0
Requires:	iok > 1.3.1
Requires:	m17n-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
M17N engine for IBus input platform. It allows input of many languages
using the input table maps from m17n-db.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%configure \
	%{?with_bridge_hotkey:--with-hotkeys} \
	--with-gtk=3.0

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-m17n
%attr(755,root,root) %{_libexecdir}/ibus-setup-m17n
%{_datadir}/ibus-m17n
%{_datadir}/ibus/component/*
