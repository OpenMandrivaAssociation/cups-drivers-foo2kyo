%define rname foo2kyo

Summary:	Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux
Name:		cups-drivers-%{rname}
Version:	0.1.0a
Release:	26
Group:		System/Printing
License:	GPLv2
Url:		https://sourceforge.net/projects/kyo-fs1016mfp/
Source0:	http://downloads.sourceforge.net/kyo-fs1016mfp/%{rname}-%{version}.tar.bz2
Source1:	foo2kyo-cups.tar.bz2
BuildRequires:	jbig-devel
Requires:	cups
Requires:	foomatic-db-engine

%description
Printer and scanner drivers for the Kyocera Mita FS-1016 MFP under Linux.

This package contains foomatic and cups Drivers for the Kyocera Mita FS-1016
MFP.

%prep
%setup -qn %{rname} -a1

sed -i -e 's/Kyocera-Mita-FS-1016/Kyocera-FS-1016/g' foomatic-db/driver/foo2kyo.xml

# fix attribs
chmod 644 COPYING

%build
gcc %{optflags} %{ldflags} -o foo2kyo foo2kyo.c -ljbig

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/foomatic/db/source/{driver,opt,printer}
install -d %{buildroot}%{_datadir}/cups/model/%{rname}

install -m0755 foo2kyo %{buildroot}%{_bindir}
install -m0755 foo2kyo-wrapper %{buildroot}%{_bindir}

for dir in driver opt printer; do
    install -c -m0644 foomatic-db/$dir/*.xml %{buildroot}%{_datadir}/foomatic/db/source/$dir/
done

install -m0644 ppd/Kyocera-FS-1016MFP-foo2kyo.ppd %{buildroot}%{_datadir}/cups/model/%{rname}/

%files
%doc COPYING
%{_bindir}/foo2kyo
%{_bindir}/foo2kyo-wrapper
%{_datadir}/foomatic/db/source/opt/*.xml
%{_datadir}/foomatic/db/source/printer/*.xml
%{_datadir}/foomatic/db/source/driver/*.xml
%dir %{_datadir}/cups/model/%{rname}
%{_datadir}/cups/model/%{rname}/Kyocera-FS-1016MFP-foo2kyo.ppd*

