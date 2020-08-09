# -*- coding:utf-8 -*-

#
# time:        02:55
# date:        2020-06-22
# description: test Description on this line 
# author:      untitled


# import pyModule
# import sys
# import os

# import 3rd-part Moudle

# sys.path.append( os.path.split( os.path.realpath(__file__) )[0] + '' )

# import usrModule

cDict = {}
cDict['default'] = {}
cDict['default']['headers'] = {
    'main' : \
'''
@headStr 
#ifndef _@unitFileName _H_
#define _@unitFileName _H_
/* dependency
*/
@dependency 
/* macro
*/
@macro 
/* enum
*/
@enum 
/* struct
*/
#pragma pack(@packa )
@struct 
#pragma pack(@packb )

/* global declare
*/
@global 
/* interface
*/
@someDeclare 

#endif /* _@unitFileName _H_ */
''',
    'headStr'      : ' ',
    'unitFileName' : ' ',
    'dependency'   : ' ',
    'macro'        : ' ',
    'enum'         : ' ',
    'struct'       : ' ',
    'packa'        : '1',
    'packb'        : ' ',
    'global'       : ' ',
    'someDeclare'  : ' ',
}

cDict['default']['source'] = {
    'main':\
'''
@headStr 
/* dependency
*/
@dependency 
/* macro
*/
@macro 
/* enum
*/
@enum 
/* struct
*/
#pragma pack(@packa )
@struct 
#pragma pack(@packb )

/* global declare
*/
@global 
/* interface
*/
@someDef 

''',
    'headStr'      : ' ',
    'dependency'   : ' ',
    'macro'        : ' ',
    'enum'         : ' ',
    'struct'       : ' ',
    'packa'        : '1',
    'packb'        : ' ',
    'global'       : ' ',
    'someDef'      : ' ',
}

cDict['default']['enum'] = {
    'main' : 
'''
typedef enum E_@code1 {
    @enumDef 
}T_E_@code1 ;
''',
    'code1'  : 'untitled'.upper(),
    'enumDef': ' ',
}

cDict['default']['struct'] = {
    'main' : 
'''
typedef struct E_@code1 {
    @structDef 
}T_E_@code1 ;
''',
    'code1'    : 'untitled'.upper(),
    'structDef': ' ',
}

cDict['default']['func'] = {
    'main' : \
'''
@out  @funcName ( @paraList  )
{
    @codeBlock 
}
''',
    'mainSide' : \
'''
@out  @funcName ( @paraList  );
''',
    'out'      : 'unsigned int',
    'paraList' : 'unsigned int input',
    'funcName' : ' ',
    'codeBlock': ' '
}

cDict['default']['include'] = {
    'main' : \
'''#include "@fileName " 
''',

    'fileName' : 'untitled.h',
}
