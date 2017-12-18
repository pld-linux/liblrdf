Summary:	Library to manipulate RDF files describing LADSPA plugins
Summary(pl.UTF-8):	Biblioteka do przetwarzania plików RDF opisujących wtyczki LADSPA
Name:		liblrdf
Version:	0.6.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/swh/LRDF/releases
Source0:	https://github.com/swh/LRDF/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8bb0ac7e8fe1a5a90083c89776bd3deb
URL:		http://sourceforge.net/projects/lrdf/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libraptor2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	ladspa-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library to make it easy to manipulate RDF files describing
LADSPA plugins. It can also be used for general RDF manipulation. It
can read RDF/XML and N3 files and export N3 files.

%description -l pl.UTF-8
Ta biblioteka powstała, aby ułatwić przetwarzanie plików RDF
opisujących wtyczki LADSPA. Może być używana także do ogólnego
przetwarzania RDF. Jest w stanie czytać pliki RDF/XML i N3 oraz
eksportować do plików N3.

%package devel
Summary:	liblrdf header files
Summary(pl.UTF-8):	Pliki nagłówkowe liblrdf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraptor2-devel >= 2.0.0

%description devel
liblrdf library header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblrdf.

%package static
Summary:	Static liblrdf library
Summary(pl.UTF-8):	Statyczna biblioteka liblrdf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblrdf library.

%description static -l pl.UTF-8
Statyczna biblioteka liblrdf.

%prep
%setup -q -n LRDF-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblrdf.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/liblrdf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblrdf.so.2
%{_datadir}/ladspa/rdf/ladspa.rdfs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblrdf.so
%{_includedir}/lrdf*.h
%{_pkgconfigdir}/lrdf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblrdf.a
