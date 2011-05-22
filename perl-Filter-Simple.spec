%define upstream_name    Filter-Simple
%define upstream_version 0.87

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simplified source filtering
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Filter/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(Text::Balanced)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


