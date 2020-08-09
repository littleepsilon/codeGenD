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
from codeGenD.usrMethod import codeGenC
from codeGenD.usrLib    import codeUnitMethod
from codeGenD.usrLib    import dictProvider

class codeGenFactoryCpp(codeGenC.codeGenFactoryC):

    def generateUnit(self):
        self.processCHeaders()
        self.processCSrc()

    def generateSys(self):
        self.generateWorkspace()
        self.generateMakefile()
        self.generateMainFile('cppSys/')
        self.generateReadme('cppSys/')
        self.generateLicense('cppSys/')
        self.generateGitIgnore('cppSys/')

    # ├── designLog
    # ├── floader_1
    # │   ├── inc
    # │   └── src
    # ├── floader_2
    # │   ├── inc
    # │   └── src
    # ├── LICENSE
    # ├── main.cpp
    # ├── makefile
    # └── readme.md
    def generateWorkspace(self):
        if not self.codeGenFloader:
            self.codeGenMkdir('cppSys')
            self.codeGenMkdir('cppSys/code')
            self.codeGenMkdir('cppSys/code/src')
            self.codeGenMkdir('cppSys/code/inc')
            self.codeGenMkdir('cppSys/designLog')
        else:
            floaderList = str(self.codeGenFloader).split()
            self.codeGenMkdir('cppSys')
            self.codeGenMkdir('cppSys/designLog')
            for singleFloader in floaderList:
                self.codeGenMkdir('cppSys/'+singleFloader)
                self.codeGenMkdir('cppSys/'+singleFloader+'/src')
                self.codeGenMkdir('cppSys/'+singleFloader+'/inc')

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
\t$(compilerStr) -c $(SRC_DIR_@code2 )/src/*.cpp -I $(SRC_DIR_@code2 )/inc
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

main.o : main.cpp
\tmkdir bin
\t$(compilerStr) -c main.cpp @floaderDir 
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
            'compilerStr'  : 'g++ -std=c++11',
            'phonyTarget'  : phonyTarget,
            'srcTargetDef' : srcTargetDef,
            'srcTarget'    : srcTarget,
            'floaderDir'   : floaderDir,
            'srcObjFile'   : srcObjFile,
            'delBinFloader': delBinFloader
        }

        with open('cppSys/makefile', 'w+') as makeFile:
            makeFile.write( codeUnitMethod.codeUnit().parse(dictMakeFile) )

    def generateMainFile(self,dirName):
        tmpDict = {
            'main':\
'''
@header 
#include <iostream>

using namespace std;

int main()
{
    cout << "test" << endl;
}
'''
        }
        tmpDict['header'] = self.header()

        with open(dirName+'main.cpp', 'w+') as mainFile:
            mainFile.write(codeUnitMethod.codeUnit().parse(tmpDict))

    def processCSrc(self):
        cSrcDict = dictProvider.cDict( dictProvider.provide( whichLan = 'cpp' ) )
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

        dirName = str('cppSrc/')
        self.codeGenMkdir(dirName)
        with open(dirName + str(self.codeGenUnitFile) + '.cpp', 'w+') as fp:
            fp.write(tmpStr)

    def processCHeaders(self):
        cHeaderDict = dictProvider.cDict( dictProvider.provide( whichLan = 'cpp' ) )
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

        dirName = str('cppInc/')
        self.codeGenMkdir(dirName)
        with open(dirName + str(self.codeGenUnitFile) + '.h', 'w+') as fileCheader:
            fileCheader.write(tmpStr)