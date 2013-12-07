%define	modname	Exception-Class
%define modver	1.32

Summary:	A module that allows you to declare real exception classes in Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Devel::StackTrace) >= 1.20
BuildRequires:	perl-devel
Requires:	perl-Class-Data-Inheritable >= 0.02
Requires:	perl-Devel-StackTrace >= 0.9

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%setup -qn %{modname}-%{modver}
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
%{_mandir}/man3/*

