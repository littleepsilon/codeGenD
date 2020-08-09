.PHONY: clean main install

main:install

install:
	python setup.py install

pack:
	python setup.py sdist

clean: 
	find -name "*.pyc" | xargs rm -rf
	find -name "*pycache*" | xargs rm -rf
	find -name "*.log" | xargs rm -rf

	-rm -rf cinc
	-rm -rf csrc
	-rm -rf pySrc
	-rm -rf cppInc
	-rm -rf cppSrc
	-rm -rf cSys
	-rm -rf cppSys
	-rm -rf pySys

	-rm *.json
	-rm *.src