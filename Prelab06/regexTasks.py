#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/19/2019 >
#######################################################
import re
import os
from pprint import pprint as pp
from uuid import UUID
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('~ee364/DataFolder/Prelab06')

def getUrlParts(url):
    #print(url)
    pattern =  "/[0-9a-zA-Z._-]+"
    #print(base)
    multiple = re.findall(pattern, url)
    #pp(multiple)
    i = 0
    pattern = "[0-9a-zA-Z._-]+"
    multiple1 = []
    while i < len(multiple):
        multiple1.append(str(re.search(pattern,multiple[i])[0]))
        i += 1
    #pp(tuple(multiple1))
    return tuple(multiple1)


def getQueryParameters(url):
    pattern = "([0-9a-zA-Z._-]+[=][0-9a-zA-Z._-]+)"
    multiple = re.findall(pattern, url)
    #pp(multiple)
    i = 0
    answer = []
    while i < len(multiple):
        match = re.search('(?P<user>[\w.-]+)[=](?P<domain>[\w.-]+)', multiple[i])
        answer.append(tuple([match[1],match[2]]))
        i += 1
    #pp(answer)
    return answer

def getSpecial(sentence, letter):
    pattern = r"([a-zA-Z]*%s[a-zA-Z]*)"
    multiple1 = re.findall(pattern%letter,sentence,re.IGNORECASE)
    pattern1 = r"([^\S]%s[a-zA-Z]*%s+)"
    multiple2 =re.findall(pattern1%(letter,letter),sentence,re.IGNORECASE)
    #l = set(multiple1) -set(multiple2)
    pattern = "[0-9a-zA-Z._-]+"
    multiple = []
    i = 0
    while i < len(multiple2):
        multiple1.remove(str(re.search(pattern, multiple2[i])[0]))
        i += 1
    #print(multiple1)
   # print(multiple)
    #multiple1.remove(str(multiple))
   # print(multiple1)
    return multiple1

def getRealMAC(sentence):
    pattern = "[a-fA-F0-9]{2}[:-][a-fA-F0-9]{2}[:-][a-fA-F0-9]{2}[:-][a-fA-F0-9]{2}[:-][a-fA-F0-9]{2}[:-][a-fA-F0-9]{2}"
    multiple1 = re.findall(pattern, sentence, re.IGNORECASE)
    #pp(multiple1)
    return multiple1

def getName():
    Filename = DataPath + '/Employees.txt'
    with open(Filename)as f:
        lines = f.read()
    # print(lines)
    pattern = "[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+[,]{2}"
    multiple = re.findall(pattern, lines)
    # print(multiple)
    i = 0
    while i < len(multiple):
        answer = re.findall(',', multiple[i])
        # print(answer)
        if str(answer) != None:
            name = re.findall('\w+', multiple[i])
            first = name[1]
            last = name[0]
            # print(first)
            multiple[i] = first + ' ' + last
            # print(multiple[i])
        i += 1
    #print(multiple)
    return multiple

def getRejectedEntries():
    Filename = DataPath + '/Employees.txt'
    with open(Filename)as f:
        lines = f.read()
    # print(lines)
    pattern = "[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+[,][,][ \t][,][ \t][;][,][;][ \t][;][,][;][ \t][;][,][;][,][ \t][;][,][;][ \t][,][,][\s]"
    multiple = re.findall(pattern, lines)
    #print(len(multiple),multiple)
    i = 0
    while i < len(multiple):

        match = re.search('(?P<last>[\w]+)[,][ \t](?P<first>[\w]+)', multiple[i])
        #print(match)
        if match != None:
            multiple[i] = match["first"] + ' ' + match["last"]
        else:
            match = re.search('(?P<last>[\w]+)[ \t](?P<first>[\w]+)', multiple[i])
            multiple[i] = match["last"] + ' ' + match["first"]
        i += 1
    #print(len(multiple),multiple)
    return  sorted(multiple)
def getEmployeesWithIDs():
    #Employees = getName()
    Filename = DataPath + '/Employees.txt'
    with open(Filename)as f:
        lines = f.read()
    pattern = "[0-9A-Fa-f]{8}[-]?[0-9A-Fa-f]{4}[-]?[0-9A-Fa-f]{4}[-]?[0-9A-Fa-f]{4}[-]?[0-9A-Fa-f]{12}"
    IDs = re.findall(pattern,lines)
    pattern1 = "[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+[,]{2}[ \t][,][ \t][,]{2}"
    names = re.findall(pattern1,lines)
    #print()
    #print(len(IDs),len(names))
    i = 0
    while i < len(names):
        answer = re.findall(',', names[i])
        # print(answer)
        if str(answer) != None:
            name = re.findall('\w+', names[i])
            first = name[1]
            last = name[0]
            # print(first)
            names[i] = first + ' ' + last
            # print(multiple[i])
        i += 1
    i= 0
    while i < len(IDs):
        IDs[i] = str(UUID(IDs[i]))
        i += 1
    #print(len(IDs),IDs)
    #print(len(names),names)
    Map = {}
    i = 0
    while i < len(IDs):
        Map[names[i]]=IDs[i]
        i += 1
    #print(Map)
    return  Map
def getEmployeesWithPhones():
    Filename = DataPath + '/Employees.txt'
    with open(Filename) as f:
        lines = f.read()
    i = 0
    pattern = "[a-zA-Z]+[,]?[ \t][a-zA-Z]+.+[\(]?[0-9]{3}[\)]?[ \t]?[-]?[0-9]{3}[-]?[0-9]{4}"
    answer= (re.findall(pattern,lines))
    #print(answer)
    answer1 = []
    Map = {}
    pattern = "[\w]+[,][ \t][\w]+.+"
    while i < len(answer):
        check = re.findall(pattern, answer[i])
        #print(check)
        if check != []:
            #print(answer)
            match = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+', answer[i])
            match2 = re.search('[\(]?(?P<phone1>[\d]{3})[\)]?[ \t]?[-]?(?P<phone2>[\d]{3})[-]?(?P<phone3>[\d]{4})',answer[i])
            #print(match["first"],match["last"])
            #print(match2["phone1"],match2["phone2"],match2["phone3"])
            name = match["last"] + ' ' + match["first"]
            Phone = match2["phone1"] +'-'+match2["phone2"]+'-'+match2["phone3"]
        else:
            match = re.search('(?P<first>[\w]+)[ \t](?P<last>[\w]+).+', answer[i])
            match2 = re.search('[\(]?(?P<phone1>[\d]{3})[\)]?[ \t]?[-]?(?P<phone2>[\d]{3})[-]?(?P<phone3>[\d]{4})',answer[i])
            #print(match["first"], match["last"])
            #print(match2["phone1"], match2["phone2"], match2["phone3"])
            name = match["last"] + ' ' + match["first"]
            Phone = match2["phone1"] + '-' + match2["phone2"] + '-' + match2["phone3"]
        Map[name] =Phone
        i+=1
    #print(Map)
    return Map

def getEmployeesWithoutIDs():
    Filename = DataPath + '/Employees.txt'
    with open(Filename)as f:
        lines = f.read()
    pattern1 = "[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+[,; \t]+[\(]?[0-9]{3}[\)]?[ \t]?[-]?[0-9]{3}[-]?[0-9]{4}"
    pattern2 = "[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+[,; \t]+[a-zA-Z]+[\n]"
    names1 = re.findall(pattern1, lines)
    i = 0
    answer = []
    while i < len(names1):
        match0 = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+', names1[i])
        #print(match0)
        if match0 == None:
            match1 = re.search('(?P<first>[\w]+)[ \t](?P<last>[\w]+).+', names1[i])
            Name = match1["first"] + ' ' + match1["last"]
        else:
            match0 = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+', names1[i])
            Name = match0["last"] + ' ' + match0["first"]
        answer.append(Name)
        i += 1
    names2 = re.findall(pattern2, lines)
    i = 0
    while i < len(names2):
        match0 = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+', names2[i])
        #print(match0)
        if match0 == None:
            match1 = re.search('(?P<first>[\w]+)[ \t](?P<last>[\w]+).+', names2[i])
            Name = match1["first"] + ' ' + match1["last"]
        else:
            match0 = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+', names2[i])
            Name = match0["last"] + ' ' + match0["first"]
        if Name not in answer:
            answer.append(Name)
        i += 1
    #print(len(answer),answer)
    return sorted(answer)
    #print(names2)
def getEmployeesWithStates():
    Filename = DataPath + '/Employees.txt'
    with open(Filename)as f:
        lines = f.read()
    pattern2 = "[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+.+[a-zA-Z]+[ \t]?[a-zA-Z]*[\n]"
    names2 = re.findall(pattern2,lines)
    i = 0
    map ={}
    while i < len(names2):
        match0 = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+,(?P<city>[\w]+[ \t]?[\w]*)[\n]', names2[i])
        #print(match0)
        if match0 == None:
            match1 = re.search('(?P<first>[\w]+)[ \t](?P<last>[\w]+).+,(?P<city>[\w]+[ \t]?[\w]*)[\n]', names2[i])
            Name = match1["first"] + ' ' + match1["last"]
            city =match1["city"]
        else:
            match0 = re.search('(?P<first>[\w]+)[,][ \t](?P<last>[\w]+).+,(?P<city>[\w]+[ \t]?[\w]*)[\n]', names2[i])
            Name = match0["last"] + ' ' + match0["first"]
            city = match0["city"]
        i += 1
        map[Name] = city
    #print(len(map),map)
    return map
def getCompleteEntries():
    Filename = DataPath + '/Employees.txt'
    with open(Filename)as f:
        lines = f.read()
    pattern2 = '[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+[,; \t]+[0-9A-Fa-f\{\}-]{32,38}[,; \t]+[ \t],[\(-\)0-9- \t]+[,; \t]+[a-zA-Z]+[ \t]?[a-zA-Z]+'
    match = re.findall(pattern2,lines)
    i = 0
    map = {}
    while i < len(match):
        answer = re.search('(?P<Name>[A-Z][a-z]+[,]?[ \t][A-Z][a-z]+)[,; \t\{]+(?P<ID>[0-9A-Fa-f-]+)[\},; \t]+(?P<Phone>[\(-\)0-9- \t]+)[,; \t]+(?P<State>[a-zA-Z]+[ \t]?[a-zA-Z]+)',match[i])
        name1 = answer["Name"]
        patternName = ','
        matchName = re.search(patternName,name1)
        if matchName == None:
            name = name1
        else:
            patternName ='(?P<Last>[a-zA-Z]+)[,][ \t](?P<First>[a-zA-Z]+)'
            match1 = re.search(patternName,name1)
            name = match1["First"] + ' ' + match1["Last"]
        ID1 = answer["ID"]
        ID = str(UUID(ID1))
        Phone1 = answer["Phone"]
        patternPhone1 = "-[0-9]{3}-"
        patternPhone2 = "\([0-9]{3}\)"
        matchName1 = re.search(patternPhone1,Phone1)
        matchName2 = re.search(patternPhone2,Phone1)
        #print(Phone1)
        if matchName2 == None and matchName1 == None:
            patternPhone = '(?P<phone1>[0-9]{3})(?P<phone2>[0-9]{3})(?P<phone3>[0-9]{4})'
            match1 = re.search(patternPhone,Phone1)
            Phone123 = match1["phone1"]+'-'+match1["phone2"]+'-'+match1["phone3"]
        elif matchName2 != None and matchName1 == None:
            patternPhone = '[\(](?P<phone1>[0-9]{3})[\)][ \t](?P<phone2>[0-9]{3})[-](?P<phone3>[0-9]{4})'
            match1 = re.search(patternPhone,Phone1)
            Phone123 = match1["phone1"]+'-'+match1["phone2"]+'-'+match1["phone3"]
        else:
            Phone123 = Phone1
        State1 = answer["State"]
        map[name]=tuple([ID,Phone123,State1])
        #print(name,ID,Phone123,State1)
        i += 1
    #print(map)
    #    #print(match[i])
    #    i  += 1
    #print(len(match))
    return map
if __name__  == "__main__":
    url = "http://www.purdue.edu/Home/asdfasd/Calendar?Year=2016&Month=September&Semester=Fall"
    getUrlParts(url)
    url = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    getQueryParameters(url)
    getEmployeesWithoutIDs()
    text = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    getSpecial(text, 't')
    sentence =  '58-1C-0A-6E-39-4D'
    getRealMAC(sentence)
    a=getRejectedEntries()
    #print(len(a),a)
    b = getEmployeesWithIDs()
    #print(len(b),b)
    getEmployeesWithPhones()
    c=getEmployeesWithStates()
    getCompleteEntries()