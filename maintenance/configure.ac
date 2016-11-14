dnl Process this file with autoconf to produce a configure script.

AC_INIT([maintenance],[3.85-1],[no-define])

AM_INIT_AUTOMAKE

AC_ARG_PROGRAM

if test "x${program_suffix}" = "xNONE"; then
  program_suffix="mp230"
  program_transform_name="s,\$\$,${program_suffix},;"
fi

AM_CONFIG_HEADER(config.h)
AM_MAINTAINER_MODE

AH_TEMPLATE([ENABLE_NLS])
AH_TEMPLATE([HAVE_CATGETS])
AH_TEMPLATE([HAVE_GETTEXT])
AH_TEMPLATE([GETTEXT_PACKAGE])
AH_TEMPLATE([HAVE_LC_MESSAGES])
AH_TEMPLATE([HAVE_STPCPY])
AH_TEMPLATE([HAVE_LIBSM])
AH_TEMPLATE([PACKAGE_LOCALE_DIR])
AH_TEMPLATE([PACKAGE_DATA_DIR])
AH_TEMPLATE([PACKAGE_SOURCE_DIR])
AH_TEMPLATE([PACKAGE_PRINTER_MODEL])
AH_TEMPLATE([XBJLIBPATH])

AC_DEFINE_UNQUOTED([PACKAGE_PRINTER_MODEL], ["${program_suffix}"], [PACKAGE_PRINTER_MODEL])

CNIJ_MODEL=${program_suffix}
AC_SUBST(CNIJ_MODEL)

case "${program_suffix}" in
  mp230) CNCL_LIB_ID=401;;
  mg2200) CNCL_LIB_ID=402;;
  e510) CNCL_LIB_ID=403;;
  mg3200) CNCL_LIB_ID=404;;
  mg4200) CNCL_LIB_ID=405;;
  ip7200) CNCL_LIB_ID=406;;
  mg5400) CNCL_LIB_ID=407;;
  mg6300) CNCL_LIB_ID=408;;
  CN_IJ_MODEL) CNCL_LIB_ID=CN_IJ_MODEL_NUM;;
esac
AC_SUBST(CNCL_LIB_ID)

AC_ARG_ENABLE(uidebug)
if test "x${enable_uidebug}" = "xyes"; then
  UI_DFLAGS=-D_PRINTUI_DEBUG_
fi

AC_SUBST(UI_DFLAGS)

AC_ARG_ENABLE(libpath)
if test "x${enable_libpath}" = "x"; then
  enable_libpath="/usr/lib/bjlib"
fi

AC_DEFINE_UNQUOTED([XBJLIBPATH], ["${enable_libpath}"], [XBJLIBPATH])
AC_SUBST(XBJLIBPATH)


AC_SEARCH_LIBS([strerror],[cposix])
AC_PROG_CC
AM_PROG_CC_STDC
AC_HEADER_STDC

AM_PATH_GTK_2_0(2.6.0, ,
            AC_MSG_ERROR(Cannot find GTK: Is gtk-config in path?))

GETTEXT_PACKAGE=maintenance${program_suffix}

AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED([GETTEXT_PACKAGE], ["${GETTEXT_PACKAGE}"], [GETTEXT_PACKAGE])

dnl Add the languages which your application supports here.
ALL_LINGUAS="cs da de el es fi fr hu it ja ko nl nb pl pt ru sv th tr zh zh_TW id"
AM_GLIB_GNU_GETTEXT

dnl Set PACKAGE_LOCALE_DIR in config.h.
if test "x${prefix}" = "xNONE"; then
  AC_DEFINE_UNQUOTED(PACKAGE_LOCALE_DIR, "${ac_default_prefix}/${DATADIRNAME}/locale")
else
  AC_DEFINE_UNQUOTED([PACKAGE_LOCALE_DIR], ["${prefix}/${DATADIRNAME}/locale"], [PACKAGE_LOCALE_DIR])
fi

dnl Set PACKAGE_DATA_DIR in config.h.
if test "x${datadir}" = 'x${prefix}/share'; then
  if test "x${prefix}" = "xNONE"; then
    AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${ac_default_prefix}/share/${PACKAGE}"], [PACKAGE_DATA_DIR])
  else
    AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${prefix}/share/${PACKAGE}"], [PACKAGE_DATA_DIR])
  fi
else
  AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${datadir}/${PACKAGE}"], [PACKAGE_DATA_DIR])
fi

dnl Set PACKAGE_SOURCE_DIR in config.h.
packagesrcdir=`cd $srcdir && pwd`
AC_DEFINE_UNQUOTED([PACKAGE_SOURCE_DIR], ["${packagesrcdir}"], [PACKAGE_SOURCE_DIR])

dnl Use -Wall if we have gcc.
changequote(,)dnl
if test "x$GCC" = "xyes"; then
  case " $CFLAGS " in
  *[\ \	]-Wall[\ \	]*) ;;
  *) CFLAGS="$CFLAGS -Wall" ;;
  esac
fi
changequote([,])dnl

CFLAGS="-O2 -Wall"


XML2_CFLAGS=`xml2-config --cflags`
AC_SUBST(XML2_CFLAGS)

case "$ABI" in
    x86) ARC=32;;
    amd64) ARC=64;;
    *) ARC=`getconf LONG_BIT`;;
esac
AC_SUBST(ARC)

AC_CONFIG_FILES([
Makefile
src/Makefile
include/Makefile
include/cncl/Makefile
include/misc/Makefile
po/Makefile.in
])
AC_OUTPUT
