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