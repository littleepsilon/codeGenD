# -*- coding:utf-8 -*-
# 
# time:        00:55
# date:        2020-06-15
# author:      None
# description: test Description on this line untitled 
# 
# import pyModule
import sys
import os
import copy
from time import strftime, localtime
# import 3rd-part Moudle

# import usrModule
from codeGenD.usrMethod import codeGenMethod
from codeGenD.usrLib    import codeUnitMethod
from codeGenD.usrLib    import dictProvider

class codeGenFactoryC(codeGenMethod.codeGenFactory):

    def generateUnit(self):
        self.processCHeaders()
        self.processCSrc()

    def generateSys(self):
        self.generateWorkspace()
        self.generateMakefile()
        self.generateMainFile('cSys/')
        self.generateReadme('cSys/')
        self.generateLicense('cSys/')
        self.generateGitIgnore('cSys/')

    # code
    # |-inc
    # |-src
    # designLog
    def generateWorkspace(self):
        if not self.codeGenFloader:
            self.codeGenMkdir('cSys')
            self.codeGenMkdir('cSys/code')
            self.codeGenMkdir('cSys/code/src')
            self.codeGenMkdir('cSys/code/inc')
            self.codeGenMkdir('cSys/designLog')
        else:
            floaderList = str(self.codeGenFloader).split()
            self.codeGenMkdir('cSys')
            self.codeGenMkdir('cSys/designLog')
            for singleFloader in floaderList:
                self.codeGenMkdir('cSys/'+singleFloader)
                self.codeGenMkdir('cSys/'+singleFloader+'/src')
                self.codeGenMkdir('cSys/'+singleFloader+'/inc')

    def generateMakefile(self):
        floaderList = str(self.codeGenFloader).split()

        phonyTarget = ''
        for singleFloader in floaderList:
            phonyTarget += singleFloader.replace('/','') + ' '

        srcTargetDef = ''
        for singleFloader in floaderList:
            srcTargetDef += 'SRC_DIR_' + str(singleFloader).upper().replace('/','') + '=' + singleFloader + '\r\n'

        srcTarget = ''
        srcTargetDictOrigin = {
            'main' : \
'''
@code1  : 
\tmkdir $(SRC_DIR_@code2 )/bin
\t$(compilerStr) -c $(SRC_DIR_@code2 )/src/*.c -I $(SRC_DIR_@code2 )/inc
\tmv *.o $(SRC_DIR_@code2 )/bin
''',
            'code1' : ' ',
            'code2' : ' '
        }

        for singleFloader in floaderList:
            srcTargetDict = copy.deepcopy(srcTargetDictOrigin)
            srcTargetDict['code1'] = str(singleFloader).replace('/','')
            srcTargetDict['code2'] = str(singleFloader).upper().replace('/','')
            srcTarget += codeUnitMethod.codeUnit().parse(srcTargetDict)

        floaderDir = ''
        for singleFloader in floaderList:
            floaderDir += ' -I' + ' $(' + 'SRC_DIR_' + str(singleFloader).upper().replace('/','') + ')/inc'

        srcObjFile = ''
        for singleFloader in floaderList:
            srcObjFile += ' $(' + 'SRC_DIR_' + str(singleFloader).upper().replace('/','') + ')/bin/*.o'

        delBinFloader = ''
        for singleFloader in floaderList:
            delBinFloader += '\trm -rf $(' + 'SRC_DIR_' + str(singleFloader).upper().replace('/','') + ')/bin\r\n'

        dictMakeFile = {
            'main' : \
'''
.PHONY: clean main @phonyTarget 

outFileName=a.bin
compilerStr=@compilerStr 
@srcTargetDef 

@srcTarget 

main.o : main.c
\tmkdir bin
\t$(compilerStr) -c main.c @floaderDir 
\tmv *.o bin/

main : main.o @phonyTarget 
\tmkdir release
\t$(compilerStr) -o $(outFileName) bin/*.o @srcObjFile 
\tmv $(outFileName) release/

clean : 
\tfind -name "*.o" | xargs rm -rf
\tfind -name "*.gch" | xargs rm -rf
\tfind -name "$(outFileName)" | xargs rm -rf
\trm -rf bin release
@delBinFloader 
''',
            'compilerStr'  : 'gcc',
            'phonyTarget'  : phonyTarget,
            'srcTargetDef' : srcTargetDef,
            'srcTarget'    : srcTarget,
            'floaderDir'   : floaderDir,
            'srcObjFile'   : srcObjFile,
            'delBinFloader': delBinFloader
        }

        with open('cSys/makefile', 'w+') as makeFile:
            makeFile.write( codeUnitMethod.codeUnit().parse(dictMakeFile) )

    def header(self):
        self.makeDes()
        tmpDict = {
            'main' : \
'''
/*
 time        : @time 
 date        : @date 
 author      : @author 
 description : @description 
*/
'''
        }
        tmpDict['time']        = strftime( "%H:%M",localtime() )
        tmpDict['date']        = strftime( "%Y-%m-%d", localtime() )
        tmpDict['author']      = str(self.yourname)
        tmpDict['description'] = str(self.desMake)
        return codeUnitMethod.codeUnit().parse(tmpDict)

    def generateMainFile(self,dirName):
        tmpDict = {
            'main' : \
'''
@header 
#include <stdio.h>

int main()
{
	printf("test\\n");
    return 0;
}
'''
        }
        tmpDict['header'] = self.header()

        with open(dirName+'main.c', 'w+') as mainFile:
            mainFile.write(codeUnitMethod.codeUnit().parse(tmpDict))

    def processCHeaders(self):
        cHeaderDict = dictProvider.cDict( dictProvider.provide( whichLan = 'c' ) )
        cHeaderDict = dictProvider.cDict( cHeaderDict['default']['headers'] )
        
        plusDict    = {
            'headStr'      : str(self.header()),
            'unitFileName' : str(self.codeGenUnitFile).upper(),
            'dependency'   : ' ',
            'macro'        : ' ',
            'enum'         : ' ',
            'struct'       : ' ',
            'packa'        : '1',
            'packb'        : ' ',
            'global'       : ' ',
            'someDeclare'  : ' ',
        }

        cHeaderDict += plusDict
        if self.codeGenAddDictch:
            cHeaderDict += self.codeGenAddDictch

        tmpStr = codeUnitMethod.codeUnit().parse(cHeaderDict)

        dirName = str('cinc/')
        self.codeGenMkdir(dirName)
        with open(dirName + str(self.codeGenUnitFile) + '.h', 'w+') as fileCheader:
            fileCheader.write(tmpStr)

    def processCSrc(self):
        cSrcDict = dictProvider.cDict( dictProvider.provide( whichLan = 'c' ) )
        cSrcDict = dictProvider.cDict( cSrcDict['default']['source'] )
        
        plusDict    = {
            'headStr'      : str(self.header()),
            'dependency'   : ' ',
            'macro'        : ' ',
            'enum'         : ' ',
            'struct'       : ' ',
            'packa'        : '1',
            'packb'        : ' ',
            'global'       : ' ',
            'someDef'      : ' ',
        }

        cSrcDict += plusDict
        if self.codeGenAddDictcs:
            cSrcDict += self.codeGenAddDictcs

        tmpStr = codeUnitMethod.codeUnit().parse(cSrcDict)

        dirName = str('csrc/')
        self.codeGenMkdir(dirName)
        with open(dirName + str(self.codeGenUnitFile) + '.c', 'w+') as fp:
            fp.write(tmpStr)
