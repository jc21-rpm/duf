%define debug_package %{nil}

%global gh_user muesli

Name:           duf
Version:        0.8.1
Release:        1%{?dist}
Summary:        Disk Usage/Free Utility - a better 'df' alternative
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Features
- User-friendly, colorful output
- Adjusts to your terminal's theme & width
- Sort the results according to your needs
- Groups & filters devices
- Can conveniently output JSON

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Feb 8 2022 Jamie Curnow <jc@jc21.com> 0.8.1-1
- https://github.com/muesli/duf/releases/tag/v0.8.1

* Tue Feb 1 2022 Jamie Curnow <jc@jc21.com> 0.8.0-1
- https://github.com/muesli/duf/releases/tag/v0.8.0

* Sat Jan 8 2022 Jamie Curnow <jc@jc21.com> 0.7.0-1
- https://github.com/muesli/duf/releases/tag/v0.7.0

* Mon Jun 21 2021 Jamie Curnow <jc@jc21.com> 0.6.2-1
- https://github.com/muesli/duf/releases/tag/v0.6.2

