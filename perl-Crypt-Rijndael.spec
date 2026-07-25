# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define modname Crypt-Rijndael
%define modver 1.16

Summary:	Crypt::CBC compliant Rijndael encryption module
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/leont/crypt-rijndael
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEONT/Crypt-Rijndael-%{modver}.tar.gz
BuildRequires:	make
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
