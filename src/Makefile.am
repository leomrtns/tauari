AM_CPPFLAGS = $(GTKDEPS_CFLAGS)  @OPENMP_CPPFLAGS@ -I$(srcdir)/../@BIOMCMCLIB@/lib
AM_CFLAGS = @AM_CFLAGS@  @OPENMP_CFLAGS@ @PYTHON_CFLAGS@
LDADD = $(GTKDEPS_LIBS) $(AM_LDFLAGS) @PYTHON_LIBS@ ../biomcmc-lib/lib/libbiomcmc_static.la

common_headers =#tauari_module.h 
common_src     = tauari_module.c 

lib_LTLIBRARIES = libtauari_c.la   ## change to noinst_LT... if should be linked statically; notice "lib" prefix
#pyexec_LTLIBRARIES = tauari_c.la   # $pyexecdir = directory where Python extension modules (shared libraries) should be installed
## make sure all headers are below this subdirectory (be careful with spaces at the end of line!)
#otherincludedir = "$(includedir)/tauari_c"
#otherinclude_HEADERS = config.h $(common_headers)
tauari_c_la_SOURCES = $(common_headers) $(common_src) 
#tauari_c_la_LDFLAGS = -module -avoid-version -shared # "module" means plugin, o.w. libtools complains about missing "lib" prefix
tauari_c_la_LDFLAGS = -module # "module" means plugin, o.w. libtools complains about missing "lib" prefix

