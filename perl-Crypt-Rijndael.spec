# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname Crypt-Rijndael
%define modver 1.12

Summary:	Crypt::CBC compliant Rijndael encryption module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Crypt/Crypt-Rijndael-%{modver}.tar.gz
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module implements the Rijndael cipher, which has just been selected as the
Advanced Encryption Standard.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc NEWS README
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%doc %{_mandir}/man3*/*
