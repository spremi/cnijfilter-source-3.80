%bcond_with prepare_fastbuild
%bcond_with fastbuild
%bcond_with build_common_package

%define VERSION 3.85
%define RELEASE 1

%define _arc  %(getconf LONG_BIT)

%define _cupslibdir     %{_usr}/lib/cups

%define _ppddir   %{_usr}

%define CNBP_LIBS   libcnbpcmcm libcnbpcnclapi libcnbpcnclbjcmd libcnbpcnclui libcnbpess libcnbpo
%define COM_LIBS    libcnnet

%define PRINT_PKG_PROGRAM   ppd cnijfilter maintenance lgmon cngpijmon

%define PKG %{MODEL}series

Name          : cnijfilter-%{PKG}
Version       : %{VERSION}
Release       : %{RELEASE}
Summary       : IJ Printer Driver Ver.%{VERSION} for Linux

License       : See the LICENSE*.txt file.

Source0       : cnijfilter-source-%{version}-%{release}.tar.gz

BuildRoot     : %{_tmppath}/%{name}-root

Requires      : cnijfilter-common >= %{version} cups popt libxml2 gtk2 libtiff libpng

BuildRequires : cups-devel popt-devel gtk2-devel libxml2-devel libtiff-devel

%if %{with build_common_package}

%package -n cnijfilter-common

Summary       : IJ Printer Driver Ver.%{VERSION} for Linux
License       : See the LICENSE*.txt file.

Requires      : cups popt libxml2 gtk2 libtiff libpng

BuildRequires : cups-devel popt-devel gtk2-devel libxml2-devel libtiff-devel

%endif


%description
IJ Printer Driver for Linux.
This IJ Printer Driver provides printing functions for Canon Inkjet
printers operating under the CUPS (Common UNIX Printing System) environment.

%if %{with build_common_package}

%description -n cnijfilter-common
IJ Printer Driver for Linux.
This IJ Printer Driver provides printing functions for Canon Inkjet
printers operating under the CUPS (Common UNIX Printing System) environment.

%endif


#
# ####################### Prepare for build
#
%prep echo $RPM_BUILD_ROOT

%if %{with fastbuild}

%setup -T -D -n  cnijfilter-source-%{version}-%{RELEASE}

%else

%setup -q -n  cnijfilter-source-%{version}-%{RELEASE}

%endif

%if ! %{with prepare_fastbuild}

%if ! %{defined MODEL}

echo "#### Usage : rpmbuild -bb [spec file] --define=\"MODEL ipXXXX\" --define=\"MODEL_NUM YYY\" ####"
exit 1

%endif

%if ! %{defined MODEL_NUM}

echo "#### Usage : rpmbuild -bb [spec file] --define=\"MODEL ipXXXX\" --define=\"MODEL_NUM YYY\" ####"
exit 1

%endif

%endif


#
# ####################### Build
#
%build

%if %{with prepare_fastbuild}

pushd  ppd
./autogen.sh --prefix=/usr --program-suffix=CN_IJ_MODEL
popd

pushd cnijfilter
./autogen.sh --prefix=%{_prefix} --program-suffix=CN_IJ_MODEL --enable-libpath=%{_libdir}/bjlib --enable-binpath=%{_bindir}
popd

pushd maintenance
./autogen.sh --prefix=%{_prefix} --program-suffix=CN_IJ_MODEL --datadir=%{_prefix}/share --enable-libpath=%{_libdir}/bjlib
popd
pushd lgmon
./autogen.sh --prefix=%{_prefix} --program-suffix=CN_IJ_MODEL --enable-progpath=%{_bindir}
popd

pushd cngpijmon
./autogen.sh --prefix=%{_prefix} --program-suffix=CN_IJ_MODEL  --enable-progpath=%{_bindir} --datadir=%{_prefix}/share
popd

%else

%if %{with fastbuild}

for prg_name in %{PRINT_PKG_PROGRAM};do
  pushd ${prg_name}

  find . -name Makefile -print > file_lists
  find . -name config.h -print >> file_lists

  for fn in `cat file_lists`; do
    if [ ! -f $fn.org ]; then
      cp $fn $fn.org
    fi
    sed -e s/CN_IJ_MODEL_NUM/%{MODEL_NUM}/g $fn.org | sed -e s/CN_IJ_MODEL/%{MODEL}/ > cn_ij_tmp; mv cn_ij_tmp $fn
  done

  make clean
  make

  popd
done

%else

pushd  ppd
./autogen.sh --prefix=/usr --program-suffix=%{MODEL}
make clean
make
popd

pushd cnijfilter
./autogen.sh --prefix=%{_prefix} --program-suffix=%{MODEL} --enable-libpath=%{_libdir}/bjlib --enable-binpath=%{_bindir}
make clean
make
popd

pushd maintenance
./autogen.sh --prefix=%{_prefix} --program-suffix=%{MODEL} --datadir=%{_prefix}/share --enable-libpath=%{_libdir}/bjlib
make clean
make
popd

pushd lgmon
./autogen.sh --prefix=%{_prefix} --program-suffix=%{MODEL} --enable-progpath=%{_bindir}
make clean
make
popd

pushd cngpijmon
./autogen.sh --prefix=%{_prefix} --program-suffix=%{MODEL}  --enable-progpath=%{_bindir} --datadir=%{_prefix}/share
make clean
make
popd

%endif

%endif

%if %{with build_common_package}

pushd libs
./autogen.sh --prefix=%{_prefix}
popd

pushd cngpij
./autogen.sh --prefix=%{_prefix} --enable-progpath=%{_bindir}
popd

pushd cngpijmnt
./autogen.sh --prefix=%{_prefix} --enable-progpath=%{_bindir}
popd

pushd pstocanonij
./autogen.sh --prefix=/usr --enable-progpath=%{_bindir}
popd

pushd backend
./autogen.sh --prefix=/usr
popd

pushd backendnet
./autogen.sh --prefix=%{_prefix} --enable-libpath=%{_libdir}/bjlib --enable-progpath=%{_bindir} LDFLAGS="-L../../com/libs_bin%{_arc}"
popd

pushd cngpijmon/cnijnpr
./autogen.sh --prefix=%{_prefix} --enable-libpath=%{_libdir}/bjlib
popd

make

%endif

#
# ####################### Install
#
%install

pushd  ppd
make install DESTDIR=${RPM_BUILD_ROOT}
popd

pushd cnijfilter
make install DESTDIR=${RPM_BUILD_ROOT}
popd

pushd maintenance
make install DESTDIR=${RPM_BUILD_ROOT}
popd

pushd lgmon
make install DESTDIR=${RPM_BUILD_ROOT}
popd

pushd cngpijmon
make install DESTDIR=${RPM_BUILD_ROOT}
popd

mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/bjlib

install -c -m 644 %{MODEL_NUM}/database/*                 ${RPM_BUILD_ROOT}%{_libdir}/bjlib
install -c -s -m 755 %{MODEL_NUM}/libs_bin%{_arc}/*.so.*  ${RPM_BUILD_ROOT}%{_libdir}

%if %{with build_common_package}

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_cupslibdir}/filter
mkdir -p ${RPM_BUILD_ROOT}%{_cupslibdir}/backend
mkdir -p ${RPM_BUILD_ROOT}%{_prefix}/share/cups/model
mkdir -p ${RPM_BUILD_ROOT}/etc/udev/rules.d/

install -c -m 644 com/ini/cnnet.ini   ${RPM_BUILD_ROOT}%{_libdir}/bjlib

make install DESTDIR=${RPM_BUILD_ROOT}

install -c -s -m 755 com/libs_bin%{_arc}/*.so.*   ${RPM_BUILD_ROOT}%{_libdir}

install -c -m 644 etc/*.rules ${RPM_BUILD_ROOT}/etc/udev/rules.d/

%endif


#
# ####################### Clean
#
%clean
rm -rf $RPM_BUILD_ROOT


#
# ####################### Post Install
#
%post
if [ -x /sbin/ldconfig ]; then
  /sbin/ldconfig
fi

%if %{with build_common_package}

%post -n cnijfilter-common
if [ -e /usr/lib64/cups/backend/usb ] ; then
  rm -f /usr/lib/cups/filter/pstocanonij
  rm -f /usr/lib/cups/backend/cnijusb
  rm -f /usr/lib/cups/backend/cnijnet
  rmdir -p --ignore-fail-on-non-empty /usr/lib/cups/filter
  rmdir -p --ignore-fail-on-non-empty /usr/lib/cups/backend
elif  [ -e /usr/lib/cups/backend/usb ] ; then
  rm -f /usr/lib64/cups/filter/pstocanonij
  rm -f /usr/lib64/cups/backend/cnijusb
  rm -f /usr/lib64/cups/backend/cnijnet
  rmdir -p --ignore-fail-on-non-empty /usr/lib64/cups/filter
  rmdir -p --ignore-fail-on-non-empty /usr/lib64/cups/backend
fi

if [ -x /sbin/ldconfig ]; then
  /sbin/ldconfig
fi

if [ -x /sbin/udevadm ]; then
  /sbin/udevadm control --reload-rules 2> /dev/null
  /sbin/udevadm trigger --action=add --subsystem-match=usb 2> /dev/null
fi

%endif


#
# ####################### Post Uninstall
#
%postun
# remove cnbp* libs
for LIBS in %{CNBP_LIBS}; do
  if [ -h %{_libdir}/${LIBS}%{MODEL_NUM}.so ]; then
    rm -f %{_libdir}/${LIBS}%{MODEL_NUM}.so
  fi
done

if [ "$1" = 0 ] ; then
  rmdir -p --ignore-fail-on-non-empty %{_prefix}/share/locale/*/LC_MESSAGES
  rmdir -p --ignore-fail-on-non-empty %{_prefix}/share/cngpijmon%{MODEL}
  rmdir -p --ignore-fail-on-non-empty %{_prefix}/share/maintenance%{MODEL}
  rmdir -p --ignore-fail-on-non-empty %{_bindir}
fi

if [ -x /sbin/ldconfig ]; then
  /sbin/ldconfig
fi

%if %{with build_common_package}

%postun -n cnijfilter-common
for LIBS in %{COM_LIBS}; do
  if [ -h %{_libdir}/${LIBS}.so ]; then
    rm -f %{_libdir}/${LIBS}.so
  fi
done

if [ "$1" = 0 ] ; then
  rmdir -p --ignore-fail-on-non-empty %{_libdir}/bjlib
fi

if [ -x /sbin/ldconfig ]; then
  /sbin/ldconfig
fi

%endif


#
# ####################### Files and directories owned by this package
#
%files
%defattr(-,root,root)
%{_bindir}/cngpijmon%{MODEL}
%{_bindir}/lgmon%{MODEL}
%{_bindir}/maintenance%{MODEL}
%{_ppddir}/share/cups/model/canon%{MODEL}.ppd
%{_prefix}/share/locale/*/LC_MESSAGES/cngpijmon%{MODEL}.mo
%{_prefix}/share/locale/*/LC_MESSAGES/maintenance%{MODEL}.mo
%{_prefix}/share/cngpijmon%{MODEL}/*
%{_prefix}/share/maintenance%{MODEL}/*

%{_bindir}/cif%{MODEL}
%{_libdir}/libcnbp*%{MODEL_NUM}.so*
%{_libdir}/bjlib/cif%{MODEL}.conf
%{_libdir}/bjlib/cnb_%{MODEL_NUM}0.tbl
%{_libdir}/bjlib/cnbpname%{MODEL_NUM}.tbl

%doc LICENSE-cnijfilter-%{VERSION}JP.txt
%doc LICENSE-cnijfilter-%{VERSION}EN.txt
%doc LICENSE-cnijfilter-%{VERSION}SC.txt
%doc LICENSE-cnijfilter-%{VERSION}FR.txt

%doc lproptions/lproptions-%{MODEL}-%{VERSION}JP.txt
%doc lproptions/lproptions-%{MODEL}-%{VERSION}EN.txt
%doc lproptions/lproptions-%{MODEL}-%{VERSION}SC.txt
%doc lproptions/lproptions-%{MODEL}-%{VERSION}FR.txt

%if %{with build_common_package}

%files -n cnijfilter-common
%defattr(-,root,root)
%{_cupslibdir}/filter/pstocanonij
%{_cupslibdir}/backend/cnijusb
%{_cupslibdir}/backend/cnijnet
%{_bindir}/cngpij
%{_bindir}/cngpijmnt
%{_bindir}/cnijnpr
%{_bindir}/cnijnetprn
%{_libdir}/libcnnet.so*
%attr(644, lp, lp) %{_libdir}/bjlib/cnnet.ini

/etc/udev/rules.d/*.rules

%doc LICENSE-cnijfilter-%{VERSION}JP.txt
%doc LICENSE-cnijfilter-%{VERSION}EN.txt
%doc LICENSE-cnijfilter-%{VERSION}SC.txt
%doc LICENSE-cnijfilter-%{VERSION}FR.txt

%endif


%ChangeLog
* Sun Jul 31 2016 Sanjeev Premi <spremi@ymail.com>
- Bump package version to avoid conflict with existing packages.

* Sun Jul 24 2016 Sanjeev Premi <spremi@ymail.com>
- Initial set of updates tested working with IP7200 series on Fedors 23.

* Thu Jul 14 2016 Sanjeev Premi <spremi@ymail.com>
- Imported source (cnijfilter-source-3.80-1.tar.gz) from Canon
