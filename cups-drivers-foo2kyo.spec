%define rname foo2kyo

Summary:	Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux
Name:		cups-drivers-%{rname}
Version:	0.1.0a
Release:	%mkrel 13
Group:		System/Printing
License:	GPL
URL:		http://sourceforge.net/projects/kyo-fs1016mfp/
Source0:	http://downloads.sourceforge.net/kyo-fs1016mfp/%{rname}-%{version}.tar.bz2
Source1:	foo2kyo-cups.tar.bz2
Requires:	cups
Requires:	foomatic-db-engine
BuildRequires:	jbig-devel
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux.

This package contains foomatic and cups Drivers for the Kyocera Mita FS-1016
MFP.

%prep

%setup -q -n %{rname} -a1

perl -p -i -e 's/Kyocera-Mita-FS-1016/Kyocera-FS-1016/g' foomatic-db/driver/foo2kyo.xml

# fix attribs
chmod 644 COPYING

%build

gcc %{optflags} %{ldflags} -o foo2kyo foo2kyo.c -ljbig

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/foomatic/db/source/{driver,opt,printer}
install -d %{buildroot}%{_datadir}/cups/model/%{rname}

install -m0755 foo2kyo %{buildroot}%{_bindir}
install -m0755 foo2kyo-wrapper %{buildroot}%{_bindir}

for dir in driver opt printer; do
    install -c -m0644 foomatic-db/$dir/*.xml %{buildroot}%{_datadir}/foomatic/db/source/$dir/
done

install -m0644 ppd/Kyocera-FS-1016MFP-foo2kyo.ppd %{buildroot}%{_datadir}/cups/model/%{rname}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING
%attr(0755,root,root) %{_bindir}/foo2kyo
%attr(0755,root,root) %{_bindir}/foo2kyo-wrapper
%attr(0644,root,root) %{_datadir}/foomatic/db/source/opt/*.xml
%attr(0644,root,root) %{_datadir}/foomatic/db/source/printer/*.xml
%attr(0644,root,root) %{_datadir}/foomatic/db/source/driver/*.xml
%attr(0755,root,root) %dir %{_datadir}/cups/model/%{rname}
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Kyocera-FS-1016MFP-foo2kyo.ppd*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-11mdv2011.0
+ Revision: 663435
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-10mdv2011.0
+ Revision: 603867
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-9mdv2010.1
+ Revision: 518839
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-8mdv2010.0
+ Revision: 413283
- rebuild

* Sat Jan 31 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-7mdv2009.1
+ Revision: 335836
- rebuilt against new jbigkit major

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-6mdv2009.1
+ Revision: 318057
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0a-5mdv2009.0
+ Revision: 220525
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0a-4mdv2008.1
+ Revision: 149145
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-3mdv2008.0
+ Revision: 75324
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-2mdv2008.0
+ Revision: 64145
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-1mdv2008.0
+ Revision: 62497
- Import cups-drivers-foo2kyo



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.0a-1mdv2008.0
- initial Mandriva package
