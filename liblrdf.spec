Summary:	Library to manipulate RDF files describing LADSPA plugins
Summary(pl):	Biblioteka do przetwarzania plik�w RDF opisuj�cych wtyczki LADSPA
Name:		liblrdf
Version:	0.3.7
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://plugin.org.uk/lrdf/%{name}-%{version}.tar.gz
# Source0-md5:	8980f8f2fcef60591b7571bdc8cd0763
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libraptor-devel >= 0.9.11
BuildRequires:	libtool
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a library to make it easy to manipulate RDF files describing
LADSPA plugins. It can also be used for general RDF manipulation. It
can read RDF/XML and N3 files and export N3 files.

%description -l pl
Ta biblioteka powsta�a, aby u�atwi� przetwarzanie plik�w RDF
opisuj�cych wtyczki LADSPA. Mo�e by� u�ywana tak�e do og�lnego
przetwarzania RDF. Jest w stanie czyta� pliki RDF/XML i N3 oraz
eksportowa� do plik�w N3.

%package devel
Summary:	liblrdf header files
Summary(pl):	Pliki nag��wkowe liblrdf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libraptor-devel >= 0.9.11

%description devel
liblrdf library header files.

%description devel -l pl
Pliki nag��wkowe biblioteki liblrdf.

%package static
Summary:	Static liblrdf library
Summary(pl):	Statyczna biblioteka liblrdf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblrdf library.

%description static -l pl
Statyczna biblioteka liblrdf.

%prep
%setup -q

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
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
