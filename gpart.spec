Summary:	Guesses and recovers damaged Master Boot Records
Summary(pl):	Odgaduje zawarto�� i odzyskuje uszkodzony Master Boot Record
Summary(pt):	Adivinha e recupera um Master Boot Record danificado
Name:		gpart
Version:	0.1h
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.stud.uni-hannover.de/user/76201/gpart/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-ntfs-ppc.patch
Patch2:		%{name}-errno.patch
URL:		http://home.pages.de/~michab/gpart/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%description -l pl
Gpart jest niewielkim narz�dziem pr�buj�cym odgadn�� jakie partycje
znajduj� si� na twardym dysku. Znajduje on zastosowanie w przypadku
uszkodzenia tablicy partycji.

%description -l pt
Gpart � uma pequena ferramenta que tenha adivinhar quais parti��es
existem um disco r�gido e tenta recuperar a tabela de parti��es caso
ela esteja danificada.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install src/gpart $RPM_BUILD_ROOT%{_sbindir}/
install man/gpart.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_sbindir}/gpart
%{_mandir}/man8/*
