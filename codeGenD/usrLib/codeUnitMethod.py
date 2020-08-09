# -*- coding:utf-8 -*-
# 
# time:        12:10
# date:        2020-06-16
# author:      david
# description: codeUnit method
# 
# import pyModule
import sys
import re
import copy
# import os

# import 3rd-part Moudle
from codeGenD.basic  import cgBasic
# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] +'')

# import usrModule

def parse(*args, **kwargs):
	return codeUnit().parse(*args, **kwargs)

class codeUnit(cgBasic.c_cgbasic):
	def __init__(self, inputPara=None):
		cgBasic.c_cgbasic.__init__(self)
		self.para     = inputPara
		self.unitDict = None

	def parse(self, codeDict, targetStr = 'main', Mode='full'):
		self.unitDict = copy.deepcopy(codeDict)
		return self.parseCore(targetStr, Mode)

	def parseCore(self, targetStr = 'main', Mode='full'):
		return self.resolveCore( targetStr, Mode )

	def resolveCore(self, keyStr, Mode='full'):
		codeBlock = self.unitDict.get(keyStr, None)
		if not codeBlock:
			# self.dbgPrint('there is no ' + keyStr + ' block, exit')
			# sys.exit()
			if Mode == 'full':
				self.unitDict[keyStr] = ' '
				codeBlock = ' '
			else:
				return '@' + keyStr + ' '
		tmpStr    = codeBlock
		labelList = re.findall('@[a-zA-Z0-9_]*', codeBlock)
		if not labelList:
			return tmpStr
		else:
			keyList = [str(i).replace('@','') for i in labelList]
			for j in keyList:
				tmpStrReplace = self.resolveCore(j, Mode)
				# deal with format
				formatStr     = re.findall( '\n([\t ]*)'+'@'+j+' ', str(tmpStr) )
				if formatStr :
					tmpStrReplace = str(tmpStrReplace).replace( '\n', '\n' + formatStr[0] )

				tmpStr        = str(tmpStr).replace('@'+j+' ', tmpStrReplace)
			return tmpStr