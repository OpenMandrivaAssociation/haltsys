%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	Tool to halt LTSP terminals
Name:		haltsys
Version:	0.2
Release:	7
License:	GPL
Group:		System/Libraries
URL:		http://www.ltsp.org
Source0:	http://www.ltsp.org/tarballs/%{name}-%{version}.tar.bz2
BuildRequires:	dietlibc-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdv2011.0
+ Revision: 619328
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-5mdv2010.0
+ Revision: 429383
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2009.0
+ Revision: 267071
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-3mdv2009.0
+ Revision: 217540
- rebuilt against dietlibc-devel-0.32

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2-2mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2007.0
+ Revision: 133029
- use dietlibc instead

* Wed Feb 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2007.1
+ Revision: 117135
- fix deps
- second build attempt
- Import haltsys

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdk
- initial Mandriva package (mille-xterm import)

