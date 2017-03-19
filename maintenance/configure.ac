#
# Initialize 'autoconf'
#
AC_PREREQ([2.68])

AC_INIT([maintenance], [3.85-2], [no-define])

AC_CONFIG_MACRO_DIRS([m4])

AM_INIT_AUTOMAKE

#
# Initialize CFLAGS early.
# (AC_PROG_CC sets CFLAGS to "-g -O2" if it wasn't already set)
#
CFLAGS="-O2 -Wall"

#
# Check for required programs
#
AC_PROG_CC
AC_PROG_CXX
AC_PROG_INSTALL
AC_PROG_MAKE_SET

#
# Check for header files
#
AC_HEADER_STDC
AC_HEADER_SYS_WAIT
AC_CHECK_HEADERS([arpa/inet.h fcntl.h netdb.h netinet/in.h stdlib.h string.h sys/socket.h unistd.h])

#
# Check for compiler characteristics
#
AC_C_CONST
AC_TYPE_SIZE_T

#
# Search libraries
#
AC_SEARCH_LIBS([strerror],[cposix])

#
# Check for library functions
#
AC_FUNC_FORK
AC_FUNC_MALLOC
AC_CHECK_FUNCS([memset socket strdup strrchr])

#
# Configure paths for GTK+ 2.0, if available.
#
AM_PATH_GTK_2_0(2.0.0, , AC_MSG_ERROR(Cannot find GTK: Is gtk-config in path?))

#
# Templates for autoheader (key, [description])
#
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

#
# Include sed commands to rename installed programs
#
AC_ARG_PROGRAM

#
# Features controlled by configure
#
AC_ARG_ENABLE(libpath)
AC_ARG_ENABLE(uidebug)

#
# Function: Get full expansion of a variable
#
AC_DEFUN([SP_FULL_EXPANSION], [_arg="$1"
  $2=`(_prev=''

    while test "[$]_arg" != "[$]_prev"
    do
      _prev="[$]_arg"                           # Save current value
      eval _arg="\"[$]_arg\""                   # Evaluate again
    done

    echo "[$]_arg")`
])

if test "x${datadir}" = "xNONE"; then
  SP_FULL_EXPANSION(["${datarootdir}"], [pkgdatadir])
fi

if test "x${program_suffix}" = "xNONE"; then
  program_suffix="mp230"
  program_transform_name="s,\$\$,${program_suffix},;"
fi

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

if test "x${enable_uidebug}" = "xyes"; then
  UI_DFLAGS=-D_PRINTUI_DEBUG_
fi
AC_SUBST(UI_DFLAGS)

if test "x${enable_libpath}" = "x"; then
  enable_libpath="/usr/lib/bjlib"
fi

AC_DEFINE_UNQUOTED([XBJLIBPATH], ["${enable_libpath}"], [XBJLIBPATH])
AC_SUBST(XBJLIBPATH)

#
# Set PACKAGE_LOCALE_DIR in config.h
#
if test "x${datadir}" = "xNONE"; then
  AC_DEFINE_UNQUOTED([PACKAGE_LOCALE_DIR], "[${pkgdatadir}/locale"])
else
  AC_DEFINE_UNQUOTED([PACKAGE_LOCALE_DIR], ["${datadir}/locale"], [PACKAGE_LOCALE_DIR])
fi

#
# Set PACKAGE_DATA_DIR in config.h
#
if test "x${datadir}" = "xNONE"; then
  AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${pkgdatadir}/${PACKAGE}${CNIJ_MODEL}"], [PACKAGE_DATA_DIR])
  else
  AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${datadir}/${PACKAGE}${CNIJ_MODEL}"], [PACKAGE_DATA_DIR])
fi

#
# Set PACKAGE_SOURCE_DIR in config.h
#
packagesrcdir=`cd $srcdir && pwd`
AC_DEFINE_UNQUOTED([PACKAGE_SOURCE_DIR], ["${packagesrcdir}"], [PACKAGE_SOURCE_DIR])

XML2_CFLAGS=`xml2-config --cflags`
AC_SUBST(XML2_CFLAGS)

ARC=`getconf LONG_BIT`
AC_SUBST(ARC)

#
# Enable i18n
#
GETTEXT_PACKAGE=maintenance${program_suffix}

AC_DEFINE_UNQUOTED([GETTEXT_PACKAGE], ["${GETTEXT_PACKAGE}"], [GETTEXT_PACKAGE])
AC_SUBST(GETTEXT_PACKAGE)

ALL_LINGUAS="cs da de el es fi fr hu it ja ko nl nb pl pt ru sv th tr zh zh_TW id"

AM_GLIB_GNU_GETTEXT

#
# Files to be generated
#
AC_CONFIG_HEADERS([config.h])

AC_CONFIG_FILES([
  Makefile
  src/Makefile
  include/Makefile
  include/cncl/Makefile
  include/misc/Makefile
  po/Makefile.in
])

AC_OUTPUT
