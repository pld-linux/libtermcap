Summary:	Library for accessing the termcap database
Summary(de.UTF-8):	Library zum Zugriff auf die termcap-Datenbank
Summary(es.UTF-8):	Biblioteca para acceder a base de datos termcap
Summary(fr.UTF-8):	Librairie pour accéder à la base de données termcap
Summary(pl.UTF-8):	Biblioteki dostępu do bazy danych termcap
Summary(pt_BR.UTF-8):	Biblioteca para acessar a base de dados termcap
Summary(tr.UTF-8):	termcap veri tabanına erişim kitaplığı
Name:		libtermcap
Version:	2.0.8
Release:	4
License:	LGPL
Group:		Libraries
Source0:	ftp://sunsite.unc.edu/pub/Linux/GCC/termcap-%{version}.tar.gz
# Source0-md5:	b9256cccfd4ddf725e20bf100f8c001a
Patch0:		%{name}-setuid.patch
Patch1:		%{name}-glibc21.patch
Patch2:		%{name}-xref.patch
Patch3:		%{name}-fix-tc.patch
Patch4:		%{name}-ignore-p.patch
Patch5:		%{name}-bufsize.patch
Patch6:		%{name}-colon.patch
Patch7:		%{name}-buffer.patch
Patch8:		%{name}-aaargh.patch
BuildRequires:	texinfo
Requires:	/etc/termcap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the library for accessing the termcap database.

%description -l de.UTF-8
Dies ist die Library zum Zugriff auf die termcap-Datenbank.

%description -l es.UTF-8
Esta es la biblioteca para acceso al banco de datos termcap.

%description -l fr.UTF-8
Bibliothèque pour accéder à la base de données termcap.

%description -l pl.UTF-8
Biblioteki dostępu do bazy danych termcap.

%description -l pt_BR.UTF-8
Esta é a biblioteca para acesso ao banco de dados termcap.

%description -l tr.UTF-8
Bu paket termcap veri tabanına ulaşım kitaplığını içerir.

%package devel
Summary:	Development libraries and header files for termcap library
Summary(de.UTF-8):	Entwicklungs-Libraries und Header-Dateien für die termcap-Library
Summary(es.UTF-8):	Biblioteca para desarrollo y archivos de inclusión para biblioteca
Summary(fr.UTF-8):	Librairies de développement et fichiers d'en-tête pour la termcap
Summary(pl.UTF-8):	Biblioteki i pliki nagłówkowe dla termcap
Summary(pt_BR.UTF-8):	Biblioteca para desenvolvimento e arquivos de inclusão para biblioteca termcap
Summary(tr.UTF-8):	termcap kitaplığını kullanan geliştirmek için gerekli dosyalar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if "%{_includedir}" == "/usr/include"
Conflicts:	ncurses-devel
%endif

%description devel
This is the package containing the development libaries and header
files for writing programs that access the termcap database. It may be
necessary to build some other packages as well.

%description devel -l pl.UTF-8
Pakiet ten zawiera biblioteki i pliki nagłówkowe dla programistów.

%description devel -l de.UTF-8
Dies ist ein Paket mit Entwicklungs-Libraries und Header-Dateien zum
Schreiben von Programmen, die auf die termcap-Datenbank zugreifen.
Eventuell müssen noch ein paar andere Pakete gebaut werden.

%description devel -l es.UTF-8
Este es el paquete que contiene las bibliotecas y archivos de
inclusión para la escritura de programas que acceden al banco de datos
termcap. Puede ser necesario también para construir otros paquetes.

%description devel -l fr.UTF-8
Ceci est le package contenant les bibliothéques de développement et
les fichiers d'en-tête pour écrire des programmes accédant à la base
de données termcap. Cela peut être nécessaire pour construire certains
autres packages.

%description devel -l pt_BR.UTF-8
Este é o pacote que contém as bibliotecas e arquivos de inclusão para
a escrita de programas que acessam o banco de dados termcap. Ele pode
ser necessário para construir outros pacotes também.

%description devel -l tr.UTF-8
Bu paket, termcap veri tabanını kullanan programlar geliştirmek için
gereken başlık dosyaları ve kitaplıkları içerir.

%package static
Summary:	Static termcap library
Summary(pl.UTF-8):	Statyczna Biblioteka termcap
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com termcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static termcap library.

%description static -l pl.UTF-8
Statyczna biblioteka termcap.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com termcap

%prep
%setup -q -n termcap-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1

%build
cat > config.h <<EOF
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
EOF

%{__make} CFLAGS="%{rpmcflags} -DHAVE_CONFIG_H -I."
%{__make} info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_libdir},%{_includedir},%{_infodir}}

install *.so.* $RPM_BUILD_ROOT/lib
install libtermcap.a $RPM_BUILD_ROOT%{_libdir}/libtermcap.a
install termcap.h $RPM_BUILD_ROOT%{_includedir}/termcap.h
install termcap.info* $RPM_BUILD_ROOT%{_infodir}

ln -sf ../../lib/libtermcap.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtermcap.so

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun devel	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h
%{_infodir}/*.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
