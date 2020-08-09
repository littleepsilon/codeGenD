codeGenDir=$(cd "$(dirname "$0")"; pwd)

cmdStr="python ${codeGenDir}/codeGenD.py"

${cmdStr} -m argv -f system -l cpp -li MIT -n untitled -fl floader_1 floader_2 gener/floader_3

${cmdStr} -m argv -f unit -l cpp -uf brand -des test Description on this line -n david
mv cppSrc/*.cpp cppSys/floader_1/src/
mv cppInc/*.h cppSys/floader_1/inc/

${cmdStr} -i -uf emerald -des happy to see you here 
mv cppSrc/*.cpp cppSys/floader_2/src/
mv cppInc/*.h cppSys/floader_2/inc/

${cmdStr} -i -uf sapphire -des happy to see you here again
mv cppSrc/*.cpp cppSys/gener/floader_3/src/
mv cppInc/*.h cppSys/gener/floader_3/inc/