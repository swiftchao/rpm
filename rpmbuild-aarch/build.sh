rpmbuild -ba '--define=_topdir /home/mockbuild/rpm/rpmbuild-aarch/rpmbuild' '--define=_tmppath /home/mockbuild/tmp/rpmbuild' /home/mockbuild/rpm/rpmbuild-aarch/rpmbuild/SPECS/hellorpm.spec
cp -rf /home/mockbuild/rpm/rpmbuild-aarch/rpmbuild/RPMS/aarch64/*.rpm /home/mockbuild/rpm/result/aarch/
cp -rf /home/mockbuild/rpm/rpmbuild-aarch/rpmbuild/SRPMS/*.rpm /home/mockbuild/rpm/result/src/
