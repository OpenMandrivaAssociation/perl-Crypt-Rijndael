%define modname	Crypt-Rijndael
%define modver 1.12

Summary:	Crypt::CBC compliant Rijndael encryption module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Crypt/Crypt-Rijndael-%{modver}.tar.gz
BuildRequires:	perl-devel

%description
This module implements the Rijndael cipher, which has just been selected as the
Advanced Encryption Standard.

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc NEWS README
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3*/*



