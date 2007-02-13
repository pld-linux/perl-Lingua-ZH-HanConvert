#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	ZH-HanConvert
Summary:	Lingua::ZH::HanConvert - convert Traditional Chinese <-> Simplified Chinese
Summary(pl.UTF-8):	Lingua::ZH::HanConvert - konwersja chiński tradycyjny <-> chiński uproszczony
Name:		perl-Lingua-ZH-HanConvert
Version:	0.12
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	918d5221e27fbe5ca8ab1ac81e0c5e10
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In the 1950's, the Chinese government simplified over 2000 Chinese
characters. Taiwan and Hong Kong still use the traditional characters.
The simplified characters are hard to read if you only know the
traditional ones, and vice-versa. This module attempts to convert
Chinese text between the two forms, using character-by-character
transliteration.

%description -l pl.UTF-8
W latach 1950-tych rząd chiński uprościł ponad 2000 chińskich
ideogramów. Tajwan i Hong Kong nadal używają ideogramów tradycyjnych.
Ideogramy uproszczone są nieczytelne dla znających tylko tradycyjne
i odwrotnie. Moduł dokonuje wzajemnej konwersji tekstów chińskich
w tych dwu postaciach stosując z transliterację znak po znaku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^use v5\.6\.0(;.*)$/use 5.006_00$1/' HanConvert.pm

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorlib}/Lingua/ZH
%{perl_vendorlib}/Lingua/ZH/HanConvert.pm
%{_mandir}/man3/*
