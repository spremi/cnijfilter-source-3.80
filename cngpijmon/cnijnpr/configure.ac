AC_INIT([cnijnpr],[3.85-1],[no-define])

AM_INIT_AUTOMAKE

AM_CONFIG_HEADER(config.h)

AH_TEMPLATE([BJLIB_PATH])

AC_ARG_ENABLE(libpath)
if test "x${enable_libpath}" = "x" ; then
   enable_libpath="/usr/lib/bjlib"
fi

AC_DEFINE_UNQUOTED([BJLIB_PATH], ["${enable_libpath}"], [BJLIB_PATH])
AC_SUBST(BJLIB_PATH)


# Checks for programs.
#AC_PROG_CXX
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_MAKE_SET
#AM_PROG_LIBTOOL


# Checks for header files.
AC_HEADER_STDC
AC_HEADER_SYS_WAIT
AC_CHECK_HEADERS([arpa/inet.h fcntl.h netdb.h netinet/in.h stdlib.h string.h sys/socket.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_FORK
AC_FUNC_MALLOC
AC_CHECK_FUNCS([memset socket strdup strrchr])

CFLAGS="-O2"

case "$ABI" in
    x86) ARC=32;;
    amd64) ARC=64;;
    *) ARC=`getconf LONG_BIT`;;
esac
AC_SUBST(ARC)

AC_CONFIG_FILES([Makefile
                 cnijnpr/Makefile])
AC_OUTPUT
