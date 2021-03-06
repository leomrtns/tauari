AC_INIT([tauari_c], [0.0.1], [leomrtns@gmail.com],[], [https://github.com/quadram-institute-bioscience/tauari])
AC_CONFIG_AUX_DIR([.])

AC_CONFIG_SRCDIR([src/tauari_module.c])
AC_CONFIG_HEADER([src/config.h])
AC_PREFIX_DEFAULT(`pwd`)
dnl libtoolize recomendation
AC_CONFIG_MACRO_DIR([m4])
CFLAGS=${CFLAGS-""}  # Override default O2
CXXFLAGS=${CXXFLAGS-""}

AM_INIT_AUTOMAKE([-Wall -Werror]) # automake initialization (completely unrelated to compiler arguments)
AC_USE_SYSTEM_EXTENSIONS
AM_MAINTAINER_MODE
dnl must be called after AC_USE_SYSTEM_EXTENSIONS (new restriction in autoconf2.68) 
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])

AC_LANG_C
AC_PROG_CC
AC_PROG_INSTALL
AC_GNU_SOURCE # directs the libc header files to provide the standard GNU system interfaces including all GNU extensions
AC_PROG_LIBTOOL # Libtool (for library): in lib/Makefile.am, we include an "abstract" libfoo.la
dnl openMP: sets $OPENMP_CFLAGS which should be passed to CFLAGS, CPPFLAGS; creates preprocessor macro _OPENMP 
dnl         (checked with "ifdef _OPENMP"); user can disable it through "--disable-openmp"
AC_OPENMP
AC_SUBST(OPENMP_CFLAGS)
AC_SUBST(OPENMP_CPPFLAGS)
PKG_CHECK_MODULES([ZLIB], [zlib])
AM_PATH_PYTHON([3.6]) # for pyexecdir, pyexec 
PKG_CHECK_MODULES([PYTHON], [python3]) # AC_SEARCH_LIBS() and AC_CHECK_HEADERS() in one go, provided pkg-config understands it 

AC_MSG_RESULT([ ===  configuration options specific to $PACKAGE_NAME]) # library checks (math etc.) are done by biomcmc-lib

AC_MSG_CHECKING([whether to build (slower) debug code])
AC_ARG_ENABLE([debug], [AS_HELP_STRING([--enable-debug], [enable debugging with gdb and friends (default=no)])],[debugit="$enableval"], [debugit=no])
AC_MSG_RESULT([$debugit])
if test x"$debugit" = x"yes"; then
  AC_DEFINE([BIOMCMC_DEBUG],[],[Debug Mode, with assert()-like error checking])
  AM_CFLAGS="${AM_CFLAGS} -g -W -pg -Wall -Werror -Wno-uninitialized -O0 -std=gnu11"
else
  AC_DEFINE([NDEBUG],[],[not in debug mode, disabling all assert() macros])
  AM_CFLAGS="${AM_CFLAGS} -funroll-loops -fomit-frame-pointer -finline-functions -O4 -std=gnu11"
fi

AC_MSG_CHECKING([whether you want static binaries])
AC_ARG_ENABLE(static-binary,
    [  --enable-static-binary  static binaries, that run on same arch without the libraries [[default=no]]],
    [ statbin_use="yes" ], [ statbin_use=""    ])
if test -n "${statbin_use}"; then
    AC_MSG_RESULT([yes])
    AM_LDFLAGS="-static ${AM_LDFLAGS}";
else
    AC_MSG_RESULT([no])
fi

AC_MSG_RESULT([ ===  end of specific configuration options])

dnl propagate changed vars among final makefiles
AC_SUBST([AM_CFLAGS])
AC_SUBST([AM_LDFLAGS])
AC_SUBST([MPI_CXXLIBS])
AC_SUBST([MPI_CXXFLAGS])

dnl better solution would be to allow arbitrary location for biomcmc-lib (it relies on ln)
AC_CHECK_FILE([${srcdir}/build_setup/biomcmc-lib],[],[ln -s submodules/biomcmc-lib ${srcdir}/build_setup/biomcmc-lib])
AC_CHECK_FILE([${srcdir}/build_setup/biomcmc-lib/configure.ac],[], [AC_MSG_ERROR(["biomcmc-lib submodule missing, please git clone --recursive or link by hand to location of source code"])])
dnl Call biomcmc-lib ./configure script recursively.
AC_CONFIG_SUBDIRS([build_setup/biomcmc-lib])
AC_SUBST([BIOMCMCLIB], [build_setup/biomcmc-lib])
dnl generate makefiles (last recipes, after defining CFLAGS etc.)
AC_CONFIG_FILES([ Makefile src/Makefile])
AC_OUTPUT

echo \
"---- 
Configuration parameters for $PACKAGE_NAME-$PACKAGE_VERSION:

 Source code location:   ${srcdir}
 Compiler     (library): ${CC}
 Compiler flags: ${AM_CFLAGS} 
 Linker  flags:  ${AM_LDFLAGS}
 Install path:   ${prefix}
----"
