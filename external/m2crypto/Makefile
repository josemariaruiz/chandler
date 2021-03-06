
VERSION=310
RELVER=$(VERSION)-1
SRC=$(BUILD_ROOT)/m2crypto/M2Crypto-$(VERSION)

include $(BUILD_ROOT)/Makefile.inc

BUILD=build_$(SNAP)

apply: patches
	patch -Nup0 < patches || true

ifeq ($(OS),Cygwin)
build: expand apply
	cd $(SRC); \
	$(PYTHON) setup.py \
          build_ext --swig=`cygpath -aw $(SWIG)` \
                    --library-dirs=`cygpath -aw $(BUILD_ROOT)/$(SNAP)/lib` \
                    --include-dirs=`cygpath -aw $(BUILD_ROOT)/$(SNAP)/include` \
          build --build-base=$(BUILD) $(DIST_OPT) \
          install --force
	cp -f $(BUILD_ROOT)/$(SNAP)/bin/libeay32.dll $(BUILD_ROOT)/$(SNAP)/$(SITE)/M2Crypto
	cp -f $(BUILD_ROOT)/$(SNAP)/bin/ssleay32.dll $(BUILD_ROOT)/$(SNAP)/$(SITE)/M2Crypto

# The tests do not run properly with Windows Python (Cygwin would work) since
# we don't have win32process module.
tests:

else
build: expand apply
	cd $(SRC); \
	MACOSX_DEPLOYMENT_TARGET=$(MACOSX_DEPLOYMENT_TARGET) $(PYTHON) setup.py \
          build_ext --swig=$(SWIG) \
                    --library-dirs=$(BUILD_ROOT)/$(SNAP)/lib \
                    --include-dirs=$(BUILD_ROOT)/$(SNAP)/include \
          build --build-base=$(BUILD) $(DIST_OPT) \
          install --force

tests:
	cd $(SRC)/tests; $(PYTHON) alltests.py

endif

M2Crypto-$(VERSION).tar.gz:
	svn export -r $(VERSION) http://svn.osafoundation.org/m2crypto/trunk M2Crypto-$(VERSION)
	tar czf M2Crypto-$(VERSION).tar.gz M2Crypto-$(VERSION)

sources: M2Crypto-$(VERSION).tar.gz

M2Crypto-$(VERSION)-expanded: M2Crypto-$(VERSION).tar.gz
	touch M2Crypto-$(VERSION)-expanded

expand: M2Crypto-$(VERSION)-expanded

snap: 
	cd $(BUILD_ROOT); \
	find $(SNAP)/$(SITE)/M2Crypto -name "*.pyc" | xargs rm -f; \
	find $(SNAP)/$(SITE)/M2Crypto -name "*.pyo" | xargs rm -f; \
	tar -cvzf $(BUILD_ROOT)/m2crypto/m2crypto-$(SNAP)-$(RELVER).tar.gz \
		$(SNAP)/$(SITE)/M2Crypto; \
	$(MD5) $(BUILD_ROOT)/m2crypto/m2crypto-$(SNAP)-$(RELVER).tar.gz > $(BUILD_ROOT)/m2crypto/m2crypto-$(SNAP)-$(RELVER).tar.gz.md5

install: m2crypto-$(SNAP)-$(RELVER).tar.gz
	tar -C $(CHANDLERBIN) -xvzf m2crypto-$(SNAP)-$(RELVER).tar.gz

upload: m2crypto-$(SNAP)-$(RELVER).tar.gz
	scp m2crypto-$(SNAP)-$(RELVER).tar.gz $(UPLOAD)
	scp m2crypto-$(SNAP)-$(RELVER).tar.gz.md5 $(UPLOAD)

clean:
	rm -rf  $(SRC)/$(BUILD)
