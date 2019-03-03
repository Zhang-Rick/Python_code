#######################################################
#    Author:      <Linfeng Zhang >
#    email:       <zhan2642@purdue.edu >
#    ID:           <ee364b21 , e.g. ee364j20 >
#    Date:         <01/19/2019 >
#######################################################
import re
import os
import copy
import collections
import enum
from enum import Enum

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

#from enum import Enum

class Datum():
    def __init__(self,*args):
        self._storage_ = args
        for elements in args:
            print(args,'\n',elements,type(elements),type(0.0))
            if type(elements) !=type(0.0):
                raise TypeError("the value entered must be a float type!")
    def __str__(self):
        answer = '('
        i = 0
        for elements in self._storage_:
            #print(elements)
            i += 1
            if i == len(self._storage_):
                answer += str(round(elements,2))
            else:
                answer += str(round(elements, 2)) + ','+' '
        answer += ')'
        #print(answer)
        return (f"{answer}")
    def __hash__(self):
        return hash(self._storage_)

    def distanceFrom(self,datum):
        a =  len(self._storage_)
        a1 = list(self._storage_)
        b =  len(datum._storage_)
        b1 = list(datum._storage_)
        i = 0
        while i < abs(a-b):
            if a - b > 0:
                b1.append(0.0)
            if a - b < 0:
                a1.append(0.0)
            i += 1
        #print(b1)
        #print(a1)
        i = 0
        sum = 0
        while i < len(a1):
            sum += (b1[i]-a1[i])**2
            i += 1
        sum = sum **(1/2.0)
        return sum

    def clone(self):
        instance = copy.deepcopy(self)
        return instance

    def __contains__(self, other):
        if type(other) != type(0.0):
            raise TypeError("The input is not a float!")
        if other in self._storage_:
            return True
        else:
            return False
    def __len__(self):
        return len(self._storage_)
    def __iter__(self):
        return iter(self._storage_)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    def __getitem__(self, item):
        return self._storage_[item]
    def __sub__(self,other):
        if isinstance(other,Datum):
            a = len(self._storage_)
            a1 = list(self._storage_)
            b = len(other._storage_)
            b1 = list(other._storage_)
            i = 0
            while i < abs(a - b):
                if a - b > 0:
                    b1.append(0.0)
                if a - b < 0:
                    a1.append(0.0)
                i += 1
            # print(b1)
            # print(a1)
            i = 0
            sum = []
            while i < len(a1):
                sum.append(a1[i] - b1[i])
                i += 1
            a=tuple(sum)
            b = Datum(*a)
            return b
        if type(other) == type(0.0):
            a=[]
            for elements in self._storage_:
                a.append(elements-other)
            a= tuple(a)
            b= Datum(*a)
            return b
        raise TypeError("Input is neither float or Datum type!")

    def __add__(self, other):
        if isinstance(other, Datum):
            a = len(self._storage_)
            a1 = list(self._storage_)
            b = len(other._storage_)
            b1 = list(other._storage_)
            i = 0
            while i < abs(a - b):
                if a - b > 0:
                    b1.append(0.0)
                if a - b < 0:
                    a1.append(0.0)
                i += 1
            # print(b1)
            # print(a1)
            i = 0
            sum = []
            while i < len(a1):
                sum.append(a1[i] + b1[i])
                i += 1
            a = tuple(sum)
            b = Datum(*a)
            return b
        if type(other) == type(0.0):
            a = []
            for elements in self._storage_:
                a.append(elements + other)
            a = tuple(a)
            b = Datum(*a)
            return b
        raise TypeError("Input is neither float or Datum type!")
    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other ):
        if type(other) != type(0.0)or type(other) == type(self):
            raise TypeError("Input is not float!")
        a = []
        for elements in self._storage_:
            a.append(elements * other)
        a = tuple(a)
        b = Datum(*a)
        return b

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) != type(0.0) or type(other) == type(self):
            raise TypeError("Input is not float!")
        a = []
        for elements in self._storage_:
            a.append(elements/other)
        a = tuple(a)
        b = Datum(*a)
        return b
    def __neg__(self):
        a=[]
        for elements in self._storage_:
            a.append((-1)*elements)
        a=tuple(a)
        b = Datum(*a)
        return b
    def __lt__(self, other):
        if isinstance(other,Datum):
            raise TypeError("Input is Datum type!")
        a = (0.0)
        b = Datum(*a)
        selfdistance = self.distanceFrom(b)
        otherdistance = other.distanceFrom(b)
        if selfdistance < otherdistance:
            return True
        return False

    def __le__(self, other):
        if isinstance(other,Datum):
            raise TypeError("Input is Datum type!")
        a = (0.0)
        b = Datum(*a)
        selfdistance = self.distanceFrom(b)
        otherdistance = other.distanceFrom(b)
        if selfdistance <= otherdistance:
            return True
        return False

    def __eq__(self, other):
        if isinstance(other,Datum):
            raise TypeError("Input is Datum type!")
        a = (0.0)
        b = Datum(*a)
        selfdistance = self.distanceFrom(b)
        otherdistance = other.distanceFrom(b)
        if selfdistance == otherdistance:
            return True
        return False

    def __ne__(self, other):
        if isinstance(other,Datum):
            raise TypeError("Input is Datum type!")
        a = (0.0)
        b = Datum(*a)
        selfdistance = self.distanceFrom(b)
        otherdistance = other.distanceFrom(b)
        if selfdistance != otherdistance:
            return True
        return False

    def __gt__(self, other):
        if isinstance(other,Datum):
            raise TypeError("Input is Datum type!")
        a = (0.0)
        b = Datum(*a)
        selfdistance = self.distanceFrom(b)
        otherdistance = other.distanceFrom(b)
        if selfdistance > otherdistance:
            return True
        return False

    def __ge__(self, other):
        if isinstance(other,Datum):
            raise TypeError("Input is Datum type!")
        a = (0.0)
        b = Datum(*a)
        selfdistance = self.distanceFrom(b)
        otherdistance = other.distanceFrom(b)
        if selfdistance >= otherdistance:
            return True
        return False

class Data(collections.UserList):
    def __init__(self,list=None):
        if list == None:
            super().__init__([])
        else:
            for elements in list:
                if not isinstance(elements,Datum):
                    raise TypeError("Input is not a Datum type")
            super(Data, self).__init__(list)

    def computeBounds(self):
        temp = self
        max = 0
        list1 = tuple([])
        max1 = []
        min1 = []
        index = 0
        i = 0
        while i < len(temp):
            if len(temp[i]) > max:
                max = len(temp[i])
                max_index = i
            i += 1
        for element in temp:
            if len(element) > max:
                max = len(element)
        i = 0
        while i < len(temp):
            j = 0
            while j < max:
                if len(max1) <= max - 1:
                    max1.append(temp[index][j])
                    min1.append(temp[index][j])
                j += 1
            i += 1
        i = 0
        while i < len(temp):
            j = 0
            while j < len(temp[i]):
                if temp[i][j] > max1[j]:
                    max1[j] = temp[i][j]
                if temp[i][j] < min1[j]:
                    min1[j] = temp[i][j]
                j += 1
            i += 1
        max1 = tuple(max1)
        min1 = tuple(min1)
        return (Datum(*min1), Datum(*max1))

    def computeMean(self):
        j = 0
        length = 0
        for element in self:
            if len(element) > max:
                length = len(element)
        average = []
        sum = []
        num = []
        i = 0
        while i < length:
            sum.append(0.0)
            num.append(0.0)
            average.append(0.0)
            i += 1
        i = 0
        while i < len(self):
            j = 0
            while j < len(self[i]):
                sum[j] += self[i][j]
                num[j] += 1
                j += 1
            i += 1
        while i < len(sum):
            average[i] = sum[i] / num[i]
            i += 1
        answer = tuple(average)
        answer = Datum(*answer)
        return answer

    def append(self, item):
        if not isinstance(item, Datum):
            raise TypeError("The item is not of a Datum instance")
        super().append(item)

    def count(self, item):
        if not isinstance(item, Datum):
            raise TypeError("The item is not of a Datum instance")
        super().count(item)

    def index(self):
        pass

    def insert(self, index, item):
        if not isinstance(item, Datum):
            raise TypeError("The item is not of a Datum instance")
        super().insert(index, item)

    def remove(self, item):
        if not isinstance(item, Datum):
            raise TypeError("The item is not of a Datum instance")
        super().remove(item)

    def __setitem__(self, k, v):
        if not isinstance(v, Datum):
            raise TypeError("The item is not of a Datum instance")
        super().__setitem__(k, v)

    def extend(self, item):
        if not isinstance(item, Datum):
            raise TypeError("The item is not of a Datum instance")
        super().extend(item)


class DataClass(Enum):
    Class2 = 0
    Class1 = 1

class DataClassifier():
    def __init__(self,group1,group2):
        if not isinstance(group1,Data):
            raise TypeError("Group1 is not Data class!")
        if not isinstance(group2,Data):
            raise TypeError("Group2 is not Data class!")
        if group1 == []:
            raise ValueError("Group1 is empty!")
        if group2 == []:
            raise ValueError("Group2 is empty!")
        self.group1 = group1
        self.group2 = group2










a = (1.2,-2.3)
k = (3.4,5.4,3.4)
b=Datum(*a)
c = Datum(*k)
print(123,b.distanceFrom(c))
print(123456,c)
c = Data([c,b]).computeBounds()
