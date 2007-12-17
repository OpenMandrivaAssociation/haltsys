%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Tool to halt LTSP terminals
Name:		haltsys
Version:	0.2
Release:	%mkrel 2
License:	GPL
Group:		System/Libraries
URL:		http://www.ltsp.org
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	dietlibc-devel

%description
This program is used in LTSP to halt the terminals.

%prep

%setup -q -n %{name}

%build

diet gcc -Os -o %{name} %{name}.c

%install
rm -rf %{buildroot}

install -d %{buildroot}/sbin
install -m0755 haltsys %{buildroot}/sbin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%attr(0755,root,root) /sbin/haltsys


