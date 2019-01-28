#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/19/2019 >
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

    #print(max_num,date)
    return date
        #     line = file.readlines()
def getGainPercent(symbol):
     symbol += ".dat"
     filename = os.path.join(DataPath, symbol)
     with open(filename,'r') as file:
         line = file.read().splitlines()
     i = 2
     n = 0
     while (i < len(line)):
         array = line[i].split(',')
         if (float(array[1]) > float(array[3])):
             n += 1
         i += 1
     #print(n)
     k = n /(len(line)-2) * 100
     #print(k)
     return k

def getVolumeSum(symbol, date1, date2):

        symbol = symbol + ".dat"
        filename = os.path.join(DataPath, symbol)
        with open(filename, 'r') as file:
            line = file.read().splitlines()
        start = findDate(symbol,date1)
        finish = findDate(symbol,date2)
        if start <= finish:
            return None
        #print(start,finish)
        i = start
        sum = 0.0
        #print(line[finish].split(',')[2],line[start].split(',')[2])

        while i > finish - 1:
            array = line[i].split(',')
            sum += float(array[2])
            i -= 1
        return int(sum)







def getBestGain(date):

    onlyfiles = [f for f in listdir(DataPath) if isfile(join(DataPath,f))]
    #print(onlyfiles)
    array = []
    i = 0
    maximum = 0.0
    while i < len(onlyfiles):
        filename = os.path.join(DataPath, onlyfiles[i])
        #print(filename)
        with open(filename, 'r') as file:
            line = file.read().split()
        #print(line)
        j = findDate(onlyfiles[i],date)
        data = line[j].split(',')
        #print(data,data[3])


        percent = (abs(float(data[1]) - float(data[3])))/float(data[3]) * 100
        if maximum < percent:
            maximum = percent
            l = i
        i += 1

    return(maximum)

def findDate(symbol,date):
    filename = os.path.join(DataPath, symbol)
    with open(filename, 'r') as file:
        line = file.read().splitlines()
    i = 2
    while(i < len(line)):
        array = line[i].split(',')
        if (str(array[0])==str(date)):
            break
        i += 1
    return i

def findYear(symbol, year):
    filename = os.path.join(DataPath, symbol)
    with open(filename, 'r') as file:
        line = file.read().splitlines()
    i = 2
    array =[]
    array2 = []
    while(i < len(line)):
        array = line[i].split(',')
        if str(year) == array[0].split('/')[0]:

            array2.append(i)
            if str(year) != array[0].split('/')[0]:
                break
        i += 1
    answer = [array2[0],array2[len(array2) - 1]]
    return answer

def getAveragePrice(symbol,year):
    symbol += '.dat'
    [start, finish] = findYear(symbol,year)
    filename = os.path.join(DataPath, symbol)
    with open(filename, 'r') as file:
        line = file.read().splitlines()
    #print(line[start],line[finish])
    i = start
    n = 0
    DailyAve = 0
    while i < finish + 1:
        close = float(line[i].split(',')[1])
        open1 = float(line[i].split(',')[3])
        DailyAve += (close + open1) / 2
        n += 1
        i += 1
    ave = DailyAve / n


    return ave

def getCountOver(symbol,price):
    filename = os.path.join(DataPath, symbol+'.dat')
    with open(filename, 'r') as file:
        line = file.read().splitlines()
    i = 2
    n = 0
    while i < len(line):
        if(float(line[i].split(',')[1]) >= price and float(line[i].split(',')[3]) >= price and float(line[i].split(',')[4]) >= price and float(line[i].split(',')[5]) >= price):
            n += 1
        i += 1
    return n

#This  block  is  optional
#if __name__  == "__main__":
    #print(getMaxDifference('AAPL'))
    #print(getMaxDifference('AMZN'))
    #print(getMaxDifference('FB'))
    #print(getMaxDifference('MSFT'))
    #print(getMaxDifference('TSLA'))
    #print(getGainPercent('TSLA'))
    #print(getBestGain('2015/07/07'))
    #print(getAveragePrice('FB', 2014))
    #print(getCountOver('MSFT', 99.43))
    #findDate('AAPL.dat','2018/12/14')

   # print(getVolumeSum('MSFT', '2014/01/17', '2018/01/08'))
    #22110230
   # 30476834813
    # Write  anything  here to test  your  cd