# codeGenD

a simple tool designed for code generate

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

## code Generate mode support

1. project generate
   1. c(including makefile, etc)
   2. cpp(makefile, etc)
   3. python
2. single source code file generate

## install

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

run install.bat (in windows)

## details

1. license generate
2. headers generate including time, date, description, author, etc
3. code auto formatting
4. multi language code block template json file	

```
├── codeGenCpp.sh
├── codeGenD
│   ├── basic
│   │   ├── cgBasic.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── interface
│   │   ├── __init__.py
│   │   └── interface.py
│   ├── test
│   │   ├── __init__.py
│   │   └── test.py
│   ├── usrLib
│   │   ├── cDict.json
│   │   ├── codeUnitMethod.py
│   │   ├── cppDict.json
│   │   ├── dictCpp.py
│   │   ├── dictC.py
│   │   ├── dictProvider.py
│   │   ├── dictPython.py
│   │   ├── __init__.py
│   │   ├── pyDict.json
│   │   └── snippts.py
│   └── usrMethod
│       ├── codeGenCpp.py
│       ├── codeGenC.py
│       ├── codeGenMethod.py
│       ├── codeGenPy.py
│       ├── __init__.py
│       └── readmeMaterial.py
├── codeGenD.py
├── codeGenPy.sh
├── codeGen.sh
├── dist
│   └── codeGenD-0.0.7.tar.gz
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

## use

```python
codeGenD.provide()
'''
para:
whichLan = 'c', fileNameIn = None
'''
```

return a cdict object, default : see codeGenD/usrLib/*.json

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
print(tmpStr)
codeGenD.out(tmpStr)
```

fill codeGenD dict object and parse it

```python
codeGenD.generate(m='argv', f='system', l='c', li='gnu3', n='untitled', fl='floader_1 floader_2 gener/floader_3')
codeGenD.generate(m='argv', f='unit',   l='c', n='david', uf='test', des='this is a test, see what happen')
'''
para
-m Material argv or file
   argv:
   -f  Format   unit or system
   -l  language c or cpp or python
      unit:
      -uf   unitFileName
      -adch dict added
      -adcs dict added
      -li   license MIT gnu3 apache
      -des  description
      sys:
      -li license MIT gnu3 apache
      -fl floaderList

      -n author name

   file:
      -cf codeGenFileName
-i increaseMode
'''
```

generate project

```python
tmpDict2 = codeGenD.cdict(
   {
      'main' : \
'''
@haha 
@hehe 
test 
    haha
    @kict_ 
''',
      'kict_' : 'test'
   }
)
    tmpDict2 += {'kict' : 'quite', 'hehe' : 'james'}
    codeGenD.out ( tmpDict2.parse( Mode='half' ), fileName='test.src' )
    codeGenD.out ( tmpDict2.parse() )
```

support __add__ method

```python
codeGenD.app(n='myApp')
'''
generate a usr codeGenD app
n='appName', li='MIT' or 'apache' or 'gnu3'
'''
```

