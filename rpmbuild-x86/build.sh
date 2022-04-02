rpmbuild -ba '--define=_topdir /home/mockbuild/rpm/rpmbuild-x86/rpmbuild' '--define=_tmppath /home/mockbuild/tmp/rpmbuild' /home/mockbuild/rpm/rpmbuild-x86/rpmbuild/SPECS/hellorpm.spec
cp -rf /home/mockbuild/rpm/rpmbuild-x86/rpmbuild/RPMS/x86_64/*.rpm /home/mockbuild/rpm/result/x86/
cp -rf /home/mockbuild/rpm/rpmbuild-x86/rpmbuild/SRPMS/*.rpm /home/mockbuild/rpm/result/src/
