%global           _enable_debug_package 0
%global           debug_package %{nil}
%global           __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:		libshp1
Version:	1.2.10
Release:	11.2
Source:		shapelib-%{version}.tar.bz2
Summary:	API for Shapefile Handling - library file
Patch1:		shapelib-endian-destdir-combined.diff
Patch2:		shapelib-fix-contrib.diff
URL:		http://shapelib.maptools.org/
Group:		Applications/GIS
License:	LGPL/MIT
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
BuildRequires:	make gcc autoconf automake libtool
BuildRequires:	proj-devel
# disable build checks detecting errors in the source code


%description
The Shapefile C Library provides the ability to write simple C programs for
reading, writing and updating (to a limited extent) ESRI Shapefiles, and the
associated attribute file (.dbf).

This package contains the dynamic link library for shapelib project.

%package -n libshp-devel
Summary:	Development Environment for %{name}
Group:		Development/Libraries/C and C++
Requires:	%{name} = %{version}
Requires:	proj-devel

%package -n shapelib
Summary:	API for Shapefile Handling
Group:		Applications/GIS

%description -n libshp-devel
The Shapefile C Library provides the ability to write simple C programs for
reading, writing and updating (to a limited extent) ESRI Shapefiles, and the
associated attribute file (.dbf).

This package contains the development Environment for shapelib project.

%description -n shapelib
The Shapefile C Library provides the ability to write simple C programs for
reading, writing and updating (to a limited extent) ESRI Shapefiles, and the
associated attribute file (.dbf).

This package contains the executable programs

%prep
%setup -q -n shapelib-%{version}
%patch1
%patch2
#%{?suse_update_libdir:%{suse_update_libdir}}

%build
%__make libdir="%{_libdir}" CFLAGS="%{optflags}" lib all
pushd contrib
%__make libdir="%{_libdir}" EXTRACFLAGS="%{optflags}"
popd

%install
%__make bindir="%{buildroot}%{_bindir}" libdir="%{buildroot}%{_libdir}" includedir="%{buildroot}%{_includedir}" install
pushd contrib
%__make bindir="%{buildroot}%{_bindir}" libdir="%{buildroot}%{_libdir}" includedir="%{buildroot}%{_includedir}" install
popd

#%__sed -i.bak -e 's/^installed=no/installed=yes/' "%{buildroot}%{_libdir}/libshp.la" \
#&& %__rm "%{buildroot}%{_libdir}/libshp.la.bak"

%clean
%__rm -rf "%{buildroot}"

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -n shapelib
%defattr(-,root,root)
%attr(0644,root,root) %doc ChangeLog dbf_api.html LICENSE.LGPL README
%doc makeshape.sh
%{_bindir}/dbfadd
%{_bindir}/dbfcat
%{_bindir}/dbfcreate
%{_bindir}/dbfdump
%{_bindir}/dbfinfo
%{_bindir}/shpadd
%{_bindir}/shpcat
%{_bindir}/shpcentrd
%{_bindir}/shpcreate
%{_bindir}/shpdata
%{_bindir}/shpdump
%{_bindir}/shpdxf
%{_bindir}/shpfix
%{_bindir}/shpinfo
%{_bindir}/shpproj
%{_bindir}/shptest
%{_bindir}/shpwkb

%files
%defattr(-,root,root)
%{_libdir}/libshp.so.*

%files  -n libshp-devel
%defattr(-,root,root)
%{_includedir}/libshp
%{_libdir}/libshp.so
%exclude %{_libdir}/libshp.la
%{_libdir}/libshp.a

%changelog
* Mon Jul 21 2008 Dirk Stöcker <opensuse@dstoecker.de> 1.2.10
- some BuildService and rpmlint fixes
* Wed Jan 11 2006 Pascal Bleser 1.2.10
- added fixing of libshp.la file ("installed=no" -> "installed=yes")
* Wed Jan 11 2006 Pascal Bleser 1.2.10
- new package
