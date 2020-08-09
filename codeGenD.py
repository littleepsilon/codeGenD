# -*- coding:utf-8 -*-
#
# time:        19:32
# date:        2020/06/06
# description: none
# author:      david
# 

# import module
import sys
import os
import logging

# import path

# import 3rd-part moudle 

# import usrModule
sys.path.append( os.path.split( os.path.realpath(__file__) )[0])
import codeGenD
from codeGenD.basic                   import cgBasic
from codeGenD.usrMethod.codeGenMethod import codeGenMethod

if __name__ == "__main__":
    logging.basicConfig( level=logging.DEBUG, filename='codeGen.log', filemode='w', format='%(asctime)s : %(message)s' )

    cmdParaStr = sys.argv[1:]
    if len(cmdParaStr) == 0:
        print('no input para, exit')
        sys.exit()

    shell            = cgBasic.shellProcesser()
    shell.dbgMode    = True
    shell.cmdStrList = cmdParaStr
 
    ret = shell.parser()
    if not ret:
        sys.exit()

    task = codeGenMethod(ret)
    task.generate()

    print('end')