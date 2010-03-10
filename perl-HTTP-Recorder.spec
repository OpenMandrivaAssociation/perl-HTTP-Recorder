%define upstream_name	 HTTP-Recorder
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Record interaction with websites
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEIRA/%{upstream_name}-%{upstream_version}.tar.bz2
# patch from https://rt.cpan.org/Public/Bug/Display.html?id=14388
# fix crash preventing the use of HTTP-Recorder
Patch0:      HTTP-Recorder-0.05-fix_cpan_14388.diff
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTTP::Request::Params)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(URI)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Class::Accessor::Fast)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a browser-independent recorder for recording interactions with
web sites.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*
