# -*- coding:utf-8 -*-
#
# time:        19:32
# date:        2020/06/06
# description: none
# author:      david
# 

# import pylib
import sys

# import 3rdPart lib

# import usrLib
from codeGenD.usrLib.snippts import *

TEST_CASE_PASS_THR = 100

def testCase1():
    res                = 0
    snipptsObj         = c_snippts()
    snipptsObj.dbgMode = True
    ret = snipptsObj.dbgPrint('testCase1')
    if ret != 1:
        res = 1
    snipptsObj.dbgMode = False
    ret = snipptsObj.dbgPrint('testCase1')
    if ret != 0:
        res = 1
    return res

def testMain():
    ret         = 0
    counterCase = 0
    funcTable = [ {'func':testCase1,'description':'basic print'} ]
    print('test runing...')
    print('/*+++++++++++++++++++*/')
    for func in funcTable:
        print('testCase : ' + str(counterCase+1) + ' >' + func['description'])
        ret         += func['func']()
        counterCase += 1
        print('/*+++++++++++++++++++*/')
    print('/*-------------------*/')
    print('ret         is %d'%(ret))
    print('counterCase is %d'%(counterCase))
    print('ratio       is %f'%((counterCase - ret)/counterCase*100.0))
    ratio = (counterCase - ret)/counterCase*100.0
    if ratio < TEST_CASE_PASS_THR:
        print('/*-------------------*/')
        print('(@_@)\tmsg    > error!pass rate too low, reject to construct!')
        print('(@_@)\tresult > failure')
        print('/*-------------------*/')
    else:
        print('/*-------------------*/')
        print('(^_^)\tresult > success')
        print('/*-------------------*/')