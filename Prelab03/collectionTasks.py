#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/19/2019 >
#######################################################
import os      # List of  module  import  statements     # Each  one on a line
import glob
from collections import Counter

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath= os.path.expanduser('~ee364/DataFolder/Prelab03')

def getComponentCountByStudent(projectID,componentSymbol):
    projectFilename = os.path.join(DataPath,"maps/"+"projects.dat")
    with open(projectFilename,'r') as f:
        projectLine = f.read().splitlines()
    LineNum = find('project',"projects.dat",projectID,14)
    if LineNum == "None":
        raise ValueError('ValueError')
        return ValueError
    start = LineNum
    while start < len(projectLine):
        start += 1
        if projectLine[start].split(' ')[14] != projectID:
            break
    finish = start
    start = LineNum
    array = []
    while start < finish:
        circuitName = "circuit_"+projectLine[start].split(' ')[4]+".dat"
        circuitFilename = os.path.join(DataPath, "circuits/" + circuitName)
        with open(circuitFilename, 'r') as f:
            circuitLine = f.read().splitlines()
        j = 10
        while j < len(circuitLine):
            array.append(circuitLine[j].split(" ")[2])
            j += 1
        start += 1
    if componentSymbol == "R":
        Num = findComponent('resistors', array)
    elif componentSymbol == "I":
        Num = findComponent('inductors', array)
    elif componentSymbol == "C":
        Num = findComponent('capacitors',array)
    elif componentSymbol == "T":
        Num = findComponent('transistors',array)
    return Num;

def getComponentCountByStudent(studentName, componentSymbol):
    studentsFilename = os.path.join(DataPath,"maps/"+"students.dat")
    with open(studentsFilename,'r') as f:
        studentsline = f.read().splitlines()
    #print(studentName.split(' ')[0])
    line = find('ads','students.dat',studentName.split(' ')[0],0)
    #print(studentsline[2].split(' ')[1],'\n',studentName.split(', ')[1])


    if studentsline[2].split(' ')[1].strip() != studentName.split(',')[1].strip():
        raise ValueError("ValueError")
        return ValueError
    else:
        studentsID = studentsline[line].split(' ')[32]
        #print(studentsID)
        files = glob.glob(DataPath+'/circuits'+'/*.dat')
        i = 0
        #print(files)
        FileArray =[]
        componentArray = []
        for names in files:
            FileArray.append(names)
        while i < len(FileArray):
            with open(FileArray[i]) as f:
                circuitLines = f.read().splitlines()
            j = 2
            while j < len(circuitLines):
                if circuitLines[j]== studentsID:
                    k = j
                    while k < len(circuitLines):
                        if circuitLines[k] == 'Components:':
                            z = k + 2
                            while z < len(circuitLines):
                                componentArray.append(circuitLines[z].strip())
                                z += 1
                            break
                        k += 1
                j += 1
            i += 1
        if componentSymbol == "R":
            Num = findComponent('resistors', componentArray)
        elif componentSymbol == "I":
            Num = findComponent('inductors', componentArray)
        elif componentSymbol == "C":
            Num = findComponent('capacitors',componentArray)
        elif componentSymbol == "T":
            Num = findComponent('transistors',componentArray)
        print(Num)
        return Num

def getParticipationByStudent(studentName):
    studentsFilename = os.path.join(DataPath,"maps/"+"students.dat")
    with open(studentsFilename,'r') as f:
        studentsline = f.read().splitlines()
    #print(studentName.split(' ')[0])
    line = find('ads','students.dat',studentName.split(' ')[0],0)
    #print(studentName.split(' ')[0],line)
    #print(studentsline[line].split(' ')[1].strip(),'1\n')
    #print(studentsline[line].split(' '))
    if studentsline[line].split(' ')[1].strip() != studentName.split(',')[1].strip():
        raise ValueError("ValueError")
        return ValueError
    else:
        #print(studentsline[line].split(' ')[len(studentsline[line].split(' '))-1])
        studentsID = studentsline[line].split(' ')[len(studentsline[line].split(' '))-1]
        #print(studentsID)
        files = glob.glob(DataPath+'/circuits'+'/*.dat')
        i = 0
        #print(files)
        FileArray =[]
        componentArray = []
        filesNameArray = []
        for names in files:
            FileArray.append(names)
        while i < len(FileArray):
            with open(FileArray[i]) as f:
                circuitLines = f.read().splitlines()
            j = 1
            while j < len(circuitLines):
                if circuitLines[j]== studentsID:
                    filesNameDat = FileArray[i].split('/')[len(FileArray[i].split('/'))-1]
                    filesName = filesNameDat.split('.')[0]
                    filesName = filesName.split('_')[1]
                    filesNameArray.append(filesName)
                j += 1
            i += 1
        i = 2
        #print(filesNameArray)
        projectsFilename = os.path.join(DataPath, "maps/" + "projects.dat")
        with open(projectsFilename, 'r') as f:
            projectsline = f.read().splitlines()
        j = 0
        projectsarray =[]
        while j < len(filesNameArray):
            while i < len(projectsline):
                #print(projectsline[i].split(' ')[4],filesNameArray[j],i)
                if projectsline[i].split(' ')[4] == filesNameArray[j]:
                    projectsarray.append(projectsline[i].split(' ')[14])
                i += 1
            i = 2
            j += 1
        answer = list(set(projectsarray))
        #print(answer)
        #print(len(answer))
        return  answer

def getParticipationByProject(projectID):
    projectsFilename = os.path.join(DataPath,"maps/"+"projects.dat")
    with open(projectsFilename,'r') as f:
        projectsline = f.read().splitlines()
    i= 0
    while i < len(projectsline):
        if projectsline[i].split(' ')[len(projectsline[i].split(' '))-1] == projectID:
            break
        i += 1
    if i == len(projectsline):
        raise ValueError("ValueError")
        return ValueError

    i = 0
    while i < len(projectsline):
        ID = projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]
        #print(ID)
        if ID.strip() == projectID.strip():
            start = i

            while i < len(projectsline):
                if projectsline[i].split(' ')[len(projectsline[i].split(' '))-1] != projectID:
                    #print(1234)
                    finish = i - 1
                    break
                i += 1
        i += 1
    #print(finish)
    circuitsArray =[]
    i = start
    studentID =[]
    while i < finish + 1:
        circuitsArray.append(DataPath+'/circuits'+projectsline[i].split(' ')[4]+'.dat')
        with open(DataPath+'/circuits/circuit_'+projectsline[i].split(' ')[4]+'.dat') as f:
            circuitLine = f.read().splitlines()
        j = 0
        while j < len(circuitLine):
            if circuitLine[j] == '-------------':
                j += 1
                while j < len(circuitLine) and circuitLine[j] != '-------------':
                    #print(circuitLine[j],j)
                    if circuitLine[j] not in studentID and  circuitLine[j]!='':
                        studentID.append(circuitLine[j])
                    j += 1
                break
            j += 1
        i += 1
    i = 0
    studentsFilename = os.path.join(DataPath, "maps/" + "students.dat")
    with open(studentsFilename) as f:
        studentlines = f.read().splitlines()
    j = 0
    studentName = []
    while j < len(studentlines):
        while i < len(studentID):
            if studentlines[j].split(' ')[len(studentlines[j].split(' '))-1] ==  studentID[i]:
                answer = studentlines[j].split(' ')[0] + studentlines[j].split(' ')[1]
                studentName.append(answer)
            i += 1
        i = 0
        j += 1
    print(studentName,len(studentName))
    return studentName

def getCostOfProject():
    devicePriceMap = {}
    deviceFilename = [os.path.join(DataPath, "maps/" + "capacitors.dat"),os.path.join(DataPath, "maps/" + "inductors.dat"),os.path.join(DataPath, "maps/" + "resistors.dat"),os.path.join(DataPath, "maps/" + "transistors.dat")]
    z = 0
    while z < len(deviceFilename):
        with open(deviceFilename[z]) as f:
            line = f.read().splitlines()
        k = 3
        #print(line)
        while k < len(line):
            devicePriceMap[line[k].split(' ')[0]] = line[k].split(' ')[len(line[k].split(' '))-1]
            k += 1
        z += 1
    #print(devicePriceMap)



    projectCircuitMap ={}
    k = 0
    i = 0
    numProjectMap ={}
    circuitDeviceMap ={}
    files = glob.glob(DataPath + '/circuits' + '/*.dat')
    #print(len(files))
    while i < len(files):
        with open(files[i]) as f:
            lines = f.read().splitlines()
        j = 2
        while j < len(lines):
            if lines[j] == 'Components:':
                j += 2
                while j < len(lines):
                    if files[i].split('/')[8].split('_')[1].split('.')[0] not in circuitDeviceMap:
                        #print("device: \n")
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]]= [lines[j].strip()]
                    else:
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]].append(lines[j].strip())
                    j+=1
                #print('file')
            j += 1

        i += 1

    #print(circuitDeviceMap)
    projectsFilename = os.path.join(DataPath, "maps/" + "projects.dat")
    with open(projectsFilename, 'r') as f:
        projectsline = f.read().splitlines()
    #print(devicePriceMap)
    circuitPriceMap = {}
    i =0
    while i < len(circuitDeviceMap):
        j = 0
        circuitPriceMap[list(circuitDeviceMap.keys())[i]] = 0
        #print('print',list(devicePriceMap.keys()))
        while j < len(circuitDeviceMap[list(circuitDeviceMap.keys())[i]]):
            #print(list(circuitDeviceMap.keys())[1])
            #print(i,j,'\n')

            circuitPriceMap[list(circuitDeviceMap.keys())[i]] += float(devicePriceMap[circuitDeviceMap[list(circuitDeviceMap.keys())[i]][j]].split('$')[1])
            j+=1
        i += 1
    #print(circuitPriceMap,'\n',len(circuitPriceMap))
    #print('\n',len(projectCircuitMap))
    #print(numProjectMap)
    projectPriceMap = {}

    i = 2
    while i < len(projectsline):
        j = i
        price = 0
        projectID = projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]
        while j < len(projectsline) and projectID.strip() == projectsline[j].split(' ')[len(projectsline[j].split(' '))-1].strip() :
            #print(j, len(projectsline))
            price += circuitPriceMap[projectsline[j].split(' ')[4].strip()]
            j += 1

        projectPriceMap[projectID] = round(price,2)
        i = j - 1
        i += 1
    print(projectPriceMap)
    return projectPriceMap

    #print(projectCircuitMap)
def getProjectByComponent(componentIDs):
    projectsFilename = os.path.join(DataPath, "maps/" + "projects.dat")
    with open(projectsFilename, 'r') as f:
        projectsline = f.read().splitlines()
    files = glob.glob(DataPath + '/circuits' + '/*.dat')
    i = 0
    circuitDeviceMap = {}
    while i < len(files):
        with open(files[i]) as f:
            lines = f.read().splitlines()
        j = 2
        while j < len(lines):
            if lines[j] == 'Components:':
                j += 2
                while j < len(lines):
                    if files[i].split('/')[8].split('_')[1].split('.')[0] not in circuitDeviceMap:
                        #print("device: \n")
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]]= [lines[j].strip()]
                    else:
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]].append(lines[j].strip())
                    j+=1
                #print('file')
            j += 1

        i += 1
    #print(circuitDeviceMap)
    projectDeviceMap = {}
    i = 2
    while i < len(projectsline):
        projectDeviceMap[projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]] = [ ]
        i += 1

    i = 2
    while i < len(projectsline):
        #print(projectsline[i].split(' ')[4])
        #print(circuitDeviceMap[projectsline[i].split(' ')[4]])

        projectDeviceMap[projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]].extend(circuitDeviceMap[projectsline[i].split(' ')[4]])
        #print(i)
        i += 1
    #print(projectDeviceMap)
    set = 10
    i = 0
    array = []
    while i < len(list(projectDeviceMap.keys())):
        #print(componentIDs,projectDeviceMap[list(projectDeviceMap.keys())[i]])
        j = 0
        #print(i)
        while j < len(componentIDs):
            #print(projectDeviceMap[list(projectDeviceMap.keys())[i]])
            if componentIDs[j] in projectDeviceMap[list(projectDeviceMap.keys())[i]]:
                if list(projectDeviceMap.keys())[i] not in array:
                    array.append(list(projectDeviceMap.keys())[i])
            j += 1
        i += 1
    print(array,'\n',len(array))
    return array

def getCommonByProject(projectID1,projectID2):
    projectsFilename = os.path.join(DataPath, "maps/" + "projects.dat")
    with open(projectsFilename, 'r') as f:
        projectsline = f.read().splitlines()
    z = 0
    projectName = []
    while z < len(projectsline):
        projectName.append(projectsline[z].split(' ')[len(projectsline[z].split(' '))-1])
        z += 1
    if (projectID1 not in projectName or projectID2 not in projectName):
        raise ValueError("ValueError")
        return ValueError
    files = glob.glob(DataPath + '/circuits' + '/*.dat')
    i = 0
    circuitDeviceMap = {}
    while i < len(files):
        with open(files[i]) as f:
            lines = f.read().splitlines()
        j = 2
        while j < len(lines):
            if lines[j] == 'Components:':
                j += 2
                while j < len(lines):
                    if files[i].split('/')[8].split('_')[1].split('.')[0] not in circuitDeviceMap:
                        #print("device: \n")
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]]= [lines[j].strip()]
                    else:
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]].append(lines[j].strip())
                    j+=1
                #print('file')
            j += 1

        i += 1
    #print(circuitDeviceMap)
    projectDeviceMap = {}
    i = 2
    while i < len(projectsline):
        projectDeviceMap[projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]] = [ ]
        i += 1

    i = 2
    while i < len(projectsline):
        #print(projectsline[i].split(' ')[4])
        #print(circuitDeviceMap[projectsline[i].split(' ')[4]])

        projectDeviceMap[projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]].extend(circuitDeviceMap[projectsline[i].split(' ')[4]])
        #print(i)
        i += 1

    projectID1Array = set(projectDeviceMap[projectID1])
    projectID2Array = set(projectDeviceMap[projectID2])
    answer = list(set(projectID1Array).intersection(projectID2Array))
    print(len(projectID1Array),'\n',len(projectID2Array))
    print(sorted(answer),'\n',len(answer))
    return sorted(answer)

def getComponentReport(componentID123):
    componentIDs = list(componentID123)
    projectsFilename = os.path.join(DataPath, "maps/" + "projects.dat")
    with open(projectsFilename, 'r') as f:
        projectsline = f.read().splitlines()
    files = glob.glob(DataPath + '/circuits' + '/*.dat')
    i = 0
    circuitDeviceMap = {}
    while i < len(files):
        with open(files[i]) as f:
            lines = f.read().splitlines()
        j = 2
        while j < len(lines):
            if lines[j] == 'Components:':
                j += 2
                while j < len(lines):
                    if files[i].split('/')[8].split('_')[1].split('.')[0] not in circuitDeviceMap:
                        #print("device: \n")
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]]= [lines[j].strip()]
                    else:
                        circuitDeviceMap[files[i].split('/')[8].split('_')[1].split('.')[0]].append(lines[j].strip())
                    j+=1
                #print('file')
            j += 1

        i += 1
    #print(circuitDeviceMap)
    projectDeviceMap = {}
    i = 2
    while i < len(projectsline):
        projectDeviceMap[projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]] = [ ]
        i += 1

    i = 2
    while i < len(projectsline):
        #print(projectsline[i].split(' ')[4])
        #print(circuitDeviceMap[projectsline[i].split(' ')[4]])

        projectDeviceMap[projectsline[i].split(' ')[len(projectsline[i].split(' '))-1]].extend(circuitDeviceMap[projectsline[i].split(' ')[4]])
        #print(i)
        i += 1
    #print(projectDeviceMap)
    deviceProjectMap = {}
    array = []
    i = 0
    while i < len(projectDeviceMap.keys()):
        array += projectDeviceMap[list(projectDeviceMap.keys())[i]]
        i += 1
    #deviceProjectMap = Counter(projectDeviceMap[list(projectDeviceMap.keys())[0]])
    deviceProjectMap = Counter(array)
    #print(type(array),array)
    #print(deviceProjectMap[componentIDs])
    j = 0
    map = {}
    #print(type(map))
    while j < len(componentIDs):
        map[componentIDs[j]] = deviceProjectMap[componentIDs[j]]
        j += 1
    print(map)
    return  map


def getCircuitByStudent(studentNames):
    studentsFilename = os.path.join(DataPath, "maps/" + "students.dat")
    with open(studentsFilename, 'r') as f:
        studentsline = f.read().splitlines()
    studentNamesArray = []
    i = 0

    while i < len(studentsline):
        studentNamesTemp = studentsline[3].split(' ')[0] + studentsline[3].split(' ')[1]
        j = 0
        while j < len(studentNames):
            if studentNamesTemp == studentNames[j]:
                studentNamesArray.append(studentsline[3].split(' ')[len((studentsline[3].split(' ')))])
            j += 1
        i += 1
    print(studentNamesArray)



def find(folder,filename,result,collome):
    if folder != 'circuit':
        MapeFilename = os.path.join(DataPath, "maps/" + filename)
        if filename == "students.dat" or "projects.dat":
            i = 2
        else:
            i = 3
    else:
        MapeFilename = os.path.join(DataPath, "circuits/" + filename)
        i = 2
    with open(MapeFilename,'r') as f:
        Line = f.read().splitlines()
        lineNum = 0
    while i < len(Line):
        answer = Line[i].split(" ")
        #print(answer)
        if answer[collome] == result:
            lineNum = i
            break
        i += 1
    return lineNum
def findComponent(component,array):
    if len(array) == 0:
        return 0
    MapeFilename = os.path.join(DataPath, "maps/" + component + ".dat")
    with open(MapeFilename,'r') as f:
        Line = f.read().splitlines()
    num = 0
    i = 0
    while i < len(array):
        j = 3
        while j < len(Line):
            if Line[j].split(" ")[0] == array[i]:
                num += 1
            j += 1
        i += 1
    return num





if __name__  == "__main__":
    #print(getComponentCountByStudent('082D6241-40EE-432E-A635-65EA8AA374B6', "C"))
    #getComponentCountByStudent('Adams,asdfasd Keith', 'I')
    #getParticipationByStudent('Bryant, 123Evelyn')
    #findDate('AAPL.dat','2018/12/14')
    #getParticipationByProject('082D6241-40EE-432E-A635-65EA8AA374B6')
    #getCostOfProject()
    #getProjectByComponent(['TAZ-349'])
    #getCommonByProject('082D6241-40EE-432E-A635-65EA8AA374B6', '08EDAB1A-743D-4B62-9446-2F1C5824A756')
    #getComponentReport(['HOR-267'])
    getCircuitByStudent('studentNames')
    #print(getVolumeSum('MSFT', '2014/01/17', '2018/01/08'))
    #22110230
    #30476834813
    # Write  anything  here to test  your  cd