## Process this file with automake to produce Makefile.in

SUBDIRS =  po src

install-data-local:
	@$(NORMAL_INSTALL)
	$(mkinstalldirs) $(DESTDIR)$(pkgdatadir)$(CNIJ_MODEL); \
	$(mkinstalldirs) $(DESTDIR)$(pkgdatadir)$(CNIJ_MODEL)/pixmaps; \
	if test -d $(srcdir)/pixmaps; then \
	  for pixmap in $(srcdir)/pixmaps/*; do \
	    if test -f $$pixmap; then \
	      $(INSTALL_DATA) $$pixmap $(DESTDIR)$(pkgdatadir)$(CNIJ_MODEL)/pixmaps; \
	    fi \
	  done \
	fi

dist-hook:
	mkdir $(distdir); \
	if test -d pixmaps; then \
	  mkdir $(distdir)/pixmaps; \
	  for pixmap in pixmaps/*; do \
	    if test -f $$pixmap; then \
	      cp -p $$pixmap $(distdir)/pixmaps; \
	    fi \
	  done \
	fi
