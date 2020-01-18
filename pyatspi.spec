%global debug_package %{nil}

Name:           pyatspi
Version:        2.8.0
Release:        3%{?dist}
Summary:        Python bindings for at-spi

Group:          Development/Languages
License:        LGPLv2 and GPLv2
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
#VCS: git:git://git.gnome.org/pyatspi
Source0:        http://download.gnome.org/sources/pyatspi/2.8/%{name}-%{version}.tar.xz

BuildRequires:  python2-devel
%if !0%{?rhel}
BuildRequires:  python3-devel
%endif
BuildRequires:  pygobject3-devel >= 2.90.1

Requires:       at-spi2-core
Requires:       pygobject3

BuildArch:      noarch

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python2 client library for at-spi.


%if !0%{?rhel}
%package -n python3-pyatspi
Summary:        Python3 bindings for at-spi
Requires:       at-spi2-core
Requires:       python3-gobject

%description -n python3-pyatspi
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.
%endif


%prep
%setup -q

%if !0%{?rhel}
# Make a copy of the source tree for building the python3 module
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
# Build the python2 module
%configure --with-python=python2
make

%if !0%{?rhel}
# Build the python3 module
pushd %{py3dir}
%configure --with-python=python3
make
popd
%endif


%install
make install DESTDIR=$RPM_BUILD_ROOT

%if !0%{?rhel}
pushd %{py3dir}
make install DESTDIR=$RPM_BUILD_ROOT
popd

# Fix up the shebang for python3 example
cp -a examples python3-examples
sed -i '1s|^#!/usr/bin/python|#!%{__python3}|' python3-examples/magFocusTracker.py
%endif


%files
%doc COPYING COPYING.GPL AUTHORS README
%doc examples/magFocusTracker.py
%{python_sitelib}/pyatspi/

%if !0%{?rhel}
%files -n python3-pyatspi
%doc COPYING COPYING.GPL AUTHORS README
%doc python3-examples/magFocusTracker.py
%{python3_sitelib}/pyatspi/
%endif


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.8.0-3
- Mass rebuild 2013-12-27

* Mon Apr 15 2013 Rui Matos <rmatos@redhat.com> - 2.8.0-2
- Don't depend on python3 in RHEL

* Mon Mar 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.8.0-1
- Update to 2.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.91-1
- Update to 2.7.91

* Sat Feb 23 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.5-2
- Build python3-pyatspi with Python 3 support

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 2.7.5-1
- Update to 2.7.5

* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 2.7.1-1
- Update to 2.7.1
- Include magFocusTracker.py example in documentation

* Wed Jul 18 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.4-1
- Update to 2.5.4
- Removed python_sitelib definition; no longer needed with recent rpmbuild

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.3-1
- Update to 2.5.3

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Wed Mar 28 2012 Richard Hughes <hughsient@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 2.3.92-1
- Update to 2.3.92

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 2.3.91-1
- Update to 2.3.91

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 2.3.5-1
- Update to 2.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 2.3.4-1
- Update to 2.3.4

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Wed Sep 28 2011 Matthias Clasen <mclasen@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 2.1.91-1
- Update to 2.1.91

* Mon Jul 25 2011 Matthias Clasen <mclasen@redhat.com> - 2.1.4-1
- Update to 2.1.4

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.1.2-1
- Update to 2.1.2

* Wed May 11 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.92-1
- Update to 1.91.92

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.91-1
- Update to 1.91.91

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.90-1
- Update to 1.91.90

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Christopher Aillon <caillon@redhat.com> - 1.91.6-1
- Update to 1.91.6

* Tue Jan 11 2011 Matthias Clasen <mclasen@redhat.com> - 1.91.5-1
- Update to 1.91.5

* Thu Dec  2 2010 Matthias Clasen <mclasen@redhat.com> - 1.91.3-1
- Update to 1.91.3

* Tue Oct  5 2010 Matthias Clasen <mclasen@redhat.com> - 1.91.0-1
- Update to 1.91.0

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Mon Sep 20 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.91-2
- Require python-xlib and and gnome-python2-gconf (#635484)

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.91-1
- Update to 0.3.91

* Wed Aug 18 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.90-1
- Update to 0.3.90

* Mon Aug  2 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.6-1
- Update to 0.3.6

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.4-1
- Update to 0.3.4

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.3-1
- Update to 0.3.3

* Fri May 28 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.2-1
- Update to 0.3.2

* Sat May 15 2010 Matthias Clasen <mclasen@redhat.com> - 0.3.1.1-1
- Update to 0.3.1.1

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.8-1
- Update to 0.1.8

* Sat Feb 20 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.7-1
- Update to 0.1.7

* Wed Feb 10 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Wed Feb  3 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.5-2
- Relocate

* Sun Jan 16 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.5-1
- Update to 0.1.5

* Thu Jan  7 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.4-3
- Incorporate review feedback

* Thu Jan  7 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.4-2
- Fix License field
- Change CORBA/DBus switching method

* Tue Dec 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.4-1
- Update to 0.1.4

* Sat Dec  5 2009 Matthias Clasen <mclasen@redhat.com> - 0.1.3-1
- Initial packaging
