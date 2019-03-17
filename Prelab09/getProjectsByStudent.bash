#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Prelab09
# Write  your  code  here


studentID=$(grep -E "$1" $DataPath"/maps/students.dat"| cut -f2 -d '|'| cut -f16 -d ' ')

circuitFiles=$(ls $DataPath"/circuits")

for circuitFile in $circuitFiles
 do
 student=$(grep -E $studentID $DataPath"/circuits/"$circuitFile)
 #echo [ "$student" == "$studentID" ]
 if [ "$student" == "$studentID" ]
 then
  circuit=${circuitFile:8:7}
  grep -E $circuit $DataPath"/maps/projects.dat" | cut -f15 -d ' '
 fi
done | sort -u


