Summary:	Guesses and recovers damaged Master Boot Records
Summary(es):	Guesses and recovers damaged Master Boot Records
Summary(pt):	Adivinha e recupera um Master Boot Record danificado
Name:		gpart
Version:	0.1g
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.stud.uni-hannover.de/user/76201/gpart/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://home.pages.de/~michab/gpart/
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
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install src/gpart $RPM_BUILD_ROOT%{_sbindir}/
install man/gpart.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/gpart
%{_mandir}/man8/*
