import json
import random
from random import randint
import math
import sys
import PIL
sys.setrecursionlimit(10000)
from colorsys import hsv_to_rgb
from PIL import Image
import numpy as np


#read file and parse Library
myLibrary = open('tiffdatawl.json','r')
myData = myLibrary.read()
myLibrary.close()
obj = json.loads(myData)



class MDCreator:

    def setAllData(self):
        count=0
        for _ in obj:
            obj[count]['NAME'] = "POINT"+ str(count)
            count+=1
        count=0
        for _ in obj:
            obj[count]['Z'] = random.uniform(0, 10)
            count+=1

        counter=0
        all=0
        #MUST HAVE DICTIONARY OF 10000 different dictionary objects :)
        for _ in range(500):
            counter+=1
            counter2=1
            for _ in range(500):
                obj[all]["Y"]=counter
                obj[all]["X"]=counter2
                counter2+=1
                all+=1

                
        with open('tiffdatawl.json', 'w') as f:
            json.dump(obj,f,indent=len(obj[0]))
            f.close()


class MAlgorithm:
    
    def checknode(self, snode,nap):
        if obj[snode]['Z']<=nap:
            global checky #Kanstraksweg
            checky=0 #Kanstraksweg
            counts=0
            return(self.pathFinder(snode,nap,counts))
        else: 
            print("Path is above NAP, therefore safe")

 
    def pathFinder(self, snode,nap,counts):
        global checky
        obj[snode]['RGB']="#0000FF"
        counts+=1
        checky+=1 #Kanstraksweg
        print(obj[snode]['NAME'])
        if counts > 10000:
            print("WARNING!!! THIS AREA WILL BE FLOODED!")
            print(checky) #Kanstraksweg
            sys.exit()
        if obj[snode]['X']>1:
            if obj[snode-1]['Z'] <= nap and obj[snode-1]['RGB']!="#0000FF":
                self.pathFinder(snode-1,nap,counts)
            if obj[snode]['Y']<int(math.sqrt(len(obj))):
                if obj[snode+int(math.sqrt(len(obj)))-1]['Z'] <= nap and obj[snode+int(math.sqrt(len(obj)))-1]['RGB']!="#0000FF":
                    self.pathFinder(snode+int(math.sqrt(len(obj)))-1,nap,counts)
            if obj[snode]['Y']>1:
                if obj[snode-int(math.sqrt(len(obj)))-1]['Z'] <= nap and obj[snode-int(math.sqrt(len(obj)))-1]['RGB']!="#0000FF":
                    self.pathFinder(snode-int(math.sqrt(len(obj)))-1,nap,counts)
                

        if obj[snode]['X']<int(math.sqrt(len(obj))):
            if obj[snode+1]['Z'] <= nap and obj[snode+1]['RGB']!="#0000FF":
                self.pathFinder(snode+1,nap,counts)
            if obj[snode]['Y']<int(math.sqrt(len(obj))):   
                if obj[snode+int(math.sqrt(len(obj)))+1]['Z'] <= nap and obj[snode+int(math.sqrt(len(obj)))+1]['RGB']!="#0000FF":
                    self.pathFinder(snode+int(math.sqrt(len(obj)))+1,nap,counts)
            if obj[snode]['Y']>1:
                if obj[snode-int(math.sqrt(len(obj)))+1]['Z'] <= nap and obj[snode-int(math.sqrt(len(obj)))+1]['RGB']!="#0000FF":
                    self.pathFinder(snode-int(math.sqrt(len(obj)))+1,nap,counts)


        if obj[snode]['Y']<int(math.sqrt(len(obj))):
            if obj[snode+int(math.sqrt(len(obj)))]['Z'] <= nap and obj[snode+int(math.sqrt(len(obj)))]['RGB']!="#0000FF":
                self.pathFinder(snode+int(math.sqrt(len(obj))),nap,counts)
        
        if obj[snode]['Y']>1:
            if obj[snode-int(math.sqrt(len(obj)))]['Z'] <= nap and obj[snode-int(math.sqrt(len(obj)))]['RGB']!="#0000FF":
                self.pathFinder(snode-int(math.sqrt(len(obj))),nap,counts)
        
class MapCreator:
    def drawPath(self,start):
        array = np.zeros([501, 501, 3], dtype=np.uint8)
        array[:,:] = [248, 213, 104] #Sandy backside
        
        count=0
        for _ in obj:
            if obj[count]["RGB"] == "#0000FF":
                array[obj[count]["X"],obj[count]["Y"]] = [55, 102, 246] #blue line
            count+=1
        startpar=0
        for _ in range(0,start):
            array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
            startpar+=1
        for _ in range(start,secondhalf):
            array[obj[startpar]["X"],obj[startpar]["Y"]] = [255, 97, 71] #red starting point
            startpar+=1
        img = Image.fromarray(array)
        img.save('testrgb.png')


# # Dit is om je data te vernieuwen
# names = MDCreator()
# names.setAllData()

# Dit is om het algoritme uit te voeren
start=55
secondhalf=int(math.sqrt(len(obj)))
nap=4

find = MAlgorithm()

startpar=0
for _ in range(0,start):
    find.checknode(startpar,nap) #lengte 1e rij meegeven voor werken met rechthoeken
    startpar+=1
for _ in range(start,secondhalf):
    find.checknode(startpar,nap) #lengte 1e rij meegeven voor werken met rechthoeken
    startpar+=1

#Dit is om het pad te tekenen
draw = MapCreator()
draw.drawPath(start)