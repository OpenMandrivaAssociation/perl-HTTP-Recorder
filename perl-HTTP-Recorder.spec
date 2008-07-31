%define module	HTTP-Recorder
%define name	perl-%{module}
%define version 0.05
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Record interaction with websites
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/L/LE/LEIRA/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a browser-independent recorder for recording interactions with
web sites.

%prep
%setup -q -n %{module}-%{version} 

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




