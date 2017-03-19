#
# Initialize 'autoconf'
#
AC_PREREQ([2.68])

AC_INIT([canon.ppd], [3.85-2], [no-define])

AM_INIT_AUTOMAKE

#
# Set name of install program
#
AC_PROG_INSTALL

#
# Features controlled by configure
#
AC_ARG_ENABLE(ppdpath)

if test "x${program_suffix}" = "xNONE"; then
	program_suffix="mp230"
fi
PPD_SUFFIX=${program_suffix}
AC_SUBST(PPD_SUFFIX)

if test "x${enable_ppdpath}" = "x"; then
	enable_ppdpath="${datadir}/cups/model"
fi
XPPDPATH=$enable_ppdpath
AC_SUBST(XPPDPATH)

#
# Files to be generated
#
AC_CONFIG_FILES([Makefile])

AC_OUTPUT
