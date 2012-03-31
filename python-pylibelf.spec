%define	oname	pylibelf
%define	module	libelf

Name:		python-%{module}
Version:	0.1
Release:	1
Summary:	An ELF parser for python that uses the libelf library
Source0:	http://eggy.yolky.org/pylibelf/static/docs/_downloads/pylibelf-full.tar.bz2
Url:		http://eggy.yolky.org/pylibelf/
License:	LGPLv2
Group:		Development/Python
BuildRequires:	python-devel
BuildRequires:	python-cython
BuildRequires:	python-sphinx
BuildRequires:	libelf-devel

%description
Pythonic wrapper for the libelf library.

%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch

%description doc
This package contains the HTML documentation for %{name}.

%prep
%setup -q -n %{oname}

%build
python setup.py build

pushd doc
	make html
popd

%install
python setup.py install --root=%{buildroot}

pushd doc
	%{__mkdir_p} %{buildroot}/%{_datadir}/%{name}/doc/
	%{__cp} -a _build/html/ %{buildroot}/%{_datadir}/%{name}/doc/
popd

%files
%{py_platsitedir}/pylibelf/*.py*
%{py_platsitedir}/pylibelf/_constants_elf_h.so
%{py_platsitedir}/pylibelf/_constants_elf_h_dynamic.so
%{py_platsitedir}/pylibelf/_constants_elf_h_relocation.so
%{py_platsitedir}/pylibelf/_constants_libelf_h.so
%{py_platsitedir}/pylibelf/libelf.so
%{py_platsitedir}/pylibelf*.egg-info

%files doc
%doc %{_datadir}/%{name}/doc/
