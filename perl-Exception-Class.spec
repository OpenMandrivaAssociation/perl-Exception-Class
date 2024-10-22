%define	modname	Exception-Class

Summary:	A module that allows you to declare real exception classes in Perl

Name:		perl-%{modname}
Version:	1.44
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Exception::Class
Source0:	https://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl-devel
Requires:	perl-Class-Data-Inheritable
Requires:	perl-Devel-StackTrace
# For tests
BuildRequires:	perl(Test::More)

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%autosetup -p1 -n %{modname}-%{version}
chmod 644 Changes LICENSE lib/Exception/Class.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes LICENSE
%{perl_vendorlib}/Exception
%{_mandir}/man3/*
