# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-ansible-compat
Epoch: 100
Version: 4.1.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Python package for Ansible 2.9 or newer
License: MIT
URL: https://github.com/ansible/ansible-compat/tags
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ansible-compat
Summary: Python package for Ansible 2.9 or newer
Requires: ansible-core >= 2.12
Requires: python3
Requires: python3-jsonschema >= 4.6.0
Requires: python3-packaging
Requires: python3-PyYAML
Requires: python3-subprocess-tee >= 0.4.1
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
Requires: ansible-core >= 2.12
Requires: python3
Requires: python3-jsonschema >= 4.6.0
Requires: python3-packaging
Requires: python3-PyYAML
Requires: python3-subprocess-tee >= 0.4.1
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
Requires: ansible-core >= 2.12
Requires: python3
Requires: python3-jsonschema >= 4.6.0
Requires: python3-packaging
Requires: python3-pyyaml
Requires: python3-subprocess-tee >= 0.4.1
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
