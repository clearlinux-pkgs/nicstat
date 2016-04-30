#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nicstat
Version  : 1.95
Release  : 9
URL      : https://downloads.sourceforge.net/nicstat/nicstat-1.95.tar.gz
Source0  : https://downloads.sourceforge.net/nicstat/nicstat-1.95.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-2.0
Requires: nicstat-bin
Requires: nicstat-doc
Patch1: nicstat-makefile.patch

%description
===================
nicstat is licensed under the Artistic License 2.0.  You can find a
copy of this license as LICENSE.txt included with the nicstat
distribution, or at http://www.perlfoundation.org/artistic_license_2_0

%package bin
Summary: bin components for the nicstat package.
Group: Binaries

%description bin
bin components for the nicstat package.


%package doc
Summary: doc components for the nicstat package.
Group: Documentation

%description doc
doc components for the nicstat package.


%prep
%setup -q -n nicstat-1.95
%patch1 -p1

%build
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
## make_install_append content
install -p -D -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nicstat

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
