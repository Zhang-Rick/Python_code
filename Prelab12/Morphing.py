import re
import os
import copy
import collections
import enum
from enum import Enum
import numpy as np
import unittest
import os
from uuid import uuid4
from time import perf_counter
from imageio import imread as libread
from scipy.spatial import Delaunay
from scipy import ndimage

def loadTriangles(leftPointFilePath, rightPointFilePath):
    with open(leftPointFilePath) as fLeft:
        LeftCordinates = fLeft.readlines()
    #print(LeftCordinates[2].split())
    with open(rightPointFilePath) as fRight:
        RightCordinates = fRight.readlines()
    pointSetLeft =[]
    pointSetRight =[]

    i = 0
    list = []
    pattern =r"(?P<LeftCoordinate>[0-9]+[.][0-9])[ \t]+(?P<rightCoordinate>[0-9]+[.][0-9])"
    while i < len(LeftCordinates):
        match = re.search(pattern,LeftCordinates[i])
        match1 = re.search(pattern,RightCordinates[i])
        #print(match['LeftCoordinate'],match['rightCoordinate'])

        pointSetLeft.append(np.float64(match['LeftCoordinate']))
        pointSetLeft.append(np.float64(match['rightCoordinate']))

        pointSetRight.append(np.float64(match1['LeftCoordinate']))
        pointSetRight.append(np.float64(match1['rightCoordinate']))


        i += 1
        #print([elements for elements in pointSetLeft])
    #triangle = np.array([elements for elements in pointSetLeft])
    #print(triangle)

    #print(pointSetLeft)
    #print(pointSetRight)
    i = 0
    list = []
    list2 = []
    pointleft = np.reshape(pointSetLeft,(int(len(pointSetLeft)/2),2))
    pointright = np.reshape(pointSetRight,(int(len(pointSetRight)/2),2))
    #print(pointleft)
    #print(pointright)
    leftTriangle = Delaunay(pointleft)
    triangleListLeft = pointleft[leftTriangle.simplices]
    triangleListRight = pointright[leftTriangle.simplices]
    i = 0
    #print(triangleListLeft)
    #print(tuple(triangleListLeft[1]))
    listLeft = []
    listRight = []
    while i < len(triangleListLeft):
        listLeft.append(Triangle(triangleListLeft[i]))
        listRight.append(Triangle(triangleListRight[i]))
        i += 1
    return tuple([listLeft,listRight])
class Triangle():
    def __init__(self,triangles):
        a = []
        # print(triangles.shape,triangles.shape == (3,2))
        if type(triangles) != type(a) and triangles.shape != (3, 2):
            raise ValueError("input is invalid!")
        else:
            for elememnts in triangles:
                # print(elememnts,elememnts.shape == (2,3))
                if type(elememnts[0]) != type(np.float64(1)) and type(elememnts[1]) != type(np.float64(1)):
                    raise ValueError("123")
        self.vertices = np.array(triangles)

    def getPoints(self):

        x1 = self.vertices[0][0]
        x2 = self.vertices[1][0]
        x3 = self.vertices[2][0]
        #print(x1)
        y1 = self.vertices[0][1]
        y2 = self.vertices[1][1]
        y3 = self.vertices[2][1]
        #print(self.vertices[0],x1,y1)
        i = 0
        minx = int((min([x1,x2,x3])))
        maxx = int((max([x1,x2,x3])))

        miny = int((min([y1,y2,y3])))
        maxy = int((max([y1,y2,y3])))
        x = (minx)
        y = (miny)
        #print(x1,x2,x3,maxx,minx)
        list =[]
        area = abs(x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2))/2
        while x < maxx:
            y= miny
            while y < maxy:
                area1 = abs(x * (y2-y3) + x2 * (y3-y) + x3 * (y-y2))/2 + abs(x1 * (y-y3) + x * (y3-y1) + x3 * (y1-y))/2 + abs(x1 * (y2-y) + x2 * (y-y1) + x * (y1-y2))/2
                #print('x:',x,'y',y)
                if area1 <= area:
                    #print('x','y')
                    list.append([x,y])
                y+=1
            x+=1

        return np.array(list,dtype=np.float64)


class Morpher():
    def __init__(self,leftImage,leftTriangles,rightImage,rightTriangles):
        for x in leftImage:
            for y in x:
                if not isinstance(y,np.uint8):
                    raise TypeError("123")

        for x in rightImage:
            for y in x:
                if not isinstance(y,np.uint8):
                    raise TypeError("123")
        for x in rightTriangles:
            if not isinstance(x, Triangle):
                raise TypeError("123")

        for x in leftTriangles:
            if not isinstance(x, Triangle):
                raise TypeError("12343")
        self.leftImage = leftImage
        self.leftTriangles = leftTriangles
        self.rightImage = rightImage
        self.rightTriangles = rightTriangles

    def getImageAtAlpha(self,alpha):
        points = self.rightTriangles[0].getPoints().tolist()
        points1 = self.leftTriangles[1].getPoints().tolist()

        leftImgTrans = self.leftImage
        print(points)
        image = self.leftImage
        print(1)
        #print(self.leftImage)
        print(2)
        #print(self.rightImage)
        i = 0

        while i < len(points):
            image[int(points[i][1])][int(points[i][0])] = self.leftImage[int(points[i][1])][int(points[i][0])] * (1-alpha) + self.rightImage[int(points[i][1])][int(points[i][0])] * (alpha)
            i += 1
        return image


