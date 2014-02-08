%define upstream_name	 Crypt-Rijndael
%define upstream_version 1.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:	Crypt::CBC compliant Rijndael encryption module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements the Rijndael cipher, which has just been selected as the
Advanced Encryption Standard.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc NEWS README
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-6mdv2012.0
+ Revision: 765134
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-5
+ Revision: 763648
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.90.0-4
+ Revision: 676704
- fix build (weird)
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-3mdv2011.0
+ Revision: 555721
- rebuild

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.90.0-2mdv2011.0
+ Revision: 555460
- rebuild

* Mon Jan 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2010.1
+ Revision: 492950
- update to 1.09

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.1
+ Revision: 477618
- update to 1.08

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 403038
- rebuild using %%perl_convert_version

* Sat Aug 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2009.0
+ Revision: 272811
- update to new version 1.07

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.06-2mdv2009.0
+ Revision: 268405
- rebuild early 2009.0 package (before pixel changes)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.06

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.05-2mdv2008.1
+ Revision: 152041
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2008.1
+ Revision: 109518
- new version


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2007.0
+ Revision: 133723
- new version, dropped patch
- Import perl-Crypt-Rijndael

* Tue Mar 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-7mdk
- spec cleanup
- %%mkrel
- rpmbuilupdate aware
- fix directory ownership
- better summary, description and url

* Thu Feb 10 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.05-6mdk
- added P0 (PLD) to make it build on x86_64

* Tue Dec 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-5mdk
- Rebuild for new perl

* Sun Jun 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.05-4mdk
- rebuilt, fix deps
- use macros

