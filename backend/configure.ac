#
# Initialize 'autoconf'
#
AC_PREREQ([2.68])

AC_INIT([backend], [3.85-2], [no-define])

AC_CONFIG_MACRO_DIRS([m4])

AM_INIT_AUTOMAKE

#
# Initialize 'libtool'
#
LT_PREREQ([2.4.6])

LT_INIT

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
# Check for libraries
#
AC_CHECK_LIB([cups], [main])      # FIXME: Replace `main' with a function in `-lcups'

#
# Check for library functions
#
AC_FUNC_FORK
AC_FUNC_MALLOC
AC_CHECK_FUNCS([memset socket strdup strrchr])

#
# Templates for autoheader (key, [description])
#
AH_TEMPLATE([PROG_PATH])

#
# Features controlled by configure
#
AC_ARG_ENABLE(progpath)

if test "x${enable_progpath}" = "x" ; then
   enable_progpath="${ac_default_prefix}/bin"
fi

AC_DEFINE_UNQUOTED([PROG_PATH], ["${enable_progpath}"], [PROG_PATH])
AC_SUBST(PROG_PATH)

#
# Files to be generated
#
AC_CONFIG_HEADERS([config.h])

AC_CONFIG_FILES([
  Makefile
  src/Makefile
])

AC_OUTPUT
