#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Portable, lightweight MessagePack serializer and deserializer written in pure Python
Summary(pl.UTF-8):	Przenośna, lekka serializacja i deserializacja MessagePack napisana w czystym Pythonie
Name:		python-u-msgpack
Version:	2.7.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/u-msgpack-python
Source0:	https://files.pythonhosted.org/packages/source/u/u-msgpack-python/u-msgpack-python-%{version}.tar.gz
# Source0-md5:	8691cea6bc7b44bce6e2115260a54323
URL:		https://github.com/vsergeev/u-msgpack-python
%if %{with tests} && %(locale -a | grep -q '^C\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
u-msgpack-python is a lightweight MessagePack <http://msgpack.org/>
serializer and deserializer module written in pure Python, compatible
with both Python 2 and Python 3, as well as CPython and PyPy
implementations of Python. u-msgpack-python is fully compliant with
the latest MessagePack specification
<https://github.com/msgpack/msgpack/blob/master/spec.md>. In
particular, it supports the new binary, UTF-8 string, and
application-defined ext types.

%description -l pl.UTF-8
u-msgpack-python to lekki moduł serializacji i deserializacji
MessagePack <http://msgpack.org/> napisany w Pythonie, zgodny z
Pythonem zarówno 2 i 3, z implementacjami CPython jak i PyPy.
u-msgpack-python jest w pełni zgodny z ostatnią specyfikacją
MessagePack <https://github.com/msgpack/msgpack/blob/master/spec.md>.
W szczególności obsługuje nowe typu binary, łańcuch UTF-8 oraz ext
definiowane przez aplikacje.

%package -n python3-u-msgpack
Summary:	Portable, lightweight MessagePack serializer and deserializer written in pure Python
Summary(pl.UTF-8):	Przenośna, lekka serializacja i deserializacja MessagePack napisana w czystym Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-u-msgpack
u-msgpack-python is a lightweight MessagePack <http://msgpack.org/>
serializer and deserializer module written in pure Python, compatible
with both Python 2 and Python 3, as well as CPython and PyPy
implementations of Python. u-msgpack-python is fully compliant with
the latest MessagePack specification
<https://github.com/msgpack/msgpack/blob/master/spec.md>. In
particular, it supports the new binary, UTF-8 string, and
application-defined ext types.

%description -n python3-u-msgpack -l pl.UTF-8
u-msgpack-python to lekki moduł serializacji i deserializacji
MessagePack <http://msgpack.org/> napisany w Pythonie, zgodny z
Pythonem zarówno 2 i 3, z implementacjami CPython jak i PyPy.
u-msgpack-python jest w pełni zgodny z ostatnią specyfikacją
MessagePack <https://github.com/msgpack/msgpack/blob/master/spec.md>.
W szczególności obsługuje nowe typu binary, łańcuch UTF-8 oraz ext
definiowane przez aplikacje.

%prep
%setup -q -n u-msgpack-python-%{version}

%build
export LC_ALL=C.UTF-8

%if %{with python2}
%py_build

%if %{with tests}
%{__python} test_umsgpack.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test_umsgpack.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE
%{py_sitescriptdir}/umsgpack.py[co]
%{py_sitescriptdir}/u_msgpack_python-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-u-msgpack
%defattr(644,root,root,755)
%doc LICENSE
%{py3_sitescriptdir}/umsgpack.py
%{py3_sitescriptdir}/__pycache__/umsgpack.cpython-*.py[co]
%{py3_sitescriptdir}/u_msgpack_python-%{version}-py*.egg-info
%endif
