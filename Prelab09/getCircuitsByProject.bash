#! /bin/bash
#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
DataPath=~ee364/DataFolder/Prelab09
# Write  your  code  here

Project=$1
grep -E $Project $DataPath"/maps/projects.dat" | cut -f5 -d ' ' | sort -u
