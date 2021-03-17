Name:           hellorpm
Version:        0.0.1 
Release:        1
Summary:        This is a test of rpm build 

Group:          Development/Libraries
License:        GPL 
URL:            https://github.com:swiftchao/rpm/rpmbuild
Source0:        %{name}-%{version}-%{release}.%{_arch}.tar.gz 
#将patch文件放在rpmbuild/SOURCES目录下
#在Sourcexx结束和Buildrequires之前加入patch，一般未使用补丁号按递增命名
#add patch
Patch0:0001-test-patch.patch

%description
%{summary}

%prep
#cur=/root/rpmbuild/BUILD
cd $RPM_SOURCE_DIR
tar -xvf $RPM_SOURCE_DIR/%{name}-%{version}-%{release}.%{_arch}.tar.gz

%setup -n %{name}-%{version}-%{release}.%{_arch}
#在setup后build之前加入使用patch
%patch0 -p4

%build
cd $RPM_SOURCE_DIR/%{name}-%{version}-%{release}.%{_arch}
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_SOURCE_DIR/%{name}-%{version}-%{release}.%{_arch}
make install
cp -r $RPM_SOURCE_DIR/%{name}-%{version}-%{release}.%{_arch} %{_topdir}/BUILDROOT/

%post
mkdir -p ${HOME}/bin
echo mkdir -p ${HOME}/bin >>/tmp/chaofeirpm.log
cp test-main ${HOME}/bin/test-main
chmod a+x ${HOME}/bin/test-main
cp test-main /usr/bin/test-main
chmod a+x /usr/bin/test-main
echo ${HOME}/bin/test-main
${HOME}/bin/test-main
echo ${HOME}/bin/test-main >>/tmp/chaofeirpm.log

%postun
rm -f ${HOME}/bin/test-main
rm -f /usr/bin/test-main
rm -f /tmp/chaofeirpm.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/*
#/test-main

%changelog * Wed Mar 1  2019 Chao Fei <chaofeibest@163.com> -0.0.1-1

