# 利用rpmbuild制作rpm包
##  1 安装制作rpm包需要的软件
      yum install rpmbuild 
      yum install rpmdevtools
##  2 开始制作rpm包
###   2.1 生成目录树
        可以修改默认值%_topdir
        vim ~/.rpmmacros
        %_topdir ${HOME}/rpmbuild
        %_topdir /home/chaofei/code/git/rpm/rpmbuild
        cd ${HOME}
        rpmdev-setuptree
        tree rpmbuild
###   2.2 拷贝源码文件的压缩包到SOURCE目录下
        cp -f /home/rpmuser/rpmbuild/SOURCES/hellorpm-0.0.1-1.x86_64.tar.gz ${HOME}/rpmbuild/SOURCES/
###   2.3 生成hellorpm.spec文件
        cd ${HOME}/rpmbuild/SPECS
        rpmdev-newspec -o hellorpm.spec
###   2.4 修改hellorpm.spec文件
        vim hellorpm.spec
###  2.5 生成rpm包文件
       cd ${HOME}/rpmbuild
       rpmbuild -ba SPECS/hellorpm.spec
###  2.6 查看生成rpm包之后的目录结构树
       cd ${HOME}
       tree rpmbuild
###  2.7 查看rpm包的信息
       cd ${HOME}/rpmbuild/RPMS/x86_64
       rpm -qpi hellorpm-0.0.1-1.x86_64.rpm
###  2.8 解压rpm包，查看是否制作正确
       rpm2cpio hellorpm-0.0.1-1.x86_64.rpm | cpio -idmv
## 3 安装rpm包
     cd ${HOME}/rpmbuild/RPMS/x86_64
     rpm -qa | grep hello
     sudo rpm -ivh hellorpm-0.0.1-1.x86_64.rpm
###  3.1 测试是否安装成功
       whereis test-main
       test-main
       rpm -qa | grep hello
## 4 卸载rpm包
     rpm -qa | grep hello
     test-main
     su root -c "rpm -qa | grep hello | xargs rpm -e"
## 5 说明
将patch文件放在rpmbuild/SOURCES目录下
在Sourcexx结束和Buildrequires之前加入patch，一般未使用补丁号按递增命名
在setup后build之前加入使用patch

P0:你当前的目录位置,去找old/a/b/foo.txt
p1:你当前目录位置去找a/b/foo.txt,p1会掉old/,到当前目录找a/b/foo.txt
p2:你当前目录位置去找a/b/foo.txt,p2会掉old/a,到当前目录找b/foo.txt
p3:你当前目录位置去找a/b/foo.txt,p3会掉old/a/b,到当前目录找foo.txt
结论：决定补丁如何补:你的补丁所在的目录（你该把补丁放在那里)
    P(N)决定去查找要补丁的文件路径,不同的N,会掉某部分路径后,再在当前目录,找已除掉后路径,找文件去补丁
    P(N)与当前目录关系很大,与补丁在那里没有关系
    patch -d xx  P(N) 〈 XX  可以命令行上指定 工作目录

