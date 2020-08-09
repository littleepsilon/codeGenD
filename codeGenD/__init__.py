# -*- coding:utf-8 -*-
#
# time:        19:32
# date:        2020/06/06
# description: none
# author:      david
# 
import sys
import os

# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '/usrLib/')
# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '/interface/')
# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '/basic/')
# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '/usrMethod/')

from codeGenD.usrLib.codeUnitMethod import codeUnit
from codeGenD.usrLib                import dictProvider
from codeGenD.usrMethod             import codeGenMethod

class cdict(dictProvider.cDict):
    pass

def provide(**kwargs):
    '''
    whichLan = 'c', fileNameIn = None
    '''
    dict1 = cdict( dictProvider.provide( **kwargs ) )
    return dict1

def store(*args, **kwargs):
    '''
    dictIn, fileName='untitled.json'
    '''
    dictProvider.store(*args, **kwargs)
    
def parse(*args, **kwargs):
    '''
    codeDict, targetStr = 'main', Mode='full' or 'half'
    '''
    return codeUnit().parse(*args, **kwargs)

def out(strParse ,fileName = 'untitled.src'):
    with open(fileName, 'w+') as tmpFile:
        tmpFile.write(strParse)

def generate(**kwargs):
    '''
    -m Material argv or file
        argv:
        -f  Format   unit or system
        -l  language c or cpp or python
            unit:
            -uf   unitFileName
            -adch dict added
            -adcs dict added
            -li   license MIT gnu3 apache
            -des  description
            sys:
            -li license MIT gnu3 apache
            -fl floaderList

            -n author name

        file:
            -cf codeGenFileName
    -i increaseMode
    '''
    codeGenMethod.generate(**kwargs)

def app(**kwargs):
    '''
    generate a usr codeGenD app
    n='appName', li='MIT' or 'apache' or 'gnu3'
    '''
    codeGenMethod.app(**kwargs)
