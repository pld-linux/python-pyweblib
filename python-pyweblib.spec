%define module  pyweblib

Summary:	Yet another web programming framework for Python.
Name:		python-%{module}
Version:	1.0.4
Release:	1
License:	GPL
Source0:	http://www.stroeder.com/pylib/PyWebLib/download/%{module}-%{version}.tar.gz
URL:		http://www.stroeder.com/pylib/PyWebLib/
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/J�zyki/Python
Requires:	python >= 2.0
BuildRequires:	python-devel >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web application library:                                                                    
    pyweblib.forms        class library for handling <FORM> input
    pyweblib.session      server-side web session handling                                    
    pyweblib.helper       misc. stuff useful in CGI-BINs                                           
    pyweblib.sslenv       retrieves SSL-related env vars
    pyweblib.httphelper   very basic HTTP functions

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{_bindir}/python -- setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
tmpfile=INSTALLED_FILES.$$
grep -v 'py$' INSTALLED_FILES | sort > $tmpfile && mv $tmpfile INSTALLED_FILES
gzip doc/CHANGES*

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc doc/*.gz htdocs/*