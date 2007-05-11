# TODO:
# - PLDize
# - fix paths in installed files

%define	buildrev	278227
Summary:	Editor for dynamic languages including Perl, PHP, Python, Ruby and Tcl
Name:		Komodo-Edit
Version:	4.0.3
Release:	0.1
License:	custom
Group:		X11/Applications/Editors
Source0:	http://downloads.activestate.com/Komodo/Linux/4.0/%{name}-%{version}-%{buildrev}-linux-libcpp6-x86.tar.gz
# Source0-md5:	f754fa658a53ebac13b30438e84d99c0
URL:		http://www.activestate.com/products/komodo_edit/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Award-winning editing for dynamic languages including Perl, PHP,
Python, Ruby and Tcl; plus support for browser-side code including
JavaScript, CSS, HTML and XML.

Background syntax checking and syntax coloring catch errors
immediately, while autocomplete and calltips guide you as you write.
Available on Linux, Mac OS X and Windows.

%prep
%setup -q -n %{name}-%{version}-%{buildrev}-linux-libcpp6-x86

%build

%install
rm -rf $RPM_BUILD_ROOT

sh install.sh \
	--install-dir "$RPM_BUILD_ROOT%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%attr(-,root,root) %{_libdir}/*
#%attr(644,root,root) %{_datadir}/desktop/*
%attr(644,root,root) %{_datadir}/icons/*
