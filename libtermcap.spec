Summary:     library for accessing the termcap database
Summary(de): Library zum Zugriff auf die termcap-Datenbank
Summary(fr): Librairie pour accéder à la base de données termcap.
Summary(pl): Biblioteki dostêpu do bazy danych termcap
Summary(tr): termcap veri tabanýna eriþim kitaplýðý
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the library for accessing the termcap database.  It is necessary
to be installed for a system to be able to do much of anything.  

%description -l pl
Biblioteki dostêpu do bazy danych termcap'a. Pakiet ten jest wykorzystywany
przez wiele aplikacji i niezbêdny dla systemu.

%description -l de
Dies ist die Library zum Zugriff auf die termcap-Datenbank. Sie muß
installiert werden, damit das System funktionsfähig ist.

%description -l fr
Bibliothèque pour accéder à la base de données termcap. Nécessaire pour
qu'un système puisse faire quelque chose.

%description -l tr
Bu paket termcap veri tabanýna ulaþým kitaplýðýný içerir. Sistem üzerinde
pek çok þeyi yapabilmek için kurulu olmasý gerekmektedir.

%package devel
Summary:     development libraries and header files for termcap library
Summary(de): Entwicklungs-Libraries und Header-Dateien für die termcap-Library
Summary(fr): Librairies de développement et fichiers d'en-tête pour la termcap.
Summary(pl): Biblioteki i pliki nag³ówkowe dla termcap
Summary(tr): termcap kitaplýðýný kullanan geliþtirmek için gerekli dosyalar
Group:       Libraries
Group(pl):   Biblioteki
Requires:    %{name} = %{version}

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

%description -l fr devel
Ceci est le package contenant les bibliothéques de développement et
les fichiers d'en-tête pour écrire des programmes accédant à la base 
de données termcap. Cela peut être nécessaire pour construire certains
autres packages.

%description -l tr devel
Bu paket, termcap veri tabanýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarý ve kitaplýklarý içerir.

%prep
%setup -q -n termcap-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -I." 

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
