Summary:	Guesses and recovers damaged Master Boot Records
Summary(es):	Guesses and recovers damaged Master Boot Records
Summary(pt):	Adivinha e recupera um Master Boot Record danificado
Name:		gpart
Version:	0.1g
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://www.stud.uni-hannover.de/user/76201/gpart/%{name}-%{version}.tar.gz
Patch0:		gpart-Makefile.patch
URL:		http://home.pages.de/~michab/gpart
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%description -l es
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%description -l pt
Gpart é uma pequena ferramenta que tenha adivinhar quais partições
existem um disco rígido e tenta recuperar a tabela de partições caso
ela esteja danificada.

%prep
%setup -q
%patch0 -p1

%build
%{__make} LDFLAGS="-s" OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install -s src/gpart $RPM_BUILD_ROOT%{_sbindir}/
install man/gpart.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	Changes README

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/gpart
%{_mandir}/man8/*
