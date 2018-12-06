%bcond_without check

%global goipath     github.com/mdlayher/netlink
%global commit      4883a4eea879019cdefdeab3d309e16ee5903ee1
Version:            0

%global common_description %{expand:
Package netlink provides low-level access to Linux netlink sockets.}

%gometa

Name:    %{goname}
Release: 0.3%{?dist}
Summary: Package netlink provides low-level access to Linux netlink sockets
License: MIT
URL:     %{gourl}
Source:  %{gosource}

%if %{with check}
BuildRequires: golang(golang.org/x/net/bpf)
BuildRequires: golang(golang.org/x/sys/unix)
%endif

%description
%{common_description}

%package   devel
Summary:   %{summary}

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
rm -rf vendor

%install
%goinstall

%check
%if %{with check}
  %gochecks
%endif

%files devel -f devel.file-list
%license LICENSE.md
%doc *\.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git4883a4e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Paul Gier <pgier@redhat.com> - 0-0.2.20180514git4883a4e
- Remove special handling of s390x

* Tue May 08 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180508gitdc21697
- First package for Fedora

