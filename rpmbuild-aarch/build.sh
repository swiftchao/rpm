VERSION="0.0.1"
HELLOREPM_VERSION="${version}-$(date +%Y%m%d)"
WORKDIR=$(cd $(dirname ${0});pwd)
hello_prj="hellorpm"
RPM_ROOT="${WORKDIR}/rpmbuild"
RPM_SOURCE="${RPM_ROOT}/SOURCES"
ARCH=$(uname -m)

git tag -f -m "hellorepm rpmbuild ${HELLOREPM_VERSION}" -a ${HELLOREPM_VERSION}
DIST=".oe2003"
pushd "${RPM_SOURCE}"
cp -r hellorpm-${VERSION} hellorpm-${VERSION}${DIST}.${ARCH}
rm -f "${RPM_ROOT}/SPECS/hellorpm.spec"
echo y | cp -f "hellorpm-${VERSION}${DIST}.${ARCH}/hellorpm.spec" "${RPM_ROOT}/SPECS/hellorpm.spec"
tar zcvf hellorpm-${VERSION}${DIST}.${ARCH}.tar.gz hellorpm-${VERSION}${DIST}.${ARCH}
popd

rpmbuild -ba "--define=_topdir ${RPM_ROOT}" "--define=_tmppath /home/mockbuild/tmp/rpmbuild" "--define=dist ${DIST}"  "${RPM_ROOT}/SPECS/hellorpm.spec"
cp -rf /home/mockbuild/rpm/rpmbuild-aarch/rpmbuild/RPMS/aarch64/*.rpm /home/mockbuild/rpm/result/aarch/
cp -rf /home/mockbuild/rpm/rpmbuild-aarch/rpmbuild/SRPMS/*.rpm /home/mockbuild/rpm/result/src/
