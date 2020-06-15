%global real_name schedule

Name:           python-schedule
Version:        1.1.0
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

%package -n python3-schedule
Summary:        Python job scheduling for humans

%description -n python3-schedule
An in-process scheduler for periodic jobs that uses the builder pattern for
configuration. Schedule lets you run Python functions (or any other callable)
periodically at pre-determined intervals using a simple, human-friendly syntax.

%prep
%autosetup -n %{real_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files schedule

%check
# Requires network:
#tox
%py3_check_import %{real_name}

%files -n python3-schedule -f %{pyproject_files}
%license LICENSE.txt
%doc AUTHORS.rst README.rst

%changelog
* Fri Nov 05 2021 Simone Caronni <negativo17@gmail.com> - 1.1.0-1
- First build.
