AC_INIT([backend],[3.85-2],[no-define])

AM_INIT_AUTOMAKE

AC_CONFIG_MACRO_DIRS([m4])

AM_CONFIG_HEADER(config.h)

AH_TEMPLATE([PROG_PATH])

AC_ARG_ENABLE(progpath)
if test "x${enable_progpath}" = "x" ; then
   enable_progpath="${ac_default_prefix}/bin"
fi

AC_DEFINE_UNQUOTED([PROG_PATH], ["${enable_progpath}"], [PROG_PATH])
AC_SUBST(PROG_PATH)

# Checks for programs.
AC_PROG_CXX
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_MAKE_SET
LT_INIT

# Checks for libraries.
# FIXME: Replace `main' with a function in `-lcups':
AC_CHECK_LIB([cups], [main])

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

AC_CONFIG_FILES([Makefile
src/Makefile])
AC_OUTPUT
