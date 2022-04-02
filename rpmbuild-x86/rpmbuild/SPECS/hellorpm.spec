%define __debug_install_post \
%{_rpmconfigdir}/find-debuginfo.sh %{?_find_debuginfo_opts} "%{_builddir}/%{?buildsubdir}"\
%{nil}
Name:           hellorpm
Version:        0.0.1 
Release:        1
Summary:        This is a test of rpm build 

Group:          Development/Libraries
License:        GPL 
URL:            https://github.com:swiftchao/rpm
Source0:        %{name}-%{version}-%{release}.%{_arch}.tar.gz 
#将patch文件放在rpmbuild/SOURCES目录下
#在Sourcexx结束和Buildrequires之前加入patch，一般未使用补丁号按递增命名
#add patch
Patch0:0001-test-patch.patch

%description
%{summary}

%prep
%setup -n %{name}-%{version}-%{release}.%{_arch}
#在setup后build之前加入使用patch
%patch0 -p4

%build
%configure
make clean
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
echo $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/share
cp -f $RPM_BUILD_DIR/%{name}-%{version}-%{release}.%{_arch}/test-main $RPM_BUILD_ROOT/usr/bin/
cp -r $RPM_BUILD_DIR/%{name}-%{version}-%{release}.%{_arch} $RPM_BUILD_ROOT/usr/local/share/


%post
chmod a+x /usr/bin/test-main
mkdir -p ${HOME}/bin
echo mkdir -p ${HOME}/bin >>/tmp/chaofeirpm.log
cp /usr/bin/test-main ${HOME}/bin/test-main
chmod a+x ${HOME}/bin/test-main
echo ${HOME}/bin/test-main
${HOME}/bin/test-main
echo ${HOME}/bin/test-main >>/tmp/chaofeirpm.log

%postun
if [ $1 = 0 ]; then
  rm -f ${HOME}/bin/test-main
  rm -f /usr/bin/test-main
  rm -f /tmp/chaofeirpm.log
fi

%clean
rm -rf $RPM_BUILD_ROOT
make clean

%files
%defattr(-,root,root,-)
/usr/local/share/%{name}-%{version}-%{release}.%{_arch}
/usr/bin/test-main

%changelog * Wed Mar 1  2019 Chao Fei <chaofeibest@163.com> -0.0.1-1

