Summary:     library for accessing the termcap database
Summary(de): Library zum Zugriff auf die termcap-Datenbank
Summary(fr): Librairie pour acc�der � la base de donn�es termcap.
Summary(pl): Biblioteki dost�pu do bazy danych termcap
Summary(tr): termcap veri taban�na eri�im kitapl���
Name:        libtermcap
Version:     2.0.8
Release:     2
Group:       Libraries
Group(pl):   Biblioteki
Copyright:   LGPL
Source:      ftp://sunsite.unc.edu/pub/Linux/GCC/termcap-%{version}.tar.gz
Patch0:      termcap-%{version}-shared.patch
Patch1:      termcap-%{version}-setuid.patch
Requires:    /etc/termcap
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is the library for accessing the termcap database.  It is necessary
to be installed for a system to be able to do much of anything.  

%description -l pl
Biblioteki dost�pu do bazy danych termcap'a. Pakiet ten jest wykorzystywany
przez wiele aplikacji i niezb�dny dla systemu.

%description -l de
Dies ist die Library zum Zugriff auf die termcap-Datenbank. Sie mu�
installiert werden, damit das System funktionsf�hig ist.

%description -l fr
Biblioth�que pour acc�der � la base de donn�es termcap. N�cessaire pour
qu'un syst�me puisse faire quelque chose.

%description -l tr
Bu paket termcap veri taban�na ula��m kitapl���n� i�erir. Sistem �zerinde
pek �ok �eyi yapabilmek i�in kurulu olmas� gerekmektedir.

%package devel
Summary:     development libraries and header files for termcap library
Summary(de): Entwicklungs-Libraries und Header-Dateien f�r die termcap-Library
Summary(fr): Librairies de d�veloppement et fichiers d'en-t�te pour la termcap.
Summary(pl): Biblioteki i pliki nag��wkowe dla termcap
Summary(tr): termcap kitapl���n� kullanan geli�tirmek i�in gerekli dosyalar
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name} = %{version}

%description devel
This is the package containing the development libaries and header
files for writing programs that access the termcap database.  It may
be necessary to build some other packages as well.

%description -l pl devel
Pakiet ten zawiera biblioteki i pliki nag��wkowe dla programist�w,
niezb�dne r�wnie� do przebudowy wielu pakiet�w �r�d�owych.

%description -l de devel
Dies ist ein Paket mit Entwicklungs-Libraries und Header-Dateien
zum Schreiben von Programmen, die auf die termcap-Datenbank
zugreifen. Eventuell m�ssen noch ein paar andere Pakete gebaut
werden.

%description -l fr devel
Ceci est le package contenant les biblioth�ques de d�veloppement et
les fichiers d'en-t�te pour �crire des programmes acc�dant � la base 
de donn�es termcap. Cela peut �tre n�cessaire pour construire certains
autres packages.

%description -l tr devel
Bu paket, termcap veri taban�n� kullanan programlar geli�tirmek i�in gereken
ba�l�k dosyalar� ve kitapl�klar� i�erir.

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
install libtermcap.a $RPM_BUILD_ROOT%{_libdir}/libtermcap.a
install termcap.h $RPM_BUILD_ROOT%{_includedir}/termcap.h

ln -sf libtermcap.so.%{version} $RPM_BUILD_ROOT/lib/libtermcap.so.2
ln -sf ../../lib/libtermcap.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtermcap.so

gzip -9nf README ChangeLog

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
/lib/*.so.*

%files devel
%defattr(644,root,root,755)
%doc {README,ChangeLog}.gz

%{_libdir}/*.a
%{_includedir}/*.h

%attr(755,root,root) %{_libdir}/*.so

%changelog
* Sun Mar 14 1999 Micha� Kuratczyk <kura@pld.org.pl>
  [2.0.8-2]
- added gzipping documentation
- cosmetic changes

* Sun Feb 28 1999 Piotr Czerwi�ski <pius@ceti.com.pl>
- fixed CFLAGS definition,
- added Polish group description,
- cosmetic changes.

* Sun Jul 19 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
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
