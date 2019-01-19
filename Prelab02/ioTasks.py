#######################################################
#    Author:      <Your  Full Name >
#    email:       <Your  Email >
#    ID:           <Your  course ID , e.g. ee364j20 >
#    Date:         <Start  Date >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from os import listdir
from os.path  import isfile, join

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab02')


def getMaxDifference(symbol):
    symbol += ".dat"
    filename = os.path.join(DataPath, symbol)
    with open(filename, 'r') as file:
        line = file.read().splitlines()

    i = 2
    max_num =0
    while (i < len(line) - 2):
        array = line[i].split(',')

        if max_num < (float(array[4]) - float(array[5])):
            max_num = float(array[4]) - float(array[5])
            date = array[0]
        i += 1

    print(max_num,date)
    return date
        #     line = file.readlines()
def getGainPercent(symbol):
     symbol += ".dat"
     with open(symbol,'r') as file:
         line = file.read().splitlines()
     i = 2
     n = 0
     while (i < len(line) - 2):
         array = line[i].split(',')
         if (float(array[1]) - float(array[3])) > 0.0:
             n += 1
         i += 1
     print(n)
     k = n /(len(line) - 2) * 100
     print(k)
     return k

def getVolumeSum(symbol, date1, date2):
    if str(date1) >= str(date2):
        return None
    else:
        symbol = symbol + ".dat"
        with open(symbol, 'r') as file:
            line = file.read().splitlines()
        start = findDate(symbol,date1)
        finish = findDate(symbol,date2)
        print(start,finish)
        i = start
        sum = 0
        if (start < finish):
            while i < finish + 1:
                array = line[i].split(',')
                print(array)
                #array2 = array.split(',')
                sum += float(array[2])
                i += 1
        else:
            while i > finish - 1:
                array = line[i].split(',')
                print(array)
                sum += float(array[2])
                i -= 1
        print(sum)
        return  sum


def findDate(symbol,date):
    filename = os.path.join(DataPath, symbol)
    with open(filename, 'r') as file:
        line = file.read().splitlines()
    i = 2
    while(i < len(line) - 2):
        array = line[i].split(',')
        if (str(array[0])==str(date)):
            break
        i += 1
    return i

def findYear(symbol, year):
    filename = os.path.join(DataPath, symbol+'.dat')
    with open(filename , 'r') as file:
        line = file.read().splitlines()
    i = 2
    array =[]
    while(i < len(line) - 2):
        array = line[i].split(',')
        if year == array.split('/')[0]:
            array.append(i)
    answer = [array[0],array[len(array) - 1]]
    print(answer)
    return answer



def getBestGain(date):

    onlyfiles = [f for f in listdir(DataPath) if isfile(join(DataPath,f))]
    #print(len(onlyfiles))
    array = []
    i = 0
    maximum = 0
    while i < len(onlyfiles):
        with open(onlyfiles[i], 'r') as file:
            line = file.read().split()
        print(line)
        j = findDate(onlyfiles[i],date)
        data = line[j].split(',')
        #print(data)
        percent = (float(data[1]) - float(data[3]))/float(date[3]) * 100
        if maximum < percent:
            maximum = percent
            l = i
        i += 1

    return(onlyfiles[l])

#This  block  is  optional
if __name__  == "__main__":
    #getMaxDifference('AAPL')
    #getMaxDifference('AMZN')
    #getMaxDifference('FB')
    #getMaxDifference('MSFT')
    #getMaxDifference('TSLA')
    #getGainPercent('AAPL')
    #getBestGain('2018/12/14')
    findYear('APPL',2019)
    #findDate('AAPL.dat','2018/12/14')

    #getVolumeSum('AAPL', '2019/01/02', '2019/01/11')

    # Write  anything  here to test  your  cd