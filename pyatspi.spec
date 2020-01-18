%global debug_package %{nil}

Name:           pyatspi
Version:        2.26.0
Release:        3%{?dist}
Summary:        Python bindings for at-spi

Group:          Development/Languages
License:        LGPLv2 and GPLv2
URL:            http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
#VCS: git:git://git.gnome.org/pyatspi
Source0:        http://download.gnome.org/sources/pyatspi/2.26/%{name}-%{version}.tar.xz

BuildRequires:  python2-devel
# For tests
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.7.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0.0
BuildRequires:  pkgconfig(atk) >= 2.11.2
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.10.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.1
BuildRequires:  python-dbus
BuildRequires:  python-enum34

%if !0%{?rhel}
BuildRequires:  python3-devel
BuildRequires:  python3-dbus
%endif

BuildArch:      noarch

%global _description\
at-spi allows assistive technologies to access GTK-based\
applications. Essentially it exposes the internals of applications for\
automation, so tools such as screen readers, magnifiers, or even\
scripting interfaces can query and interact with GUI controls.\
\
This package includes a python2 client library for at-spi.\


%description %_description

%package -n python2-pyatspi
Summary: %summary
Requires:       at-spi2-core
Requires:       python-gobject
%{?python_provide:%python_provide python2-pyatspi}
# Remove before F30
Provides: pyatspi%{?_isa} = %{version}-%{release}
Obsoletes: pyatspi < %{version}-%{release}

%description -n python2-pyatspi %_description

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
%autosetup -p1

%if !0%{?rhel}
# Make a copy of the source tree for building the python3 module
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
# Build the python2 module
%configure --with-python=python2 --enable-tests
make

%if !0%{?rhel}
# Build the python3 module
pushd %{py3dir}
%configure --with-python=python3 --enable-tests
make
popd
%endif


%install
%make_install

%if !0%{?rhel}
pushd %{py3dir}
%make_install
popd

# Fix up the shebang for python3 example
cp -a examples python3-examples
sed -i '1s|^#!/usr/bin/python|#!%{__python3}|' python3-examples/magFocusTracker.py
%endif

%check
# Done by the 'build' step, with --enable-tests


%files -n python2-pyatspi
%license COPYING COPYING.GPL
%doc AUTHORS README
%doc examples/magFocusTracker.py
%{python2_sitelib}/pyatspi/

%if !0%{?rhel}
%files -n python3-pyatspi
%license COPYING COPYING.GPL
%doc AUTHORS README
%doc python3-examples/magFocusTracker.py
%{python3_sitelib}/pyatspi/
%endif


%changelog
* Mon Jun 11 2018 Ray Strode <rstrode@redhat.com> - 2.26.0-3
- Require python-gobject instead of python2-gobject
  Related: #1569757

* Wed Jun 06 2018 Richard Hughes <rhughes@redhat.com> - 2.26.0-2
- Update to 2.26.0
- Resolves: #1569757

* Tue Jan 17 2017 Kalev Lember <klember@redhat.com> - 2.20.3-1
- Update to 2.20.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 09 2016 Kalev Lember <klember@redhat.com> - 2.20.2-1
- Update to 2.20.2

* Wed Apr 13 2016 Kalev Lember <klember@redhat.com> - 2.20.1-1
- Update to 2.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 2.19.91-1
- Update to 2.19.91

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 2.17.90-1
- Update to 2.17.90
- Use make_install macro

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 2.16.0-1
- Update to 2.16.0
- Use license macro for the COPYING files

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 2.15.90-1
- Update to 2.15.90

* Tue Feb 03 2015 Richard Hughes <rhughes@redhat.com> - 2.15.4-1
- Update to 2.15.4

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 2.14.0-1
- Update to 2.14.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 2.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Kalev Lember <kalevlember@gmail.com> - 2.12.0-1
- Update to 2.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 2.11.92-1
- Update to 2.11.92

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 2.11.90-1
- Update to 2.11.90

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 2.11.3-1
- Update to 2.11.3

* Tue Nov 19 2013 Richard Hughes <rhughes@redhat.com> - 2.11.2-1
- Update to 2.11.2

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Tue Sep 17 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.92-1
- Update to 2.9.92

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.90-1
- Update to 2.9.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.3-1
- Update to 2.9.3

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 2.9.2-1
- Update to 2.9.2

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

* Sun Jan 17 2010 Matthias Clasen <mclasen@redhat.com> - 0.1.5-1
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
