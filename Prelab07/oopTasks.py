#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/19/2019 >
#######################################################
import re
import os

from enum import Enum

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

#from enum import Enum


class Level(Enum):


# self.name = ['Freshman','Sophomore','Junior','Senior']
    Freshman = 'Freshman'
    Sophomore = 'Sophomore'
    Junior = 'Junior'
    Senior = 'Senior'
class ComponentType(Enum):
    Inductor = 0
    Resistor = 1
    Capacitor = 2
    Transistor = 3

class Student():
    def __init__(self,ID,firstName,lastName,level):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.studentLevel = level
        if level not in Level.__members__:
            raise TypeError("The argument must be an instance of the 'Level' Enum.")

    def __str__(self):
        return (f"{self.ID}, {self.firstName} {self.lastName}, {self.studentLevel}")


class Component():
    def __init__(self,ID,ctype,price):
        #print(ctype)
        self.ID = ID
        self.ctype = ctype
        self.price = round(float(price),2)
        #print(self.ctype.name)
        if not isinstance(ctype,ComponentType):
            raise TypeError("The argument must be an instance of the 'ComponentType' Enum.")
    def __str__(self):
        return (f"{self.ID}, {self.ctype}, ${self.price}")
    def __hash__(self):
        return hash(self.ID)


class Circuit():
    def __init__(self,ID,components,cost):
        self.ID = ID
        self.components = components
        self.cost = 0
        for element in components:
            #print(456,element.ctype)
            if not isinstance(element,Component):
                raise TypeError("The argument must be an instance of the 'Level' Enum.")
        for element in self.components:
                self.cost += element.price

    def __str__(self):
        c = 0
        i = 0
        t = 0
        r = 0
        price = 0


        #print(ComponentType.Transistor)
        for element in self.components:
            #print(element,element.ctype)
            if element.ctype == ComponentType.Capacitor:
                c += 1
            elif element.ctype == ComponentType.Inductor:
                i += 1
            elif element.ctype == ComponentType.Transistor:
                t += 1
            else:
                r += 1
        #print(self.components[1])
        return (f"{self.ID}: (R = {r}, C = {c}, I = {i}, T = {t}), Cost = ${self.cost}")

    def getByType(self,Components):
        answer = set()
        if Components not in ComponentType._member_names_:
            raise ValueError("The argument must be an instance of the 'Level' Enum.")
        i = 0
        while i < len(self.components):
            if self.components[i].ctype == Components.ctype:
                answer.add(self.components)
            i += 1
        return  answer

    def __sub__(self, other):
        if not isinstance(other,Component):
            raise TypeError("The argument must be an instance of the 'Component' class.")
        else:
            if other not in self.components:
                return self
            else:
                self.cost -= float(other.price)
                self.components.remove(other)
                return self
    def __add__(self, other):
        if not isinstance(other,Component):
            raise TypeError("The argument must be an instance of the 'Component' class.")
        else:
            if other not in self.components:
                return self
            else:
                self.cost += float(other.price)
                self.components.append(other)
                return self
    def __contains__(self, item):
        i = 0
        while i < len(self.components):
            if item.ID == self.components[i].ID and item.ctype == self.components[i].ctype and item.price == self.components[i].price:
                return True
            i += 1
        return False

    def __eq__(self, other):
        if not isinstance(other,Circuit):
            raise TypeError("Circuit2 must be an instance of the 'Component' class.")
        if self.cost == other.cost:
            return True
        else:
            return False


class Project():
    def __init__(self,ID,participants,circuits,cost):
        self.ID = ID
        self.participants = participants
        self.circuits = circuits
        self.cost = 0
        for elements in participants:
            if not isinstance(elements,Student):
                raise TypeError("Studnets must be an instance of the 'Student' class.")
        for elements in circuits:
            if not isinstance(elements,Circuit):
                raise TypeError("Circuit must be an instance of the 'Circuit' class.")
    def __str__(self):
        for elements in self.circuits:
            #print('loop',elements,elements.cost)
            self.cost += elements.cost
        return f"{self.ID}: ({len(self.circuits)} Circuits, {len(self.participants)} Participants), Cost = ${self.cost}"
    def __contains__(self, item):
        if not isinstance(item,Student)and not isinstance(item,Circuit) and not isinstance(item,Component):
            raise TypeError("This input must be an instance of the 'Student, Circuit or Component' class.")
        if isinstance(item,Circuit):
            i = 0
            while i < len(self.circuits):
                if item.ID == self.circuits[i].ID and item.components == self.circuits[i].components and item.cost == self.circuits[i].cost:
                    return True
                i += 1
        if isinstance(item,Component):
            i = 0
            while i < len(self.circuits):
                j = 0
                while j < len(self.circuits[i].components):
                    if item.ID == self.circuits[i].components[j].ID and item.ctype == self.circuits[i].components[j].ctype and item.price == self.circuits[i].components[j].price:
                        return True
                    j += 1
                i += 1
        if isinstance(item,Student):
            i = 0
            while i < len(self.participants):
                if item.ID == self.participants[i].ID and item.firstName == self.participants[i].firstName and item.lastName == self.participants[i].lastName and item.level == self.participants[i].level:
                    return True
                i += 1
        return False

    def __sub__(self, other):
        if not isinstance(other,Circuit):
            raise TypeError("The circuitd must be an instance of the 'Circuit' class.")
        else:
            if other not in self.circuits:
                return self
            else:
                self.cost -= float(other.cost)
                self.circuits.remove(other)
                return self
    def __add__(self, other):
        if not isinstance(other,Circuit):
            raise TypeError("The circuitd must be an instance of the 'Circuit' class.")
        else:
            if other not in self.circuits:
                return self
            else:
                self.cost += float(other.cost)
                self.circuits.append(other)
                return self
    def __getitem__(self, item):
        answer = []
        for elements in self.circuits:
            if item == elements.ID:
                return elements
            else:
                answer.append(elements.ID)
        if item not in answer:
            raise KeyError("the circuit does not exist")

#print(Student(123123,"asfd",'asdf','Freshman'))
a = Component(123123,ComponentType.Resistor,'1')
#print(a)
b = Component(123,ComponentType.Inductor,'1')
c = Circuit(123123,[a,b],'1.21233')
d = Circuit(123123,[a,a],'1.21233')
print(d)
stu1 = Student(123,'Linfeng','Zhang','Junior')
stu2 = Student(123,'Songlin','Chen','Junior')
e = Project(123123,[stu1,stu2],[c,d],'1.21233')
print(e)

