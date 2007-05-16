# TODO:
# - PLDize
# - fix paths in installed files
%define	buildrev	278227
Summary:	Editor for dynamic languages including Perl, PHP, Python, Ruby and Tcl
Summary(pl.UTF-8):	Edytor dla języków dynamicznych takich jak Perl, PHP, Python, Ruby czy Tcl
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

# it says and fails: BFD: kotcllint: warning: Empty loadable segment detected, is this intentional ?
%define		_noautostrip .*/kotcllint

%description
Award-winning editing for dynamic languages including Perl, PHP,
Python, Ruby and Tcl; plus support for browser-side code including
JavaScript, CSS, HTML and XML.

Background syntax checking and syntax coloring catch errors
immediately, while autocomplete and calltips guide you as you write.
Available on Linux, Mac OS X and Windows.

%description -l pl.UTF-8
Zdobywający nagrody edytor dla języków dynamicznych, takich jak Perl,
PHP, Python, Ruby czy Tcl; zawiera obsługę dla kodu po stronie
przeglądarki wraz z JavaScriptem, CSS-em, HTML-em i XML-em.

Sprawdzanie składni w tle i jej kolorowanie pozwala natychmiast
wyłapać błędy, a automatyczne dopełnianie i podpowiadanie wywołań
prowadzi programistę w trakcie pisania. Edytor dostępny jest dla
Linuksa, MacOS X i Windows.

%prep
%setup -q -n %{name}-%{version}-%{buildrev}-linux-libcpp6-x86

%install
rm -rf $RPM_BUILD_ROOT

sh install.sh \
	--install-dir $RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
# XXX: FIXME
%attr(-,root,root) %{_libdir}/*
#%{_desktopdir}/*
# XXX: too many dirs?
%{_iconsdir}/*
