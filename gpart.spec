Summary:	Guesses and recovers damaged Master Boot Records
Summary(pl.UTF-8):	Odgaduje zawartość i odzyskuje uszkodzony Master Boot Record
Summary(pt.UTF-8):	Adivinha e recupera um Master Boot Record danificado
Name:		gpart
Version:	0.1h
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://www.stud.uni-hannover.de/user/76201/gpart/%{name}-%{version}.tar.gz
# Source0-md5:	ee3a2d2dde70bcf404eb354b3d1ee6d4
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-ntfs-ppc.patch
Patch2:		%{name}-errno.patch
# ftp://ftp.namesys.com/pub/misc-patches/
Patch3:		gpart-0.1h-reiserfs-3.6.patch.gz
# Patch3-md5:	ed479abcb1d7612669c4275a1c445085
Patch4:		%{name}-x86_64.patch
Patch5:		%{name}-l64seek.patch
URL:		http://www.stud.uni-hannover.de/user/76201/gpart/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Gpart is a small tool which tries to guess what partitions are on a PC
type harddisk in case the primary partition table was damaged.

%description -l pl.UTF-8
Gpart jest niewielkim narzędziem próbującym odgadnąć jakie partycje
znajdują się na twardym dysku. Znajduje on zastosowanie w przypadku
uszkodzenia tablicy partycji.

%description -l pt.UTF-8
Gpart é uma pequena ferramenta que tenha adivinhar quais partições
existem um disco rígido e tenta recuperar a tabela de partições caso
ela esteja danificada.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p2
%patch4 -p1
%patch5 -p1

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
