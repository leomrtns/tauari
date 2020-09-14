AM_CPPFLAGS = $(GTKDEPS_CFLAGS)  @OPENMP_CPPFLAGS@ -I$(top_srcdir)/@BIOMCMCLIB@/lib
AM_CFLAGS = @AM_CFLAGS@  @OPENMP_CFLAGS@ @PYTHON_CFLAGS@
LIBBIOMC_LA = $(top_builddir)/@BIOMCMCLIB@/lib/libbiomcmc_static.la
LDADD = $(LIBBIOMC_LA) $(GTKDEPS_LIBS) $(AM_LDFLAGS) @PYTHON_LIBS@

common_headers =#tauari_module.h 
common_src     = tauari_module.c 

lib_LTLIBRARIES = tauari_c.la   ## change to noinst_LT... if should be linked statically; notice "lib" prefix
#pyexec_LTLIBRARIES = tauari_c.la   # $pyexecdir = directory where Python extension modules (shared libraries) should be installed

tauari_c_la_SOURCES = $(common_headers) $(common_src) 
tauari_c_la_LDFLAGS = -module -shared  # "module" means plugin, o.w. libtools complains about missing "lib" prefix
tauari_c_la_LIBADD = $(LDADD) 
#tauari_c_la_LIBADD = ${LIBBIOMC_LA) 
