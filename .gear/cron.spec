
%define _unpackaged_files_terminate_build 1

%define buildpath $PWD/.build

Name: golang-cronv3

Version: 3.0.0

Release: alt1

Summary: Package cron implements a cron spec parser and job runner.

License: MIT

Group: Development/Other

Url: https://github.com/robfig/cron.git

Source: %name-%version.tar

BuildArch: noarch


BuildRequires(pre): rpm-build-golang

BuildRequires: golang

BuildRequires: golang-tools-devel



%description
cron v3 is a major upgrade to the library that addresses all outstanding bugs, feature requests, and rough edges.
It is based on a merge of master which contains various fixes to issues found over the years and the v2 branch which contains some backwards-incompatible features like the ability to remove cron jobs.
In addition, v3 adds support for Go Modules, cleans up rough edges like the timezone support, and fixes a number of bugs.


%prep

%setup

%build

export BUILDDIR="$PWD/.build"

export GOPATH="%go_path"




%golang_build


%install

export BUILDDIR="$PWD/.build"

export GOPATH="%go_path"

%golang_install


%check
export GOPATH="%go_path"
%gotest


%files
%doc LICENSE  README.md
%go_path
%changelog

* Mon Feb 17 2025 Ivan Hanas <xeno@altlinux.org> 3.0.0-alt1
- Initial Build for ALT


