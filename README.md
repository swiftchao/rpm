利用rpmbuild制作rpm包
1 安装制作rpm包需要的软件
  yum install rpmbuild 
  yum install rpmdevtools
2 开始制作rpm包
  2.1 生成目录树
    cd ${HOME}
    rpmdev-setuptree
    tree rpmbuild
  2.2 拷贝源码文件的压缩包到SOURCE目录下
    cp -f /home/rpmuser/rpmbuild/SOURCES/hellorpm-0.0.1-1.x86_64.tar.gz ${HOME}/rpmbuild/SOURCES/
  2.3 生成hellorpm.spec文件
    cd ${HOME}/rpmbuild/SPECS
    rpmdev-newspec -o hellorpm.spec
  2.4 修改hellorpm.spec文件
    vim hellorpm.spec
  2.5 生成rpm包文件
    cd ${HOME}/rpmbuild
    rpmbuild -ba SPECS/hellorpm.spec
  2.6 查看生成rpm包之后的目录结构树
    cd ${HOME}
    tree rpmbuild
  2.7 查看rpm包的信息
    cd /home/chaofei/code/git/rpm/rpmbuild/RPMS/x86_64
    rpm -qpi hellorpm-0.0.1-1.x86_64.rpm
  2.8 解压rpm包，查看是否制作正确
    rpm2cpio hellorpm-0.0.1-1.x86_64.rpm | cpio -idmv
3 安装rpm包
  cd /home/chaofei/code/git/rpm/rpmbuild/RPMS/x86_64
  rpm -qa | grep hello
  sudo rpm -ivh hellorpm-0.0.1-1.x86_64.rpm
  3.1 测试是否安装成功
  whereis test-main
  test-main
  rpm -qa | grep hello
4 卸载rpm包
  rpm -qa | grep hello
  test-main
  su root -c "rpm -qa | grep hello | xargs rpm -e"
