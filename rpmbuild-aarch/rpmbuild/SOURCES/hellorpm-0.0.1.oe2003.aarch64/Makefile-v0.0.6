objects=test-main.o max.o swap.o
test-main:$(objects)
	gcc -o test-main $(objects)

$(objects):

.PHONY:alltest
alltest:test1
test1:
	echo $@ $(subst 1,, $@)

.PHONY:clean
clean:
	-rm -rf test-main $(objects) *.gch

# -rm 作用报错也继续执行

install:
	mkdir -p ${HOME}/bin
	echo mkdir -p ${HOME}/bin >> /tmp/chaofeirpm.log
	cp test-main ${HOME}/bin/test-main
	chmod a+x ${HOME}/bin/test-main
	#cp test-main /usr/bin/test-main
	#chmod a+x /usr/bin/test-main
	echo ${HOME}/bin/test-main
	${HOME}/bin/test-main
	echo ${HOME}/bin/test-main >> /tmp/chaofeirpm.log

uninstall:
	rm -f ${HOME}/bin/test-main
	#rm -f /usr/bin/test-main
	rm -f /tmp/chaofeirpm.log

.PHONY:test
test:
	objects=*.o
	echo $(objects)
	#objects=$(wildcard *o)
	#echo $(objects)
  vpath="%.h ./"
	#echo $(vpath)

.PHONY: cleanall cleanobj cleandiff
cleanall: cleanobj cleandiff
	rm -f test-main
cleanobj:
	rm -f *.o
cleandiff:
	rm -f *.diff
