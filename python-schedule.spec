%global real_name schedule

Name:           python-schedule
Version:        0.6.0
Release:        1%{?dist}
Summary:        Python job scheduling for humans
License:        MIT
URL:            http://schedule.readthedocs.io/
BuildArch:      noarch

Source0:        https://github.com/dbader/%{real_name}/archive/%{version}.tar.gz#/%{real_name}-%{version}.tar.gz

BuildRequires:  python3-devel

%description
An in-process scheduler for periodic jobs that uses the builder pattern for
configuration. Schedule lets you run Python functions (or any other callable)
periodically at pre-determined intervals using a simple, human-friendly syntax.

%package     -n python3-schedule
Summary:        Python job scheduling for humans

%description -n python3-schedule
An in-process scheduler for periodic jobs that uses the builder pattern for
configuration. Schedule lets you run Python functions (or any other callable)
periodically at pre-determined intervals using a simple, human-friendly syntax.

%prep
%autosetup -n %{real_name}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}

#%check
#%{__python3} setup.py test

%files -n python3-schedule
%license LICENSE.txt
%doc AUTHORS.rst README.rst
%{python3_sitelib}/*

%changelog
* Sun Jun 14 2020 Simone Caronni <negativo17@gmail.com> - 0.6.0-1
- First build.
