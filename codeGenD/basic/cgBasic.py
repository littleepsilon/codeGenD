# -*- coding:utf-8 -*-
#
# time:        19:32
# date:        2020/06/06
# description: none
# author:      david
# 

# import module
import sys
import logging
import os
import re
import json

# import path
# sys.path.append('path')

# import 3rd-part moudle 

class c_cgbasic(object):
    def __init__(self, logSwitch = False, dbgMode = False):
        self.name      = 'david'
        self.dbgMode   = dbgMode
        self.dbgHex    = True
        self.dbgBin    = True
        self.logSwitch = logSwitch

    def dbgPrint(self, msg, dbgHex=False, dbgBin=False, logSwitch=True):
        if dbgHex == True:
            if self.dbgHex == True:
                print(str(self.__class__) + ':--->>' + ' ' + str(msg))
                if logSwitch and self.logSwitch:
                    logging.info('[' + str(self.__class__) + ']' + ':--->>' + ' ' + str(msg))
            return

        if dbgBin == True:
            if self.dbgBin == True:
                print(str(self.__class__) + ':--->>' + ' ' + str(msg))
                if logSwitch and self.logSwitch:
                    logging.error('[' + str(self.__class__) + ']' + ':--->>' + ' ' + str(msg))
            return

        if self.dbgMode == True:
            print(str(self.__class__) + ':--->>' + ' ' + str(msg))
            if logSwitch and self.logSwitch:
                logging.debug('[' + str(self.__class__) + ']' + ':--->>' + ' ' + str(msg))
            return
        
class shellProcesser(c_cgbasic):
    def __init__(self):
        c_cgbasic.__init__(self)
        self.cmdStrList = []
        self.cmdStrDict = {'noUseKey':'noUsrValue'}
        self.argvCnt    = 0

    def parser(self):
        elseLock = False
        for unitStr in self.cmdStrList:
            res = re.match('-{1,2}(.)*',unitStr)
            if res:
                elseLock = True
                keywordStr = res.group(0).split('-')[-1]
                # self.dbgPrint('the key word is ( ' + keywordStr + ' )')
                if keywordStr in self.cmdStrDict:
                    self.dbgPrint('the keyword exist')
                    return False
                self.cmdStrDict[keywordStr] = 'unSet'
                self.cmdStrDict['noUseKey'] = 'noUse'
            elif elseLock:
                # self.dbgPrint('not a keyword : ' + unitStr)
                if self.cmdStrDict['noUseKey'] == 'use':
                    self.cmdStrDict[keywordStr] += ' '
                else:
                    self.cmdStrDict[keywordStr]  = ''
                self.cmdStrDict[keywordStr] += unitStr
                self.cmdStrDict['noUseKey']  = 'use'
            else:
                self.dbgPrint('find no keyword to start')
                return False

        self.dbgPrint(self.cmdStrDict)
        return self.cmdStrDict

    def saveShellParaDict(self, dictObj):
        jsonStr  = json.dumps(dictObj)
        with open('cmdParaDict.json', 'w+') as dictFile:
            dictFile.write(jsonStr)

    def loadShellParaDict(self):
        with open('cmdParaDict.json', 'r') as dictFile:
            jsonStr  = dictFile.read()
        return json.loads(jsonStr)
