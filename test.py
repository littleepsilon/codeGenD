# -*- coding:utf-8 -*-

#
# time:        02:06
# date:        2020-06-22
# description: test Description on this line 
# author:      untitled


# import pyModule
import sys
import os
import logging

# import 3rd-part Moudle

# import usrModule
import codeGenD

if __name__ == '__main__':

    # 1. -------------------------------------------------------------
    tmpDict = codeGenD.provide()
    codeGenD.store(tmpDict)
    # 2. -------------------------------------------------------------
    tmpDict['default']['func']['funcName' ] = 'testFunc'
    tmpDict['default']['func']['codeBlock'] = \
'''
printf("haha");
printf("hello");
while(0){
    printf("world");
}
'''
    tmpStr  = codeGenD.parse(tmpDict['default']['func'], 'mainSide')
    tmpStr += codeGenD.parse(tmpDict['default']['func'], 'main')
    print(tmpStr)
    codeGenD.out(tmpStr)
    # 3. -------------------------------------------------------------
    codeGenD.generate(m='argv', f='system', l='c', li='gnu3', n='untitled', fl='floader_1 floader_2 gener/floader_3')
    codeGenD.generate(m='argv', f='unit',   l='c', n='david', uf='test', des='this is a test, see what happen')
    # 4. -------------------------------------------------------------
    tmpDict2 = codeGenD.cdict(
        {
            'main' : \
'''
@haha 
@hehe 
test 
    haha
    @kict_ 
''',
            'kict_' : 'test'
        }
    )
    tmpDict2 += {'kict' : 'quite', 'hehe' : 'james'}
    codeGenD.out ( tmpDict2.parse() )
    codeGenD.out ( tmpDict2.parse( Mode='half' ), fileName='test.src' )
    # 5. -------------------------------------------------------------
    codeGenD.app(n='myApp')