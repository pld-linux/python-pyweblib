%define		module	pyweblib
Summary:	Yet another web programming framework for Python
Summary(pl.UTF-8):	Jeszcze jedno środowisko do programowania WWW dla Pythona
Name:		python-%{module}
Version:	1.3.3
Release:	6
License:	GPL
Source0:	http://www.stroeder.com/pylib/PyWebLib/download/%{module}-%{version}.tar.gz
# Source0-md5:	755b6d474ea584194afb9c4474df0b2a
URL:		http://www.stroeder.com/pylib/PyWebLib/
BuildRequires:	rpmbuild(macros) >= 1.710
Group:		Development/Languages/Python
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.0
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Web application library:
pyweblib.forms		class library for handling <FORM> input
pyweblib.session	server-side web session handling
pyweblib.helper		misc. stuff useful in CGI-BINs
pyweblib.sslenv		retrieves SSL-related env vars
pyweblib.httphelper	very basic HTTP functions

%description -l pl.UTF-8
Biblioteka aplikacji WWW:
pyweblib.forms		biblioteka klas do obsługi wejścia <FORM>
pyweblib.session	obsługa sesji po stronie serwera WWW
pyweblib.helper		różne narzędzia przydatne w cgi-bin
pyweblib.sslenv		odczytywanie zmiennych związanych z SSL
pyweblib.httphelper	podstawowe funkcje HTTP

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install
%py_postclean

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
install cgi-bin/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* htdocs/*
%{py_sitescriptdir}/*
%{_examplesdir}/*
