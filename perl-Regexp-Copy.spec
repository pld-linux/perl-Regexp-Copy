#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Copy
Summary:	Regexp::Copy - copy Regexp objects
Summary(pl):	Regexp::Copy - kopiowanie obiekt�w Regexp
Name:		perl-Regexp-Copy
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0f3875e0655c0ac9eb37813ec82c137
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexp::Copy allows you to copy the contents of one Regexp object to
another. A problem that I have found with the qr// operator is that
the Regexp objects that it creates are is impossible to dereference.
This causes problems if you want to change the data in the regexp
without losing the reference to it. Its impossible. Regexp::Copy
allows you to change the Regexp by copying one object created through
qr// to another.

%description -l pl
Regexp::Copy pozwala na kopiowanie zawarto�ci jednego obiektu Regexp
do innego. Problem z operatorem qr// jest taki, �e do obiekt�w przez
niego utworzonych nie mo�na si�ga�. Powoduje to problemy, je�li chcemy
zmieni� dane w wyra�eniu bez utraty referencji do niego - jest to
niemo�liwe. Regexp::Copy pozwala na modyfikowanie wyra�enia
regularnego poprzez kopiowanie obiektu utworzonego przez qr// do
innego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%dir %{perl_vendorarch}/Regexp
%{perl_vendorarch}/Regexp/*.pm
%dir %{perl_vendorarch}/auto/Regexp/Copy
%{perl_vendorarch}/auto/Regexp/Copy/autosplit.ix
%{perl_vendorarch}/auto/Regexp/Copy/Copy.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Regexp/Copy/Copy.so
%{_mandir}/man3/*
