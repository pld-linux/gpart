Summary: Guesses and recovers damaged Master Boot Records
Summary(pt_BR): Adivinha e recupera um Master Boot Record danificado
Summary(es): Guesses and recovers damaged Master Boot Records
Name: gpart
Version: 0.1e
Release: 2cl
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: http://www.stud.uni-hannover.de/user/76201/gpart/gpart-%{version}.tar.gz
BuildRoot: /var/tmp/gpart-%{version}
License: GPL

%description
Gpart is a small tool which tries to guess what partitions
are on a PC type harddisk in case the primary partition table
was damaged.

%description -l pt_BR
Gpart é uma pequena ferramenta que tenha adivinhar quais partições
existem um disco rígido e tenta recuperar a tabela de partições
caso ela esteja danificada.

%description -l es
Gpart is a small tool which tries to guess what partitions
are on a PC type harddisk in case the primary partition table
was damaged.

%prep
%setup
%build
make

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{man/man8,sbin}
install -s -m 755 src/gpart $RPM_BUILD_ROOT/usr/sbin/
install -m 644 man/gpart.8 $RPM_BUILD_ROOT/usr/man/man8/
gzip -9 $RPM_BUILD_ROOT/usr/man/man8/gpart.8

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/gpart
/usr/man/man8/gpart.8.gz

%changelog
* Wed Feb 02 2000 Guilherme Wunsch Manika <gwm@conectiva.com>
- Created first package
