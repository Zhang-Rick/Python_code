#######################################################
#    Author:      <Linfeng Zhang>
#    email:       <zhan2642@purdue.edu>
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/09/2019>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import math
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('∼ee364/DataFolder/Prelab01')



def find(pattern):
     with open('sequence.txt') as file:
         testsite_array = file.readlines()
     i = 0#sequence index
     j = 0#find index
     array = []
     test = list(str(testsite_array))
     while i < len(test) - len(pattern) + 1:
         x = 0
         a = 0
         print("1")
         while test[i + x] == pattern[j + x] or pattern[j + x] == 'x':
              if x == len(pattern) - 1  :
                  n = 0
                  a = 0

                  answer = 0
                  print("i =",i," x = ",x," n = ",n)
                  while n < len(pattern):
                      print("3")
                      answer += int(test[i + x - n]) * pow(10,n)
                      print("answer",answer)
                      n += 1
                  array.append(answer)
                  a += 1
                  break
              x += 1
         i += 1
     print(array)
     return array
def getStreakProduct(sequence, maxSize, product):
    i = 0
    j = 1
    array = []
    seq = []
    sequence = int(sequence)
    #print(sequence)
    while int(sequence) > 0:
        result = int(sequence) % 10
        #print(result)
        seq.append(result)
        sequence /= 10
    seq = seq[::-1]
    print(seq)
    while i < len(seq)-1:
        j = 1
        pro = seq[i]*seq[i+ j]
        if pro == product:
            answer = seq[i] * 10 + seq[i + j]
            array.append(answer)
        print("i = ",i," j = ",j)
        while (pro < product) and j < maxSize-1 and i + j < len(seq) - 1:
            pro *= seq[i + j + 1]
            j += 1
            answer = 0
            if pro == product:
               z=0
               while j >= 0:
                   answer += seq[i+j] * pow(10,z)
                   z += 1
                   j -= 1
               array.append(answer)
        i+=1
    print(array)
    return array

def writePyramids(filePath,baseSize,count,char):
    f = open(filePath,"w")
    i = 0
    j = 0
    while (i < (baseSize-1)/2 + 2):
        while j < (int((baseSize - 1)/2 ) + 1 - i):
            print(1)
            f.write(" ")
            j += 1
        j = 0
        f.write(char*(1+2*i))
        f.write("\n")
        i += 1

    return



def getStreaks(sequence, letters):
    i = 0
    j = 0
    array = []
    array1 = []
    #print(1)
    while i < len(sequence):
        #print(2)
        while j < len(letters):
            #print(3)

            if sequence[i] == letters[j] and i < len(sequence):
                array =''
                while sequence[i] == letters[j] and i < len(sequence):
                    #print(4)

                    array += sequence[i]
                    #print(sequence[i])
                    i += 1
                array1.append(array)
                #print("array1",array1)
                j = 0
            j += 1
        j = 0
        i += 1

    #print(array1,'1')
    return array1

if __name__ =="__main__":
    #find("x8")
    #getStreakProduct("11114822",5,32)
    writePyramids('pyramis15.txt',15,5,'*')
    #getStreaks("AAASSSSSSAPP","SAQT")