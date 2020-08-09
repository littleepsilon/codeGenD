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
from time import strftime, localtime
# import 3rd-part Moudle

# import usrModule
from codeGenD.usrMethod import codeGenMethod
from codeGenD.usrLib    import codeUnitMethod
from codeGenD.usrLib    import dictProvider

class codeGenFactoryP(codeGenMethod.codeGenFactory):

    def generateUnit(self):
        self.generatePy()

    def generateSys(self):
        self.generateWorkspace()
        self.generateInitPy('pySys/'+str(self.yourname)+'/')
        self.generateMainPy('pySys/')
        self.generateRequirements('pySys/')
        self.generateSetup('pySys/')
        self.generateGitIgnore('pySys/')
        self.generateReadme('pySys/')
        self.generateLicense('pySys/')

    def generateWorkspace(self):
        self.codeGenMkdir('pySys')
        self.codeGenMkdir('pySys/'+str(self.yourname))
        self.codeGenMkdir('pySys/designLog')
        if self.codeGenFloader:
            floaderList = str(self.codeGenFloader).split()
            for singleFloader in floaderList:
                self.codeGenMkdir('pySys/'+str(self.yourname) + '/' + singleFloader)
                self.generateInitPy('pySys/'+str(self.yourname)+'/' + singleFloader + '/')

    def generateRequirements(self,dirname):
        with open(dirname+'requirement.txt', 'w+') as requirementFile:
            requirementFile.close()

    def generateInitPy(self, dirname):
        pyStrDict = {}
        pyStrDict['main'] = \
'''
# -*- coding:utf-8 -*-
@headers 
# import pyModule
import sys
import os

# import 3rd-part Moudle

# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '' )

# import usrModule

'''
        pyStrDict['headers']  = str(self.header())
        tmpStr = codeUnitMethod.codeUnit().parse(pyStrDict)

        with open(dirname + '__init__.py', 'w+') as initPyFile:
            initPyFile.write(tmpStr)

    def generateMainPy(self, dirname):
        pyStrDict = {}
        pyStrDict['main'] = \
'''
# -*- coding:utf-8 -*-
@headers 
# import pyModule
import sys
import os

# import 3rd-part Moudle

# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '' )

# import usrModule

import @yourName 

if __name__ == '__main__':
    pass

'''
        pyStrDict['yourName'] = str(self.yourname)
        pyStrDict['headers']  = str(self.header())
        tmpStr = codeUnitMethod.codeUnit().parse(pyStrDict)
        with open(dirname+'main.py', 'w+') as mainPyFile:
            mainPyFile.write(tmpStr)

    def generateSetup(self,dirname):
        setupFile = open(dirname+'setup.py', 'w+')
        setupFile.close()

    def generatePy(self):
        pySrcDict = dictProvider.cDict( dictProvider.provide( whichLan = 'python' ) )
        pySrcDict = dictProvider.cDict( pySrcDict['default']['layout'] )

        plusDict    = {
            'headers'      : str(self.header()),
            'pyModules'    : ' ',
            'import1'      : ' ',
            'import2'      : ' ',
            'import3'      : ' ',
            'subjectBlock' : ' ',
        }

        pySrcDict += plusDict
        if self.codeGenAddDictcs:
            pySrcDict += self.codeGenAddDictcs

        tmpStr = codeUnitMethod.codeUnit().parse(pySrcDict)

        dirName = str('pySrc/')
        self.codeGenMkdir(dirName)
        with open(dirName + str(self.codeGenUnitFile)+'.py', 'w+') as pyFile:
            pyFile.write(tmpStr)

    def header(self):
        self.makeDes()
        headerDict         = {}
        headerDict['main'] = \
'''
#
# time:        @time 
# date:        @date 
# description: @des 
# author:      @author 

'''
        headerDict['time']   = strftime( "%H:%M",localtime() )
        headerDict['date']   = strftime( "%Y-%m-%d", localtime() )
        headerDict['des']    = str(self.desMake)
        headerDict['author'] = str(self.yourname)

        headerTask           = codeUnitMethod.codeUnit()
        return headerTask.parse(headerDict)