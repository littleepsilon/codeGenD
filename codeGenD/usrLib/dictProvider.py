# -*- coding:utf-8 -*-

#
# time:        23:40
# date:        2020-06-20
# description: test Description on this line 
# author:      untitled


# import pyModule
import sys
import os
import copy
import json

# import 3rd-part Moudle

sys.path.append( '../../' )

# import usrModule
from codeGenD.usrLib import codeUnitMethod

from codeGenD.usrLib.dictC      import cDict as cDict_
from codeGenD.usrLib.dictPython import pyDict
from codeGenD.usrLib.dictCpp    import cppDict


def provide(whichLan = 'c', fileNameIn = None):
    if fileNameIn:
        return dictProvider().provide( fileNameIn )
    elif whichLan == 'c':
        return dictProvider().provide( os.path.split( os.path.realpath(__file__) )[0] + '/' + 'cDict.json')
    elif whichLan == 'cpp':
        return dictProvider().provide( os.path.split( os.path.realpath(__file__) )[0] + '/' + 'cppDict.json')
    elif whichLan == 'python':
        return dictProvider().provide( os.path.split( os.path.realpath(__file__) )[0] + '/' + 'pyDict.json')

def store(dictIn, fileName='untitled.json'):
    with open(fileName, 'w+') as filep:
        filep.write( json.dumps(dictIn) )        
class cDict(dict):
    def __add__(self, other):
        dict1=cDict( copy.deepcopy( self.copy() ) )
        dict1.update(other)
        return dict1

    def provide(self):
        dict1=cDict( copy.deepcopy( self.copy() ) )
        return dict1

    def parse(self, targetStr = 'main', Mode='full'):
        return codeUnitMethod.codeUnit().parse( self.provide(), targetStr, Mode )

class dictProvider(object):
    def __init__(self):
        pass
    
    def provide(self, fileName = 'cDict.json'):
        with open( fileName,'r' ) as fileR:
            cDict = json.loads( fileR.read() )
        return cDict

if __name__ == '__main__':

    cDictJson = open('cDict.json','w+')
    cDictJson.write( json.dumps(cDict_) )
    cDictJson.close()

    pyDictJson = open('pyDict.json', 'w+')
    pyDictJson.write( json.dumps(pyDict) )
    pyDictJson.close()

    cppDictJson = open('cppDict.json', 'w+')
    cppDictJson.write( json.dumps(cppDict) )
    cppDictJson.close()
