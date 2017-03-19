#
# Initialize 'autoconf'
#
AC_PREREQ([2.68])

AC_INIT([lgmon], [3.85-2], [no-define])

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
AC_PROG_INSTALL
AC_PROG_MAKE_SET
AC_PROG_RANLIB

#
# Check for header files
#
AC_HEADER_STDC
AC_CHECK_HEADERS([unistd.h])

#
# Check for compiler characteristics
#
AC_C_CONST
AC_TYPE_SIZE_T

#
# Search libraries
#
AC_SEARCH_LIBS([strerror], [cposix])

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
AH_TEMPLATE([PROG_PATH])

#
# Include sed commands to rename installed programs
#
AC_ARG_PROGRAM

#
# Features controlled by configure
#
AC_ARG_ENABLE(progpath)

if test "x${program_suffix}" = "xNONE"; then
  program_suffix="mg6300"
  program_transform_name="s,\$\$,${program_suffix},;"
fi

AC_DEFINE_UNQUOTED([PACKAGE_PRINTER_MODEL], ["${program_suffix}"], [PACKAGE_PRINTER_MODEL])

if test "x${enable_progpath}" = "x" ; then
   enable_progpath="${ac_default_prefix}/bin"
fi

AC_DEFINE_UNQUOTED([PROG_PATH], ["${enable_progpath}"], [PROG_PATH])
AC_SUBST(PROG_PATH)

case "${program_suffix}" in
  mp230)  CNCL_LIB_ID=401;;
  mg2200) CNCL_LIB_ID=402;;
  e510)   CNCL_LIB_ID=403;;
  mg3200) CNCL_LIB_ID=404;;
  mg4200) CNCL_LIB_ID=405;;
  ip7200) CNCL_LIB_ID=406;;
  mg5400) CNCL_LIB_ID=407;;
  mg6300) CNCL_LIB_ID=408;;
  CN_IJ_MODEL) CNCL_LIB_ID=CN_IJ_MODEL_NUM;;
esac
AC_SUBST(CNCL_LIB_ID)

#
# Set PACKAGE_LOCALE_DIR in config.h
#
if test "x${prefix}" = "xNONE"; then
  AC_DEFINE_UNQUOTED([PACKAGE_LOCALE_DIR], ["${ac_default_prefix}/${DATADIRNAME}/locale"], [PACKAGE_LOCALE_DIR])
else
  AC_DEFINE_UNQUOTED([PACKAGE_LOCALE_DIR], ["${prefix}/${DATADIRNAME}/locale"], [PACKAGE_LOCALE_DIR])
fi

#
# Set PACKAGE_DATA_DIR in config.h
#
if test "x${datadir}" = 'x${prefix}/share'; then
  if test "x${prefix}" = "xNONE"; then
    AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${ac_default_prefix}/share/${PACKAGE}"], [PACKAGE_DATA_DIR])
  else
    AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${prefix}/share/${PACKAGE}"], [PACKAGE_DATA_DIR])
  fi
else
  AC_DEFINE_UNQUOTED([PACKAGE_DATA_DIR], ["${datadir}/${PACKAGE}"], [PACKAGE_DATA_DIR])
fi

#
# Set PACKAGE_SOURCE_DIR in config.h
#
packagesrcdir=`cd $srcdir && pwd`
AC_DEFINE_UNQUOTED([PACKAGE_SOURCE_DIR], ["${packagesrcdir}"], [PACKAGE_SOURCE_DIR])

ARC=`getconf LONG_BIT`
AC_SUBST(ARC)

#
# Files to be generated
#
AC_CONFIG_HEADERS([config.h])

AC_CONFIG_FILES([
  Makefile
  src/Makefile
  include/Makefile
  include/cncl/Makefile
])

AC_OUTPUT
