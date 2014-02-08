%define	upstream_name	 Exception-Class
%define upstream_version 1.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	A module that allows you to declare real exception classes in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Devel::StackTrace) >= 1.20
BuildRequires:	perl-devel

BuildArch: 	noarch

Requires: 	perl-Class-Data-Inheritable >= 0.02
Requires:	perl-Devel-StackTrace >= 0.9

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes LICENSE lib/Exception/Class.pm

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE
%{perl_vendorlib}/Exception
%{_mandir}/*/*

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.320.0-5mdv2012.0
+ Revision: 765201
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.320.0-4
+ Revision: 763717
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.320.0-3
+ Revision: 667130
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.320.0-2mdv2011.0
+ Revision: 564734
- rebuild for perl 5.12.1

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.320.0-1mdv2011.0
+ Revision: 552697
- update to 1.32

* Mon Mar 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.300.0-1mdv2010.1
+ Revision: 526441
- update to 1.30

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.0-1mdv2010.0
+ Revision: 403161
- rebuild using %%perl_convert_version

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2010.0
+ Revision: 373749
- update to new version 1.29

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2010.0
+ Revision: 372881
- update to new version 1.28

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2010.0
+ Revision: 372108
- update to new version 1.27

* Wed Oct 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdv2009.1
+ Revision: 298160
- new version

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2009.1
+ Revision: 296794
- update to new version 1.25

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.24-2mdv2009.0
+ Revision: 268504
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.0
+ Revision: 195407
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.23-2mdv2008.0
+ Revision: 64796
- rebuild


* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdk
- New release 1.23

* Tue Oct 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdk
- New release 1.22
- spec cleanup
- fix sources url
- better url
- better summary
- %%mkrel
- make test in %%check
- fix directory ownership

* Wed May 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.21-1mdk
- 1.21

* Tue Jan 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.20-1mdk
- 1.20
- Restore tests

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.19-1mdk
- 1.19
- wipe out buildroot in %%install, not %%prep
- use %%makeinstall_std macro
- drop test for now

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 1.14-1mdk
- 1.14.

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.01-4mdk
- rebuild for new auto{prov,req}

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 1.01-3mdk
- rebuild

