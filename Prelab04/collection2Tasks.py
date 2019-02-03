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
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab04')

def techToID():
    filename = os.path.join(DataPath,'maps/technicians.dat')
    with open(filename) as f:
        lines = f.read().splitlines()
    i = 2
    techToIDMap = {}
    while i < len(lines):
        name = list(filter(None,lines[i].split(' ')))[0] +' '+ list(filter(None,lines[i].split(' ')))[1]
        techToIDMap[name] = list(filter(None,lines[i].split(' ')))[3]
        i += 1

    #print(techToIDMap)
    #techID = techToIDMap[techName]
    #print(techID)
    return techToIDMap

def virusToID():
    filename = os.path.join(DataPath,'maps/viruses.dat')
    with open(filename) as f:
        lines = f.read().splitlines()
    i = 2
    virusToIDMap = {}
    while i < len(lines):
        name = list(filter(None,lines[i].split(' ')))[2]
        virusToIDMap[name] = list(filter(None,lines[i].split(' ')))[0]
        i += 1
    #print(virusToIDMap)
    return virusToIDMap

def virusCost():
    filename = os.path.join(DataPath, 'maps/viruses.dat')
    with open(filename) as f:
        lines = f.read().splitlines()
    i = 2
    virusCostMap = {}
    while i < len(lines):
        name = list(filter(None, lines[i].split(' ')))[2]
        dollar = list(filter(None, lines[i].split(' ')))[4]
        cost = dollar.split('$')[1]
        virusCostMap[name] = float(cost)
        i += 1
    #print(virusCostMap)
    return virusCostMap

def getTechWork(techName):
    techToIDMap = techToID()
    TechID = techToIDMap[techName]
    virusToIDMap = virusToID()
    #print(TechID)
    onlyfiles = [f for f in listdir(DataPath + '/reports/') if isfile(join(DataPath + '/reports/', f))]
    #print(onlyfiles)
    i = 0##file index
    #techToVirusMap = {}
    virusToUnitMap = {}
    while i < len(onlyfiles):
        filename = DataPath + '/reports/' + onlyfiles[i]
        with open(filename) as f:
            lines = f.read().splitlines()
        ID = lines[0].split(' ')[2]
        if ID == TechID:
            j = 4
            while j < len(lines):
                virusIDinfile = list(filter(None,lines[j].split(' ')))[1]
                virusNumber = list(filter(None,lines[j].split(' ')))[2]
                virusNameinfile = virusToIDMap[virusIDinfile]
                #print(virusIDinfile,virusNameinfile)
                if virusNameinfile not in list(virusToUnitMap.keys()):
                    virusToUnitMap[virusNameinfile] = int(virusNumber)
                else:
                    virusToUnitMap[virusNameinfile] += int(virusNumber)
                j += 1
        i += 1
    #print(virusToUnitMap)
    return virusToUnitMap

def getStrainConsumption(virusName):
    techToIDMap = techToID()
    virusToIDMap = virusToID()
    inverseVirusToIDMap = dict(zip(virusToIDMap.values(),virusToIDMap.keys()))
    inverseTechToIDMap = dict(zip(techToIDMap.values(), techToIDMap.keys()))
    #print(inverseVirusToIDMAp,'\n',virusToIDMap)
    virusID = inverseVirusToIDMap[virusName]
    techToUnitMap = {}
    onlyfiles = [f for f in listdir(DataPath + '/reports/') if isfile(join(DataPath + '/reports/', f))]
    i = 0
    while i < len(onlyfiles):
        filename = DataPath + '/reports/' + onlyfiles[i]
        with open(filename) as f:
            lines = f.read().splitlines()
        techID = lines[0].split(' ')[2]
        techName = inverseTechToIDMap[techID]
        j = 4
        while j < len(lines):
            virusIDinfile = list(filter(None,lines[j].split(' ')))[1]
            virusNumber = list(filter(None,lines[j].split(' ')))[2]
            #print(virusID,virusIDinfile)
            if virusIDinfile == virusID:
                if techName not in techToUnitMap.keys():
                    techToUnitMap[techName] = int(virusNumber)
                else:
                    techToUnitMap[techName] += int(virusNumber)
            j += 1
        i += 1
    #print(techToUnitMap)
    return techToUnitMap

def getTechSpeeding():
    techToIDMap = techToID()
    virusToIDMap = virusToID()
    inverseVirusToIDMap = dict(zip(virusToIDMap.values(), virusToIDMap.keys()))
    inverseTechToIDMap = dict(zip(techToIDMap.values(), techToIDMap.keys()))
    virusCostMap = virusCost()

    filename = os.path.join(DataPath,'maps/technicians.dat')
    techCostMap = {}
    with open(filename) as f:
        lines = f.read().splitlines()
    i = 2#techs
    while i < len(lines):
        techName = list(filter(None,lines[i].split(' ')))[0] + ' ' + list(filter(None,lines[i].split(' ')))[1]
        #print(techName,techID)
        techCostMap[techName] = 0.00
        i += 1
    onlyfiles = [k for k in listdir(DataPath + '/reports/') if isfile(join(DataPath + '/reports/', k))]
    i = 0
    while i < len(onlyfiles):
        #print(i,len(onlyfiles))
        filename1 = DataPath + '/reports/' + onlyfiles[i]
        with open(filename1) as f:
            line = f.read().splitlines()
        ID = line[0].split(' ')[2]
        Name = inverseTechToIDMap[ID]
        j = 4
        while j < len(line):
            #print(list(filter(None,line[j].split(' '))))
            circuit = list(filter(None,line[j].split(' ')))[1]
            price = virusCostMap[circuit]*int(list(filter(None,line[j].split(' ')))[2])
            techCostMap[Name] += round(price,2)
            j += 1
        techCostMap[Name] = round(techCostMap[Name], 2)
        i += 1
    #print(techCostMap)
    return techCostMap

def getStrainCost():
    techToIDMap = techToID()
    virusToIDMap = virusToID()
    inverseVirusToIDMap = dict(zip(virusToIDMap.values(), virusToIDMap.keys()))
    inverseTechToIDMap = dict(zip(techToIDMap.values(), techToIDMap.keys()))
    virusCostMap = virusCost()
    virusTotalCostMap ={}
    filename = os.path.join(DataPath,'maps/viruses.dat')
    with open(filename) as f:
        lines = f.read().splitlines()
    i = 2#techs
    while i < len(lines):
        virusID1 = list(filter(None,lines[i].split(' ')))[2]
        virusName = virusToIDMap[virusID1]
        #print(virusName)
        virusTotalCostMap[virusName] = 0.0
        i += 1
    onlyfiles = [k for k in listdir(DataPath + '/reports/') if isfile(join(DataPath + '/reports/', k))]
    i = 0
    while i < len(onlyfiles):
        filename1 = DataPath + '/reports/' + onlyfiles[i]
        with open(filename1) as f:
            line = f.read().splitlines()
        j = 4
        while j < len(line):
            virusID2 = list(filter(None,line[j].split(' ')))[1]
            #print(list(filter(None,line[j].split(' '))))
            virusName1 = virusToIDMap[virusID2]
            #print(float(list(filter(None,line[j].split(' ')))[2]))
            virusTotalCostMap[virusName1] +=  virusCostMap[list(filter(None,line[j].split(' ')))[1]]* float(list(filter(None,line[j].split(' ')))[2])
            j += 1
        #print(virusName1,virusTotalCostMap[virusName1])
        i += 1
    i = 0
    while i < len(virusTotalCostMap.keys()):
        virusTotalCostMap[list(virusTotalCostMap.keys())[i]] = round(virusTotalCostMap[list(virusTotalCostMap.keys())[i]], 2)
        i += 1

    #print(virusTotalCostMap)
    return  virusTotalCostMap

def getAbsentTechs():
    techToIDMap = techToID()
    inverseTechToIDMap = dict(zip(techToIDMap.values(), techToIDMap.keys()))
    techArray = set(techToIDMap.keys())
    #print(techArray)
    onlyfiles = [k for k in listdir(DataPath + '/reports/') if isfile(join(DataPath + '/reports/', k))]
    i = 0
    while i < len(onlyfiles):
        filename1 = DataPath + '/reports/' + onlyfiles[i]
        with open(filename1) as f:
            line = f.read().splitlines()
        ID = line[0].split(' ')[2]
        Name = inverseTechToIDMap[ID]
        if Name in techArray:
            techArray.remove(Name)
        i += 1
    #print(techArray,len(techArray))
    return techArray

def getUnusedStrain():
    virusToIDMap = virusToID()
    inverseVirusToIDMap = dict(zip(virusToIDMap.values(), virusToIDMap.keys()))
    virusArray = set(virusToIDMap.values())
    #print(len(virusArray))
    onlyfiles = [k for k in listdir(DataPath + '/reports/') if isfile(join(DataPath + '/reports/', k))]
    i = 0
    while i < len(onlyfiles):
        filename1 = DataPath + '/reports/' + onlyfiles[i]
        with open(filename1) as f:
            line = f.read().splitlines()
        j = 4
        while j < len(line):
            virusID = list(filter(None,line[j].split(' ')))[1]
            virusName = virusToIDMap[virusID]
            #print(virusName)
            if virusName in virusArray:
                virusArray.remove(virusName)
            j += 1
        i += 1
    #print(virusArray,'\n',len(virusArray))
    return virusArray










#if __name__  == "__main__":
    #techToID()
    #virusToID()
    #filename = os.path.join(DataPath,'maps/technicians.dat')
    #with open(filename) as f:
    #    lines = f.read().splitlines()
    #i = 2
    #while i < len(lines):
    #    name = lines[i].split(' ')[0] + ' ' + lines[i].split(' ')[1]
    #    getTechWork(name)
    #    i += 1
    #getStrainConsumption('Deltavirus')
    #getTechSpeeding()
    #virusCost()
    #getStrainCost()
    #getAbsentTechs()
    #getUnusedStrain()