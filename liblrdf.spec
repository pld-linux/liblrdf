Summary:	-
Summary(pl):	-
Name:		liblrdf
Version:	0.3.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://plugin.org.uk/lrdf/%{name}-%{version}.tar.gz
BuildRequires:	libraptor-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
