# cnijfilter-source-3.80 (NEW & IMPROVED)

:sunny: Tested working win IP7200 series printer on Fedora 23.

## Motivation
So far, single Window$ machine had served good as 'print-hub' for
my IP7200 series printer. With more Fedora boxes added to the home
network, this dependency had to go.

But, the compatible Linux driver package doesn't build on Fedora 23.
So, decided to take it as a weekend-project.

## Build instructions

The instructions here would work on Fedora.

Equivalent commands could, easily, be derived for other Linux flavors.

### Install dependencies
Install these packages as build dependencies:
```
$ dnf install rpm-build
$ dnf install cups-devel
$ dnf install popt-devel
$ dnf install gtk2-devel
$ dnf install libxml2-devel
$ dnf install libtiff-devel
```

### Get source tree

Clone this repository.
```
$ git clone https://github.com/spremi/cnijfilter-source-3.80.git
```

#### Create source tarball
```
$ git archive --format=tar.gz --prefix=cnijfilter-source-3.85-2/ HEAD > ../cnijfilter-source-3.85-2.tar.gz
```

#### Build RPM

Build RPM packages specific to a printer model. See the original instructions below for details.

For example:
```
$ rpmbuild -tb cnijfilter-source-3.85-2.tar.gz --define="MODEL ip7200" --define="MODEL_NUM 406" --with build_common_package
```

## Original README Contents

### How to build rpm

#### When you build one printer driver package
```
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --define="MODEL [Printer Model Name]" --define="MODEL_NUM [Printer Model ID]" --with build_common_package
```
#### When you build plural printer driver packages
##### step 1)
```
$ rpmbuild -tc cnijfilter-source-X.XX-Y.tar.gz --with prepare_fastbuild
```
##### step 2)
```
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --with fastbuild --define="MODEL [Printer Model Name]" --define="MODEL_NUM [Printer Model ID]" --with build_common_package
```
##### step 3) and after step 3)
```
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --with fastbuild --define="MODEL [Printer Model Name]" --define="MODEL_NUM [Printer Model ID]"

    You can set the following [Printer Model Name]/[Printer Model ID].
        [Printer Model Name]        [Printer Model ID]
    ------------------------------------------------------------------
         mp230                       401
         mg2200                      402
         e510                        403
         mg3200                      404
         mg4200                      405
         ip7200                      406
         mg5400                      407
         mg6300                      408
```

### Example
#### Example for build MP230 package
```
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --define="MODEL MP230" --define="MODEL_NUM 401" --with build_common_package
```

#### Example for build MG2200/E510/MG3200 packages
```
$ rpmbuild -tc cnijfilter-source-X.XX-Y.tar.gz --with prepare_fastbuild
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --with fastbuild --define="MODEL MG2200" --define="MODEL_NUM 402" --with build_common_package
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --with fastbuild --define="MODEL E510" --define="MODEL_NUM 403"
$ rpmbuild -tb cnijfilter-source-X.XX-Y.tar.gz --with fastbuild --define="MODEL MG3200" --define="MODEL_NUM 404"
```
