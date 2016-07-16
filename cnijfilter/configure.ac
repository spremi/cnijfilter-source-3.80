dnl Process this file with autoconf to produce a configure script.

AC_INIT(cif, 3.80-1, no-define)

AM_INIT_AUTOMAKE

AH_TEMPLATE([PACKAGE])
AH_TEMPLATE([VERSION])
AH_TEMPLATE([XBJLIBPATH])
AH_TEMPLATE([XBINPATH])

if test "${program_suffix}" = "NONE"; then
  program_suffix="mg6300"
  program_transform_name="s,\$\$,${program_suffix},;"
fi

AC_ARG_ENABLE(libpath)
if test "${enable_libpath}" = ""; then
  enable_libpath="/usr/lib/bjlib"
fi

AC_DEFINE_UNQUOTED([XBJLIBPATH], ["${enable_libpath}"], [XBJLIBPATH])
AC_SUBST(XBJLIBPATH)


AC_ARG_ENABLE(binpath)
if test "${enable_binpath}" = ""; then
  enable_binpath="/usr/local/bin"
fi

AC_DEFINE_UNQUOTED([XBINPATH], ["${enable_binpath}"], [XBINPATH])
AC_SUBST(XBINPATH)


AM_CONFIG_HEADER(config.h)

dnl Checks for programs.
AC_ISC_POSIX

case "${program_suffix}" in
  mg6300) CNCL_LIB_ID=408;;
  mg5400) CNCL_LIB_ID=407;;
  ip7200) CNCL_LIB_ID=406;;
  mg4200) CNCL_LIB_ID=405;;
  mg3200) CNCL_LIB_ID=404;;
  e510) CNCL_LIB_ID=403;;
  mg2200) CNCL_LIB_ID=402;;
  mp230) CNCL_LIB_ID=401;;
  CN_IJ_MODEL) CNCL_LIB_ID=CN_IJ_MODEL_NUM;;
esac
AC_SUBST(CNCL_LIB_ID)

ARC=`getconf LONG_BIT`
AC_SUBST(ARC)

AC_PROG_CC
AM_PROG_CC_STDC

dnl Checks for libraries.

dnl Checks for header files.
AC_HEADER_STDC
AC_HEADER_SYS_WAIT
AC_CHECK_HEADERS(unistd.h)

dnl Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_SIZE_T

dnl OPTION
CFLAGS="-O2"

dnl Checks for library functions.
AC_CHECK_FUNCS(socket)

AC_OUTPUT([
Makefile
src/Makefile
include/Makefile
include/cncl/Makefile
include/misc/Makefile
])