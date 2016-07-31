dnl Process this file with autoconf to produce a configure script.

AC_INIT([cngpijmon],[3.85-1],[no-define])

AM_INIT_AUTOMAKE

AC_ARG_PROGRAM

AC_ARG_ENABLE(progpath)
if test "x${enable_progpath}" = "x" ; then
   enable_progpath="${ac_default_prefix}/bin"
fi

AC_DEFINE_UNQUOTED([PROG_PATH], ["${enable_progpath}"], [PROG_PATH])
AC_SUBST(PROG_PATH)

if test "x${program_suffix}" = "xNONE"; then
  program_suffix="mg6300"
  program_transform_name="s,\$\$,${program_suffix},;"
fi

AM_CONFIG_HEADER(config.h)

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
AH_TEMPLATE([PROG_PATH])

CNIJ_MODEL=${program_suffix}
AC_SUBST(CNIJ_MODEL)

AC_SEARCH_LIBS([strerror],[cposix])
AC_PROG_CC
AM_PROG_CC_STDC
AC_HEADER_STDC

AM_PATH_GTK_2_0(2.0.0, ,
            AC_MSG_ERROR(Cannot find GTK: Is gtk-config in path?))

GETTEXT_PACKAGE=cngpijmon${program_suffix}
AC_SUBST(GETTEXT_PACKAGE)
dnl AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE,"$GETTEXT_PACKAGE")

dnl Add the languages which your application supports here.
ALL_LINGUAS="cs da de el es fi fr hu it ja ko nl nb pl pt ru sv th tr zh zh_TW id"
AM_GLIB_GNU_GETTEXT

dnl Set PACKAGE_LOCALE_DIR in config.h.
if test "x${prefix}" = "xNONE"; then
  AC_DEFINE_UNQUOTED([PACKAGE_LOCALE_DIR], ["${ac_default_prefix}/${DATADIRNAME}/locale"], [PACKAGE_LOCALE_DIR])
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

CFLAGS="-O2"

dnl Use -Wall if we have gcc.
changequote(,)dnl
if test "x$GCC" = "xyes"; then
  case " $CFLAGS " in
  *[\ \	]-Wall[\ \	]*) ;;
  *) CFLAGS="$CFLAGS -Wall" ;;
  esac
fi
changequote([,])dnl

XML2_CFLAGS=`xml2-config --cflags`
AC_SUBST(XML2_CFLAGS)

AC_CONFIG_FILES([
Makefile
src/Makefile
po/Makefile.in
])
AC_OUTPUT
