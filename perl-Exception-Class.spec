%define	module	Exception-Class
%define	name	perl-%{module}
%define	version	1.26
%define	release	%mkrel 1

Summary: 	A module that allows you to declare real exception classes in Perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{module}/
Source: 	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.bz2
Requires: 	perl-Class-Data-Inheritable >= 0.02
Requires:	perl-Devel-StackTrace >= 0.9
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:  perl(Devel::StackTrace) >= 1.20
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes LICENSE lib/Exception/Class.pm

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
%doc Changes LICENSE
%{perl_vendorlib}/Exception
%{_mandir}/*/*
