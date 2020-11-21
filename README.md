# codeGenD

a simple module designed for code generation

## license
```
MIT License

Copyright (c) 2020 devTools

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## language support

1. cpp
2. c
3. python

## code generation mode support

1. project generation mode
   1. c(including makefile, etc)
   2. cpp(makefile, etc)
   3. python
2. single source code file generation

## install codeGenD

```shell
pip install codeGenD
```

or

```shell
make intall
```

or 
```python
python setup.py install
```

or

run install.bat (in windows cmd or powershell)

## details

1. license generate
2. headers generate including time, date, description, author, etc
3. code auto formatting
4. multi language code block template provided

```
├── codeGenCpp.sh
├── codeGenD
│   ├── basic
│   │   ├── cgBasic.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── interface
│   │   ├── __init__.py
│   │   └── interface.py
│   ├── test
│   │   ├── __init__.py
│   │   └── test.py
│   ├── usrLib
│   │   ├── cDict.json
│   │   ├── codeUnitMethod.py
│   │   ├── cppDict.json
│   │   ├── dictCpp.py
│   │   ├── dictC.py
│   │   ├── dictProvider.py
│   │   ├── dictPython.py
│   │   ├── __init__.py
│   │   ├── pyDict.json
│   │   └── snippts.py
│   └── usrMethod
│       ├── codeGenCpp.py
│       ├── codeGenC.py
│       ├── codeGenMethod.py
│       ├── codeGenPy.py
│       ├── __init__.py
│       └── readmeMaterial.py
├── codeGenD.py
├── codeGenPy.sh
├── codeGen.sh
├── install.bat
├── LICENSE
├── makefile
├── MANIFEST.in
├── pack.bat
├── README.md
├── requirements.txt
├── setup.py
└── test.py
```

## use case

import module
```python
import codeGenD as cg

cgObj = cg.cdict(
    {
        'main':\
'''
@ret_type  @func_name  ( @paralist  )
{
    @body 
}
''',
        'ret_type' :'int',
        'func_name':'func_name_add',
        'paralist' :'int a, int b',
        'body'     :'return a+b',
    }
)

tmp_str = cgObj.parse('main')
print(tmp_str)
```

__add__ method:

```python
import codeGenD as cg

cgObj = cg.cdict(
    {
        'main':\
'''
@ret_type  @func_name  ( @paralist  )
{
    @body 
}
''',
        'ret_type' :'int',
        'func_name':'func_name_add',
        'paralist' :'int a, int b',
        'body'     :'return a+b',
    }
)

cgObj += {
    'func_name':'usr_add',
    'ret_type' :'unsigned int',
}

print(cgObj)
tmpStr = cgObj.parse('main')
print(tmpStr)
```

```python
codeGenD.provide()
'''
para:
whichLan = 'c',      fileNameIn = None
           'python',
           'cpp',
'''
```
this method loads a codeGenD.cdict object from a json file, that stores code snippts of certain language.
for example : in cDict.json
```python
{
    "default": {
        "headers": {
            "main": "\n@headStr \n#ifndef _@unitFileName _H_\n#define _@unitFileName _H_\n/* dependency\n*/\n@dependency \n/* macro\n*/\n@macro \n/* enum\n*/\n@enum \n/* struct\n*/\n#pragma pack(@packa )\n@struct \n#pragma pack(@packb )\n\n/* global declare\n*/\n@global \n\n/* interface\n*/\n@someDeclare \n\n#endif /* _@unitFileName _H_ */\n",
            "headStr": " ",
            "unitFileName": " ",
            "dependency": " ",
            "macro": " ",
            "enum": " ",
            "struct": " ",
            "packa": "1",
            "packb": " ",
            "global": " ",
            "someDeclare": " "
        },
        "source": {
            "main": "\n@headStr \n/* dependency\n*/\n@dependency \n/* macro\n*/\n@macro \n/* enum\n*/\n@enum \n/* struct\n*/\n#pragma pack(@packa )\n@struct \n#pragma pack(@packb )\n\n/* global declare\n*/\n@global \n\n/* local var\n*/\n@localvar \n\n/* interface\n*/\n@someDef \n\n",
            "headStr": " ",
            "dependency": " ",
            "macro": " ",
            "enum": " ",
            "struct": " ",
            "packa": "1",
            "packb": " ",
            "global": " ",
            "localvar": " ",
            "someDef": " "
        },
        "enum": {
            "main": "\ntypedef enum E_@code1 {\n    @enumDef \n}T_E_@code1 ;\n",
            "code1": "UNTITLED",
            "enumDef": " "
        },
        "struct": {
            "main": "\ntypedef struct E_@code1 {\n    @structDef \n}T_E_@code1 ;\n",
            "code1": "UNTITLED",
            "structDef": " "
        },
        "func": {
            "main": "\n@out  @funcName ( @paraList  )\n{\n    @codeBlock \n}\n",
            "mainSide": "\n@out  @funcName ( @paraList  );\n",
            "out": "unsigned int",
            "paraList": "unsigned int input",
            "funcName": " ",
            "codeBlock": " "
        },
        "include": {
            "main": "#include \"@fileName \" \n",
            "fileName": "untitled.h"
        }
    }
}
```

fileNameIn can be a certain file path, if left blank, will return a default cdict object from usrLib/*.json

```python
codeGenD.store(tmpDict)
'''
para:
dictIn, fileName='untitled.json'
'''
```

store cdict object as a json file

```python
tmpDict = codeGenD.provide()
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
'''
codeDict, targetStr = 'main', Mode='full' or 'half'
'''
# Mode = 'half' means don't fill a space in unsolve target, left it as it were
print(tmpStr)
codeGenD.out(tmpStr) # output a file, default fileName = 'untitled.src'
```

fill codeGenD dict object and parse it

```python
codeGenD.generate(m='argv', f='system', l='c', li='gnu3', n='untitled', fl='floader_1 floader_2 gener/floader_3')
codeGenD.generate(m='argv', f='unit',   l='c', n='david', uf='test', des='this is a test, see what happen')
'''
para
-m Material argv or file
   argv:
   -f  Format   unit or system      unit->just src file / system->project
   -l  language c or cpp or python
      unit:
      -uf   unitFileName
      -adch dict added
      -adcs dict added
      -li   license MIT gnu3 apache
      -des  description
      sys:
      -li license MIT gnu3 apache
      -fl floader list of src

      -n author name   project name in python option

   file:
      -cf codeGenFileName
-i increaseMode
'''
```

generate project or src file

see more by using:

```python
import codeGenD as cg

help(cg)
```

