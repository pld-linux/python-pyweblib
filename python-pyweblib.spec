%include	/usr/lib/rpm/macros.python
%define module  pyweblib
Summary:	Yet another web programming framework for Python
Summary(pl):	Jeszcze jedno ¶rodowisko do programowania WWW dla Pythona
Name:		python-%{module}
Version:	1.3.1
Release:	1
License:	GPL
Source0:	http://www.stroeder.com/pylib/PyWebLib/download/%{module}-%{version}.tar.gz
# Source0-md5:	75ad0dfd2fd9a6f03fcfb363e70c17c7
URL:		http://www.stroeder.com/pylib/PyWebLib/
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
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

%description -l pl
Biblioteka aplikacji WWW:
pyweblib.forms        biblioteka klas do obs³ugi wej¶cia <FORM>
pyweblib.session      obs³uga sesji po stronie serwera WWW
pyweblib.helper       ró¿ne narzêdzia przydatne w cgi-bin
pyweblib.sslenv       odczytywanie zmiennych zwi±zanych z SSL
pyweblib.httphelper   podstawowe funkcje HTTP

%prep
%setup -q -n %{module}-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{_bindir}/python -- setup.py install --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm
install cgi-bin/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* htdocs/*
%{py_sitescriptdir}/*
%{_examplesdir}/*
