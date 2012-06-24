Summary:	Library for accessing the termcap database
Summary(de):	Library zum Zugriff auf die termcap-Datenbank
Summary(es):	Biblioteca para acceder a base de datos termcap
Summary(fr):	Librairie pour acc�der � la base de donn�es termcap
Summary(pl):	Biblioteki dost�pu do bazy danych termcap
Summary(pt_BR):	Biblioteca para acessar a base de dados termcap
Summary(tr):	termcap veri taban�na eri�im kitapl���
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

%description -l de
Dies ist die Library zum Zugriff auf die termcap-Datenbank.

%description -l es
Esta es la biblioteca para acceso al banco de datos termcap.

%description -l fr
Biblioth�que pour acc�der � la base de donn�es termcap.

%description -l pl
Biblioteki dost�pu do bazy danych termcap.

%description -l pt_BR
Esta � a biblioteca para acesso ao banco de dados termcap.

%description -l tr
Bu paket termcap veri taban�na ula��m kitapl���n� i�erir.

%package devel
Summary:	Development libraries and header files for termcap library
Summary(de):	Entwicklungs-Libraries und Header-Dateien f�r die termcap-Library
Summary(es):	Biblioteca para desarrollo y archivos de inclusi�n para biblioteca
Summary(fr):	Librairies de d�veloppement et fichiers d'en-t�te pour la termcap
Summary(pl):	Biblioteki i pliki nag��wkowe dla termcap
Summary(pt_BR):	Biblioteca para desenvolvimento e arquivos de inclus�o para biblioteca termcap
Summary(tr):	termcap kitapl���n� kullanan geli�tirmek i�in gerekli dosyalar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if "%{_includedir}" == "/usr/include"
Conflicts:	ncurses-devel
%endif

%description devel
This is the package containing the development libaries and header
files for writing programs that access the termcap database. It may be
necessary to build some other packages as well.

%description devel -l pl
Pakiet ten zawiera biblioteki i pliki nag��wkowe dla programist�w.

%description devel -l de
Dies ist ein Paket mit Entwicklungs-Libraries und Header-Dateien zum
Schreiben von Programmen, die auf die termcap-Datenbank zugreifen.
Eventuell m�ssen noch ein paar andere Pakete gebaut werden.

%description devel -l es
Este es el paquete que contiene las bibliotecas y archivos de
inclusi�n para la escritura de programas que acceden al banco de datos
termcap. Puede ser necesario tambi�n para construir otros paquetes.

%description devel -l fr
Ceci est le package contenant les biblioth�ques de d�veloppement et
les fichiers d'en-t�te pour �crire des programmes acc�dant � la base
de donn�es termcap. Cela peut �tre n�cessaire pour construire certains
autres packages.

%description devel -l pt_BR
Este � o pacote que cont�m as bibliotecas e arquivos de inclus�o para
a escrita de programas que acessam o banco de dados termcap. Ele pode
ser necess�rio para construir outros pacotes tamb�m.

%description devel -l tr
Bu paket, termcap veri taban�n� kullanan programlar geli�tirmek i�in
gereken ba�l�k dosyalar� ve kitapl�klar� i�erir.

%package static
Summary:	Static termcap library
Summary(pl):	Statyczna Biblioteka termcap
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com termcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static termcap library.

%description static -l pl
Statyczna biblioteka termcap.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com termcap

%prep
%setup -q -n termcap-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

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
%{_infodir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
