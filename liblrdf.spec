Summary:	Library to manipulate RDF files describing LADSPA plugins
Summary(pl):	Biblioteka do przetwarzania plików RDF opisuj±cych wtyczki LADSPA
Name:		liblrdf
Version:	0.3.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://plugin.org.uk/lrdf/%{name}-%{version}.tar.gz
BuildRequires:	libraptor-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library to make it easy to manipulate RDF files describing
LADSPA plugins. It can also be used for general RDF manipulation. It
can read RDF/XML and N3 files and export N3 files.

%description -l pl
Ta biblioteka powsta³a, aby u³atwiæ przetwarzanie plików RDF
opisuj±cych wtyczki LADSPA. Mo¿e byæ u¿ywana tak¿e do ogólnego
przetwarzania RDF. Jest w stanie czytaæ pliki RDF/XML i N3 oraz
eksportowaæ do plików N3.

%package devel
Summary:	liblrdf header files
Summary(pl):	Pliki nag³ówkowe liblrdf
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
liblrdf library header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki liblrdf.

%package static
Summary:	Static liblrdf library
Summary(pl):	Statyczna biblioteka liblrdf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static liblrdf library.

%description static -l pl
Statyczna biblioteka liblrdf.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/ladspa
%dir %{_datadir}/ladspa/rdf
%{_datadir}/ladspa/rdf/ladspa.rdfs

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
