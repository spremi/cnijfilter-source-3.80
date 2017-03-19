#
# Initialize 'autoconf'
#
AC_PREREQ([2.68])

AC_INIT([cif], [3.85-2], [no-define])

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

#
# Check for header files
#
AC_HEADER_STDC
AC_HEADER_SYS_WAIT
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
# Check for library functions
#
AC_FUNC_MALLOC
AC_CHECK_FUNCS([memset socket])

#
# Templates for autoheader (key, [description])
#
AH_TEMPLATE([PACKAGE])
AH_TEMPLATE([VERSION])
AH_TEMPLATE([XBJLIBPATH])
AH_TEMPLATE([XBINPATH])

#
# Features controlled by configure
#
AC_ARG_ENABLE(libpath)
AC_ARG_ENABLE(binpath)

if test "x${enable_libpath}" = "x"; then
  enable_libpath="/usr/lib/bjlib"
fi

AC_DEFINE_UNQUOTED([XBJLIBPATH], ["${enable_libpath}"], [XBJLIBPATH])
AC_SUBST(XBJLIBPATH)

if test "x${enable_binpath}" = "x"; then
  enable_binpath="/usr/local/bin"
fi

AC_DEFINE_UNQUOTED([XBINPATH], ["${enable_binpath}"], [XBINPATH])
AC_SUBST(XBINPATH)

if test "x${program_suffix}" = "xNONE"; then
  program_suffix="mg6300"
  program_transform_name="s,\$\$,${program_suffix},;"
fi

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
])

AC_OUTPUT
