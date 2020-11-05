# -*- coding:utf-8 -*-

#
# time:        02:56
# date:        2020-06-22
# description: test Description on this line 
# author:      untitled


# import pyModule
# import sys
# import os

# import 3rd-part Moudle

# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '' )

# import usrModule

pyDict = {}

pyDict['default'] = {}

pyDict['default']['class'] = {
    'main' : \
'''
class @className ( @obj  ):
    @init 
    @funcBlock 
''',
    'className' : 'untitled',
    'obj'       : ' ',
    'init'      : ' ',
    'funcBlock' : ' ',
}

pyDict['default']['def'] = {
    'main' : \
'''
def @funcName (@para ):
    @funcBlock 
''',
    'funcName' : 'untitled',
    'para'     : ' ',
    'funcBlock': 'pass',
}

pyDict['default']['layout'] = {
    'main' : \
'''
# -*- coding:utf-8 -*-
@headers 
# import pyModule
# import sys
# import os
@pyModules 

# import 3rd-part Moudle
@import1 
# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '' )
@import2 
# import usrModule
@import3 

@subjectBlock 
''',
    'headers'      : ' ',
    'pyModules'    : ' ',
    'import1'      : ' ',
    'import2'      : ' ',
    'import3'      : ' ',
    'subjectBlock' : ' ',
}

pyDict['default']['setup'] = {
    'main' : \
'''
# -*- coding:utf-8 -*-
@headers 
# import pyModule
# import sys
# import os
import setuptools
@pyModules 

# import 3rd-part Moudle
@import1 
# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '' )
@import2 
# import usrModule
@import3 

@subjectBlock 

setuptools.setup(
    name="@projectName ",
    version="@version ",
    author="@yourName ",
    author_email="@email ",
    description="@projDes ",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="@url ",
    packages=setuptools.find_packages(),
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
''',
    'headers'      : ' ',
    'pyModules'    : ' ',
    'import1'      : ' ',
    'import2'      : ' ',
    'import3'      : ' ',
    'subjectBlock' : ' ',
    'projectName'  : ' ',
    'version'      : ' ',
    'yourName'     : ' ',
    'email'        : ' ',
    'projDes'      : ' ',
    'url'          : ' ',
}