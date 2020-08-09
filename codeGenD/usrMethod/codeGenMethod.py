# -*- coding:utf-8 -*-
#
# time:        19:32
# date:        2020/06/06
# description: this file includes method generate single src file or floaders workspace blank project
# author:      david
# 

import sys
import logging
import os
import json

from time import strftime, localtime

# import 3rd-part moudle 

# import usrModule
from codeGenD.basic  import cgBasic

from codeGenD.usrMethod.readmeMaterial import readmeStrMaterial
from codeGenD.usrMethod.readmeMaterial import licenseStr, licenseStrApache, licenseStrGNU3

# generate files or floader workspace method

def generate(**kwargs):
    codeGenMethod(kwargs).generate()

def app(**kwargs):
    kwargs['l']  ='python'
    kwargs['f']  ='system'
    kwargs['fl'] ='usrLib usrMethod basic interface test'
    codeGenMethod(kwargs).generate()

class codeGenMethod(cgBasic.c_cgbasic):
    def __init__(self, argsDict):
        cgBasic.c_cgbasic.__init__(self)

        self.codeGenMaterial  = None
        self.codeGenFormat    = None
        self.codeGenLanguage  = None
        self.codeGenUnitFile  = None
        self.codeGenClassName = None
        self.codeGenLicense   = None
        self.codeGenFileName  = None
        self.codeGenYourName  = None
        self.codeGenDes       = None
        self.codeGenDesYN     = None
        self.codeGenIncrease  = None

        self.argsDict         = argsDict

        self.dealPara()

    def dealPara(self):
        self.dbgPrint(self.argsDict)

        self.codeGenIncrease  = self.argsDict.get('i',   None)
        if self.codeGenIncrease:
            argsDictLast = cgBasic.shellProcesser().loadShellParaDict()
            self.dbgPrint('lastJsonPara' + str(argsDictLast))
            argsDictLast.update(self.argsDict)
            self.argsDict = argsDictLast
            self.dbgPrint('nowJsonPara' + str(self.argsDict) )

        self.codeGenMaterial  = self.argsDict.get('m',    None)
        self.codeGenFormat    = self.argsDict.get('f',    None)
        self.codeGenLanguage  = self.argsDict.get('l',    None)
        self.codeGenUnitFile  = self.argsDict.get('uf',   None)
        self.codeGenClassName = self.argsDict.get('c',    None)
        self.codeGenLicense   = self.argsDict.get('li',   None)
        self.codeGenFileName  = self.argsDict.get('cf',   None)
        self.codeGenDes       = self.argsDict.get('des',  None)
        self.codeGenYourName  = self.argsDict.get('n',    None)
        self.codeGenFloader   = self.argsDict.get('fl',   None)
        self.codeGenAddDictch = self.argsDict.get('adch', None)
        self.codeGenAddDictcs = self.argsDict.get('adcs', None)

        cgBasic.shellProcesser().saveShellParaDict(self.argsDict)

    def grepFromFile(self):
        if self.codeGenMaterial == 'file':
            pass

    def generateUnit(self):
        unittask = codeGenFactory(self.argsDict).factory()
        unittask.generateUnit()

    def generateSys(self):
        systask = codeGenFactory(self.argsDict).factory()
        systask.generateSys()

    def generate(self):
        self.dbgPrint('generating...')
        self.grepFromFile()
        if self.codeGenFormat == 'unit':
            self.generateUnit()
        elif self.codeGenFormat == 'system':
            self.generateSys()
        
class codeGenFactory(cgBasic.c_cgbasic):
    def __init__(self, argsDict):
        cgBasic.c_cgbasic.__init__(self)
        self.product          = None
        self.codeGenUnitFile  = None
        self.codeGenClassName = None
        self.codeGenLicense   = None
        self.headerStr        = ''
        self.yourname         = None
        self.codeGenDes       = None

        self.desMake          = ''

        self.argsDict         = argsDict

        self.dealParas()

    def dealParas(self):
        self.product            = self.argsDict.get('l',    None)
        self.codeGenUnitFile    = self.argsDict.get('uf',   None)
        self.codeGenClassName   = self.argsDict.get('c',    None)
        self.codeGenLicense     = self.argsDict.get('li',   None)
        self.yourname           = self.argsDict.get('n',    None)
        self.codeGenDes         = self.argsDict.get('des',  None)
        self.codeGenFloader     = self.argsDict.get('fl',   None)
        self.codeGenAddDictch   = self.argsDict.get('adch', None)
        self.codeGenAddDictcs   = self.argsDict.get('adcs', None)

    def factory(self):
        if self.product in 'c':
            from codeGenD.usrMethod import codeGenC
            return codeGenC.codeGenFactoryC( self.argsDict )
        elif str(self.product) in 'python':
            from codeGenD.usrMethod import codeGenPy
            return codeGenPy.codeGenFactoryP( self.argsDict )
        elif str(self.product) in 'cpp':
            from codeGenD.usrMethod import codeGenCpp
            return codeGenCpp.codeGenFactoryCpp( self.argsDict )
        else:
            self.dbgPrint('not a support language...')

    def makeDes(self):
        self.desMake = ''
        self.desMake = str( self.codeGenDes )

    def codeGenMkdir(self, dirStr):
        try:
            self.dbgPrint('1-' + dirStr)
            fList = str(dirStr).split('/')
            self.dbgPrint('2-' + str(fList))
            tmpStr = ''
            for i in fList:
                if not tmpStr:
                    tmpStr += str(i)
                else:
                    tmpStr += '/' + str(i) 
                self.dbgPrint('3-' + tmpStr)
                try:
                    os.mkdir(tmpStr)
                except:
                    pass
        except:
            pass

    def generateReadme(self, locationStr):
        with open(locationStr+'readme.md', 'w+') as readmeFile:
            readmeFile.write(readmeStrMaterial)

    def generateLicense(self, locationStr):
        if str(self.codeGenLicense) == 'MIT':
            self.dbgPrint('generate license mit')
            with open(locationStr+'LICENSE', 'w+') as licenseFile:
                licenseFile.write(licenseStr)
        elif str(self.codeGenLicense) == 'apache':
            self.dbgPrint('generate license apache')
            with open(locationStr+'LICENSE', 'w+') as licenseFile:
                licenseFile.write(licenseStrApache)
        elif str(self.codeGenLicense) == 'gnu3':
            self.dbgPrint('generate license gnu3')
            with open(locationStr+'LICENSE', 'w+') as licenseFile:
                licenseFile.write(licenseStrGNU3)

    def generateGitIgnore(self, locationStr):
        with open(locationStr+'.gitignore','w+') as gitignoreFile:
            gitignoreFile.write('designLog/')

    def header(self):
        # timedate,etc
        pass

    def generateUnit(self):
        pass

    def generateSys(self):
        pass
