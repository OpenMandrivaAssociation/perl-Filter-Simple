%define upstream_name    Filter-Simple
%define upstream_version 0.91

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simplified source filtering
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Filter/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(Text::Balanced)
BuildArch:	noarch

%description
The Problem
    Source filtering is an immensely powerful feature of recent versions of
    Perl. It allows one to extend the language itself (e.g. the Switch
    module), to simplify the language (e.g. Language::Pythonesque), or to
    completely recast the language (e.g. Lingua::Romana::Perligata).
    Effectively, it allows one to use the full power of Perl as its own,
    recursively applied, macro language.

    The excellent Filter::Util::Call module (by Paul Marquess) provides a
    usable Perl interface to source filtering, but it is often too powerful
    and not nearly as simple as it could be.

    To use the module it is necessary to do the following:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.870.0-1mdv2011.0
+ Revision: 677342
- update to new version 0.87

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.850.0-2
+ Revision: 656916
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.850.0-1mdv2011.0
+ Revision: 595972
- update to new version 0.85

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.840.0-2mdv2011.0
+ Revision: 552185
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.840.0-1mdv2010.0
+ Revision: 395254
- import perl-Filter-Simple


* Sun Jul 12 2009 cpan2dist 0.84-1mdv
- initial mdv release, generated with cpan2dist


