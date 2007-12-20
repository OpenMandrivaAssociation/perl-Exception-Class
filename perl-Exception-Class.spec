%define	module	Exception-Class
%define	name	perl-%{module}
%define	version	1.23
%define	release	%mkrel 2

Summary: 	A module that allows you to declare real exception classes in Perl
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{module}-%{version}.tar.bz2
Url: 		http://search.cpan.org/dist/%{module}/
Requires: 	perl perl-Class-Data-Inheritable >= 0.02
Requires:	perl-Devel-StackTrace >= 0.9
BuildRequires:	perl-devel
BuildRequires:	perl-Class-Data-Inheritable
BuildRequires:  perl-Devel-StackTrace
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module allows you to declare hierarchies of exception classes for use
in your code. It also provides a simple exception class that it uses as the
default base class for all other exceptions.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes LICENSE README lib/Exception/Class.pm

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
%doc Changes LICENSE README
%{perl_vendorlib}/Exception
%{_mandir}/*/*
