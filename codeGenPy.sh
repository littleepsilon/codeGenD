codeGenDir=$(cd "$(dirname "$0")"; pwd)

cmdStr="python ${codeGenDir}/codeGenD.py"

${cmdStr} -m argv -f unit -l python -uf test -des test Description on this line -n untitled
${cmdStr} -m argv -f system -l python -li MIT -n untitled -fl floader_1 floader_2