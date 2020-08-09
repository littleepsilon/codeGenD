codeGenDir=$(cd "$(dirname "$0")"; pwd)

cmdStr="python ${codeGenDir}/main.py"

${cmdStr} -m argv -f system -l c -li MIT -n untitled -fl floader_1 floader_2 gener/floader_3

${cmdStr} -m argv -f unit -l c -uf brand -des test Description on this line -n untitled
mv csrc/*.c cSys/floader_1/src/
mv cinc/*.h cSys/floader_1/inc/

${cmdStr} -m argv -f unit -l c -uf brand -des test Description on this line -n untitled
mv csrc/*.c cSys/floader_2/src/
mv cinc/*.h cSys/floader_2/inc/

${cmdStr} -m argv -f unit -l c -uf brand -des test Description on this line -n untitled
mv csrc/*.c cSys/gener/floader_3/src/
mv cinc/*.h cSys/gener/floader_3/inc/
