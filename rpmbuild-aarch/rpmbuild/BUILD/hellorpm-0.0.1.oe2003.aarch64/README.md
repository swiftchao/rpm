#root user exec mv Makefile-root Makefile
#simple user exec mv Makefile-simpleuser Makefile
#if you want change the value of %_topdir you can create ~/.rpmmacros file
#%_topdir default value is ~/rpmbuild defined in /usr/lib/rpm/macros file
#vim ~/.rpmmacros
#eg: %_topdir /home/chaofei/code/git/rpm/rpmbuild
