EXTRA_DIST = recipe tauari 
ACLOCAL_AMFLAGS = -I m4
SUBDIRS = @BIOMCMCLIB@ src 
# https://stackoverflow.com/questions/25065337/building-nested-autotools-package-without-installing
install installdirs: SUBDIRS = src # do not install biomcmc-lib (only works with --disable-shared atm) 
