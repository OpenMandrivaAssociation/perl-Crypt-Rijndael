%define module	Crypt-Rijndael
%define name	perl-%{module}
%define version	1.04
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Crypt::CBC compliant Rijndael encryption module
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/D/DI/DIDO/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
Source0:	Crypt-Rijndael-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module implements the Rijndael cipher, which has just been selected as the
Advanced Encryption Standard.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor CFLAGS="%{optflags}"
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
%doc NEWS README
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3*/*


