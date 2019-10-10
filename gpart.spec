Summary:	Guesses and recovers damaged Master Boot Records
Summary(pl.UTF-8):	Odgaduje zawartość i odzyskuje uszkodzony Master Boot Record
Summary(pt.UTF-8):	Adivinha e recupera um Master Boot Record danificado
Name:		gpart
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/System
Source0:	https://github.com/baruch/gpart/archive/%{version}.tar.gz
# Source0-md5:	2d709068b5123198b3eb337f9d4686a8
URL:		https://github.com/baruch/gpart/
BuildRequires:	autoconf
BuildRequires:	automake
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

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%attr(755,root,root) %{_sbindir}/gpart
%{_mandir}/man8/gpart.8*
