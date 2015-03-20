%global           _enable_debug_package 0
%global           debug_package %{nil}
%global           __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:             libbson
Version:          1.1.0
Release:          1%{?dist}
Summary:          Libbson Library for Centos 7

Group:            Development/Libraries
License:          PHP/Zend
URL:              https://github.com/mongodb/libbson
Source0:          %{name}.tar.gz
BuildRequires:    gcc >= 4.7.2, cmake >= 2.8.7

%description
Libbson Library for Centos 7

%prep
%setup -qc

%build
cd libbson
./autogen.sh
make

%install
export DONT_STRIP=1
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}/usr/local/share/doc/libbson
%{__mkdir} -p %{buildroot}/usr/local/include/libbson-1.0
%{__mkdir} -p %{buildroot}/usr/local/lib/pkgconfig

%{__install} -c -m 0644 libbson/COPYING libbson/NEWS libbson/README %{buildroot}/usr/local/share/doc/libbson
%{__install} -c -m 0644 libbson/src/bson/bcon.h libbson/src/bson/bson.h libbson/src/bson/bson-atomic.h libbson/src/bson/bson-clock.h libbson/src/bson/bson-compat.h libbson/src/bson/bson-context.h libbson/src/bson/bson-endian.h libbson/src/bson/bson-error.h libbson/src/bson/bson-iter.h libbson/src/bson/bson-json.h libbson/src/bson/bson-keys.h libbson/src/bson/bson-macros.h libbson/src/bson/bson-md5.h libbson/src/bson/bson-memory.h libbson/src/bson/bson-oid.h libbson/src/bson/bson-reader.h libbson/src/bson/bson-string.h libbson/src/bson/bson-types.h libbson/src/bson/bson-utf8.h libbson/src/bson/bson-value.h libbson/src/bson/bson-version.h libbson/src/bson/bson-writer.h libbson/src/bson/bson-stdint.h libbson/src/bson/bson-config.h %{buildroot}/usr/local/include/libbson-1.0
%{__install} -c -m 0644 libbson/src/libbson-1.0.pc %{buildroot}/usr/local/lib/pkgconfig

%files
%defattr(-,root,root,-)
/usr/local/share/doc/libbson/*
/usr/local/include/libbson-1.0/*
/usr/local/lib/pkgconfig

# Cleanup

%clean
rm -rf $RPM_BUILD_ROOT
