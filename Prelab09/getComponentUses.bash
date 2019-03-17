#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Prelab09
# Write  your  code  here
componentID=$1
circuitFiles=$(ls $DataPath"/circuits/")
#echo $circuitFiles
for circuitFile in $circuitFiles
do
 #echo $circuitFile
 a=$(grep -E $1 $DataPath"/circuits/"$circuitFile)
 b=${a:2:8}
 #echo [ "$b" == "$componentID" ]
 if [ "$b" == "$componentID" ]
 then
   Circuit+=${circuitFile:8:7}' '
 fi
 #echo $Circuit
done
echo $Circuit | sort -u | wc -w
