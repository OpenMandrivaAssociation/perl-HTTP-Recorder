%define upstream_name	 HTTP-Recorder
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Record interaction with websites
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEIRA/%{upstream_name}-%{upstream_version}.tar.bz2
# patch from https://rt.cpan.org/Public/Bug/Display.html?id=14388
# fix crash preventing the use of HTTP-Recorder
Patch0:		HTTP-Recorder-0.05-fix_cpan_14388.diff
BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTTP::Request::Params)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(URI)
BuildRequires:	perl(Email::Simple)
BuildRequires:	perl(Class::Accessor::Fast)
BuildArch:	noarch

%description
This is a browser-independent recorder for recording interactions with
web sites.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/HTTP
%{_mandir}/*/*


%changelog
* Wed Mar 10 2010 Michael Scherer <misc@mandriva.org> 0.50.0-2mdv2010.1
+ Revision: 517256
- fix crash " Can't locate object method "query_param"", patch from Stephen R. Scaffidi

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 403268
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.05-5mdv2009.0
+ Revision: 257249
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.05-3mdv2008.1
+ Revision: 135847
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.05-3mdv2007.0
+ Revision: 73490
- import perl-HTTP-Recorder-0.05-3mdv2007.1

* Tue Apr 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-2mdk
- Add BuildRequires

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- 0.0.5 
- rpmbuildupdate aware
- spec cleanup
- better summary

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdk
- initial Mandriva package

