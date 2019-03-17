#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Prelab09
# Write  your  code  here
componentIDa=$1
componentIDc=$2
circuitFiles=$(ls $DataPath"/circuits/")
#echo $circuitFiles
for circuitFile in $circuitFiles
do
 #echo $circuitFile
 a=$(grep -E $1 $DataPath"/circuits/"$circuitFile)
 b=${a:2:8}
 c=$(grep -E $2 $DataPath"/circuits/"$circuitFile)
 d=${c:2:8}	
 #echo [ "$b" == "$componentIDa" ]
 if [ "$b" == "$componentIDa" ]
 then
   Circuita+=${circuitFile:8:7}' '
 fi
 if [ "$d" == "$componentIDc" ]
 then
   Circuitc+=${circuitFile:8:7}' '
 fi

 #echo $Circuita
done
a1=$(echo $Circuita | sort -u | wc -w)
a2=$(echo $Circuitc | sort -u | wc -w)
if [ "$a1" -gt "$a2" ]
then 
 echo $1
else 
 echo $2
fi
