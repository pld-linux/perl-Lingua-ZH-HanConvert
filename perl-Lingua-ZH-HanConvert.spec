#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	ZH-HanConvert
Summary:	Lingua::ZH::HanConvert - convert Traditional Chinese <-> Simplified Chinese
Summary(pl):	Lingua::ZH::HanConvert - konwersja chiñski tradycyjny <-> chiñski uproszczony
Name:		perl-Lingua-ZH-HanConvert
Version:	0.12
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In the 1950's, the Chinese government simplified over 2000 Chinese
characters. Taiwan and Hong Kong still use the traditional characters.
The simplified characters are hard to read if you only know the
traditional ones, and vice-versa. This module attempts to convert
Chinese text between the two forms, using character-by-character
transliteration.

%description -l pl
W latach 1950-tych rz±d chiñski upro¶ci³ ponad 2000 chiñskich
ideogramów. Tajwan i Hong Kong nadal u¿ywaj± ideogramów tradycyjnych.
Ideogramy uproszczone s± nieczytelne dla znaj±cych tylko tradycyjne
i odwrotnie. Modu³ dokonuje wzajemnej konwersji tekstów chiñskich
w tych dwu postaciach stosuj±c z transliteracjê znak po znaku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_sitelib}/Lingua/ZH
%{perl_sitelib}/Lingua/ZH/HanConvert.pm
%{_mandir}/man3/*
