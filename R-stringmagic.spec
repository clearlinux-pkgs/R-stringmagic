#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-stringmagic
Version  : 1.1.1
Release  : 4
URL      : https://cran.r-project.org/src/contrib/stringmagic_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/stringmagic_1.1.1.tar.gz
Summary  : Character String Operations and Interpolation, Magic Edition
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-stringmagic-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# stringmagic
The purpose of `stringmagic` is to facilitate the manipulation of character strings.

%package lib
Summary: lib components for the R-stringmagic package.
Group: Libraries

%description lib
lib components for the R-stringmagic package.


%prep
%setup -q -n stringmagic
pushd ..
cp -a stringmagic buildavx2
popd
pushd ..
cp -a stringmagic buildavx512
popd
pushd ..
cp -a stringmagic buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1714065921

%install
export SOURCE_DATE_EPOCH=1714065921
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/stringmagic/DESCRIPTION
/usr/lib64/R/library/stringmagic/INDEX
/usr/lib64/R/library/stringmagic/Meta/Rd.rds
/usr/lib64/R/library/stringmagic/Meta/features.rds
/usr/lib64/R/library/stringmagic/Meta/hsearch.rds
/usr/lib64/R/library/stringmagic/Meta/links.rds
/usr/lib64/R/library/stringmagic/Meta/nsInfo.rds
/usr/lib64/R/library/stringmagic/Meta/package.rds
/usr/lib64/R/library/stringmagic/Meta/vignette.rds
/usr/lib64/R/library/stringmagic/NAMESPACE
/usr/lib64/R/library/stringmagic/NEWS.md
/usr/lib64/R/library/stringmagic/R/stringmagic
/usr/lib64/R/library/stringmagic/R/stringmagic.rdb
/usr/lib64/R/library/stringmagic/R/stringmagic.rdx
/usr/lib64/R/library/stringmagic/doc/guide_customization.R
/usr/lib64/R/library/stringmagic/doc/guide_customization.html
/usr/lib64/R/library/stringmagic/doc/guide_customization.rmd
/usr/lib64/R/library/stringmagic/doc/guide_string_magic.R
/usr/lib64/R/library/stringmagic/doc/guide_string_magic.html
/usr/lib64/R/library/stringmagic/doc/guide_string_magic.rmd
/usr/lib64/R/library/stringmagic/doc/guide_string_tools.R
/usr/lib64/R/library/stringmagic/doc/guide_string_tools.html
/usr/lib64/R/library/stringmagic/doc/guide_string_tools.rmd
/usr/lib64/R/library/stringmagic/doc/index.html
/usr/lib64/R/library/stringmagic/doc/ref_operations.R
/usr/lib64/R/library/stringmagic/doc/ref_operations.html
/usr/lib64/R/library/stringmagic/doc/ref_operations.rmd
/usr/lib64/R/library/stringmagic/doc/ref_regex_flags.R
/usr/lib64/R/library/stringmagic/doc/ref_regex_flags.html
/usr/lib64/R/library/stringmagic/doc/ref_regex_flags.rmd
/usr/lib64/R/library/stringmagic/doc/ref_regex_logic.R
/usr/lib64/R/library/stringmagic/doc/ref_regex_logic.html
/usr/lib64/R/library/stringmagic/doc/ref_regex_logic.rmd
/usr/lib64/R/library/stringmagic/doc/ref_string_magic_special_operations.R
/usr/lib64/R/library/stringmagic/doc/ref_string_magic_special_operations.html
/usr/lib64/R/library/stringmagic/doc/ref_string_magic_special_operations.rmd
/usr/lib64/R/library/stringmagic/help/AnIndex
/usr/lib64/R/library/stringmagic/help/aliases.rds
/usr/lib64/R/library/stringmagic/help/figures/argument.png
/usr/lib64/R/library/stringmagic/help/figures/example-argument.png
/usr/lib64/R/library/stringmagic/help/figures/example-options.png
/usr/lib64/R/library/stringmagic/help/figures/example-simple_operation.png
/usr/lib64/R/library/stringmagic/help/figures/operation-template.png
/usr/lib64/R/library/stringmagic/help/figures/options.png
/usr/lib64/R/library/stringmagic/help/paths.rds
/usr/lib64/R/library/stringmagic/help/stringmagic.rdb
/usr/lib64/R/library/stringmagic/help/stringmagic.rdx
/usr/lib64/R/library/stringmagic/html/00Index.html
/usr/lib64/R/library/stringmagic/html/R.css
/usr/lib64/R/library/stringmagic/tests/_tests/pluralization_tests.R
/usr/lib64/R/library/stringmagic/tests/_tests/string_magic_tests.R
/usr/lib64/R/library/stringmagic/tests/_tests/string_tools_tests.R
/usr/lib64/R/library/stringmagic/tests/stringmagic_tests.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/stringmagic/libs/stringmagic.so
/V4/usr/lib64/R/library/stringmagic/libs/stringmagic.so
/VA/usr/lib64/R/library/stringmagic/libs/stringmagic.so
/usr/lib64/R/library/stringmagic/libs/stringmagic.so
