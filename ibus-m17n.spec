#
# Conditional build:
%bcond_with	bridge_hotkey		# enable the engine hotkeys
#
Summary:	The M17N engine for IBus platform
Summary(pl.UTF-8):	Silnik M17N dla platformy IBus
Name:		ibus-m17n
Version:	1.3.4
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus/downloads/list
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	6f644b73c5943e3c7fb2e02b9e259804
Patch0:		%{name}-iok.patch
Patch1:		%{name}-xkb-options.patch
Patch2:		%{name}-xx-icon-symbol.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.16.1
BuildRequires:	gnome-common
BuildRequires:	libtool
BuildRequires:	m17n-lib-devel
BuildRequires:	pkgconfig
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	ibus-devel >= 1.4.0
BuildRequires:	libxklavier-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	ibus >= 1.4.0
Requires:	iok > 1.3.1
Requires:	m17n-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
M17N engine for IBus input platform. It allows input of many languages
using the input table maps from m17n-db.

%description -l pl.UTF-8
Silnik M17N dla platformy wprowadzania znaków IBus. Pozwala na
wprowadzanie znaków z wielu języków przy użyciu map tablic wejściowych
z m17n-db.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_bridge_hotkey:--with-hotkeys} \
	--with-gtk=3.0

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not yet - only single, empty file exists
#find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-m17n
%attr(755,root,root) %{_libexecdir}/ibus-setup-m17n
%{_datadir}/ibus-m17n
%{_datadir}/ibus/component/m17n.xml
