%define	upstream_name	 Exception-Class
%define upstream_version 1.32

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary: 	A module that allows you to declare real exception classes in Perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url: 		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:  perl(Devel::StackTrace) >= 1.20
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
