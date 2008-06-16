%define rname foo2kyo

Summary:	Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux
Name:		cups-drivers-%{rname}
Version:	0.1.0a
Release:	%mkrel 5
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

gcc %{optflags} -o foo2kyo foo2kyo.c -ljbig

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
