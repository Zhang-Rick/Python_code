#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >wwwwwww
#######################################################
DataPath=~ee364/DataFolder/Prelab09
# Write  your  code  here
project="$1"
circuits=$(grep -E $prxoject $DataPath"/maps/projects.dat" | cut -f5 -d ' ' | sort -u)
for circuit in $circuits
do
 #echo $circuit
 name='circuit_'$circuit'.dat'
 lines+=$(grep -E '[0-9]{5}[-][0-9]{5}' $DataPath'/circuits/'$name)
 lines+=' '
done
#echo $lines

for line in $lines
do
 grep -E $line $DataPath"/maps/students.dat" | cut -f1,2,3 -d ' '
done | sort -u


