Summary:     library for accessing the termcap database
Name:        libtermcap
Version:     2.0.8
Release:     1d
Source:      ftp://sunsite.unc.edu/pub/Linux/GCC/termcap-%{version}.tar.gz
Copyright:   LGPL
Group:       Libraries
Group(pl):   Biblioteki
Patch0:      termcap-%{version}-shared.patch
Patch1:      termcap-%{version}-setuid.patch
Requires:    /etc/termcap
Buildroot:   /tmp/%{name}-%{version}-root
Summary(de): Library zum Zugriff auf die termcap-Datenbank
Summary(fr): Librairie pour accéder à la base de données termcap.
Summary(pl): Biblioteki dostêpu do bazy danych termcap
Summary(tr): termcap veri tabanýna eriþim kitaplýðý

%description
This is the library for accessing the termcap database.  It is necessary
to be installed for a system to be able to do much of anything.  

%description -l pl
Biblioteki dostêpu dla bazy danych termcap'a. Pakiet ten jest wykorzystywany
przez wiele aplikacji i niezbêdny dla systemu.

%package devel
Summary:     development libraries and header files for termcap library
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name} = %{version}
Summary(de): Entwicklungs-Libraries und Header-Dateien für die termcap-Library
Summary(fr): Librairies de développement et fichiers d'en-tête pour la termcap.
Summary(pl): Biblioteki i pliki nag³ówkowe dla termcap
Summary(tr): termcap kitaplýðýný kullanan geliþtirmek için gerekli dosyalar

%description devel
This is the package containing the development libaries and header
files for writing programs that access the termcap database.  It may
be necessary to build some other packages as well.

%description -l pl devel
Pakiet ten zawiera biblioteki i pliki nag³ówkowe dla programistów,
niezbêdne równie¿ do przebudowy wielu pakietów ¼ród³owych.

%description -l de devel
Dies ist ein Paket mit Entwicklungs-Libraries und Header-Dateien
zum Schreiben von Programmen, die auf die termcap-Datenbank
zugreifen. Eventuell müssen noch ein paar andere Pakete gebaut
werden.

%description -l de
Dies ist die Library zum Zugriff auf die termcap-Datenbank. Sie muß
installiert werden, damit das System funktionsfähig ist.

%description -l fr devel
Ceci est le package contenant les bibliothéques de développement et
les fichiers d'en-tête pour écrire des programmes accédant à la base 
de données termcap. Cela peut être nécessaire pour construire certains
autres packages.

%description -l fr
Bibliothèque pour accéder à la base de données termcap. Nécessaire pour
qu'un système puisse faire quelque chose.

%description -l tr devel
Bu paket, termcap veri tabanýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarý ve kitaplýklarý içerir.

%description -l tr
Bu paket termcap veri tabanýna ulaþým kitaplýðýný içerir. Sistem üzerinde
pek çok þeyi yapabilmek için kurulu olmasý gerekmektedir.

%prep
%setup -q -n termcap-%{version}
%patch0 -p1
%patch1 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -I." 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{lib,usr/{lib,include}}

install *.so.* $RPM_BUILD_ROOT/lib
install libtermcap.a $RPM_BUILD_ROOT/usr/lib/libtermcap.a
install termcap.h $RPM_BUILD_ROOT/usr/include/termcap.h
ln -sf libtermcap.so.%{version} $RPM_BUILD_ROOT/lib/libtermcap.so.2
ln -sf ../../lib/libtermcap.so.%{version} $RPM_BUILD_ROOT/usr/lib/libtermcap.so

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
/lib/*.so.*

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog

/usr/lib/*.a
/usr/include/*.h

%attr(755,root,root) /usr/lib/*.so

%changelog
* Sun Feb 28 1999 Piotr Czerwiñski <pius@ceti.com.pl>
- fixed CFLAGS definition,
- added Polish group description,
- cosmetic changes.

* Sun Jul 19 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
[2.0.8-1d]
- build for PLD Tornado,
- translation modified for pl,
- build from non root's account.
- major changes.

* Tue Jun 30 1998 Alan Cox <alan@redhat.com>
- But assume system termcap is sane. Also handle setfsuid return right.

* Tue Jun 30 1998 Alan Cox <alan@redhat.com>
- TERMCAP environment hole for setuid apps squished.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc
