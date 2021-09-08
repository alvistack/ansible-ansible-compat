%global debug_package %{nil}

Name: python-ansible-compat
Epoch: 100
Version: 2.0.3
Release: 1%{?dist}
BuildArch: noarch
Summary: Python package for Ansible 2.9 or newer
License: MIT
URL: https://github.com/ansible-community/ansible-compat/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A python package contains functions that facilitate working with various
versions of Ansible 2.9 and newer.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ansible-compat
Summary: Python package for Ansible 2.9 or newer
Requires: python3
Requires: python3-cached-property >= 1.5
Requires: python3-PyYAML
Requires: python3-subprocess-tee >= 0.3.5
Provides: python3-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-compat) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-compat) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-compat) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ansible-compat
A python package contains functions that facilitate working with various
versions of Ansible 2.9 and newer.

%files -n python%{python3_version_nodots}-ansible-compat
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ansible-compat
Summary: Python package for Ansible 2.9 or newer
Requires: python3
Requires: python3-cached-property >= 1.5
Requires: python3-PyYAML
Requires: python3-subprocess-tee >= 0.3.5
Provides: python3-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-compat) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-compat) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-compat) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-compat
A python package contains functions that facilitate working with various
versions of Ansible 2.9 and newer.

%files -n python3-ansible-compat
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-ansible-compat
Summary: Python package for Ansible 2.9 or newer
Requires: python3
Requires: python3-cached_property >= 1.5
Requires: python3-pyyaml
Requires: python3-subprocess-tee >= 0.3.5
Provides: python3-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-compat) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-compat) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-compat = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-compat) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-compat
A python package contains functions that facilitate working with various
versions of Ansible 2.9 and newer.

%files -n python3-ansible-compat
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
