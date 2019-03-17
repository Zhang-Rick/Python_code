#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Prelab09
# Write  your  code  here
studentname=$1

studentID=$(grep -E "$studentname" $DataPath"/maps/students.dat"| cut -f2 -d '|'| cut -f16 -d ' ')

circuitFiles=$(ls $DataPath"/circuits")

for circuitFile in $circuitFiles
do
 student=$(grep -E $studentID $DataPath"/circuits/"$circuitFile)
 #echo [ "$student" == "$studentID" ]
 if [ "$student" == "$studentID" ]
 then
  echo ${circuitFile:8:7}

 fi
done | sort -u
