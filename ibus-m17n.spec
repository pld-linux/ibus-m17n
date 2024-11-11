Summary:	The M17N engine for IBus platform
Summary(pl.UTF-8):	Silnik M17N dla platformy IBus
Name:		ibus-m17n
Version:	1.4.34
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/ibus/ibus-m17n/releases
Source0:	https://github.com/ibus/ibus-m17n/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0f1c453ce850049261292f0837b20f8f
URL:		https://github.com/ibus/ibus-m17n
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	libtool
BuildRequires:	m17n-lib-devel
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	ibus-devel >= 1.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	ibus >= 1.4.0
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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-gtk=3.0

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-m17n
%attr(755,root,root) %{_libexecdir}/ibus-setup-m17n
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.m17n.gschema.xml
%{_datadir}/ibus-m17n
%{_datadir}/ibus/component/m17n.xml
%{_datadir}/metainfo/m17n.appdata.xml
%{_desktopdir}/ibus-setup-m17n.desktop
%{_iconsdir}/hicolor/*x*/apps/ibus-m17n.png
%{_iconsdir}/hicolor/scalable/apps/ibus-m17n.svg
