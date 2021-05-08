import numpy as np
import math

def getDist(lonA,latA,lonB,latB):
    x = (lonB-lonA) * math.cos((latB+latA)/2)
    y = latB-latA
    return math.sqrt(x*x+y*y)*6371


lon = np.deg2rad(float(input().replace(",",".")))
lat = np.deg2rad(float(input().replace(",",".")))
n = int(input())
minDist = None
for i in range(n):
    defib=input().split(";")
    defib[4]=np.deg2rad(float(defib[4].replace(",",".")))
    defib[5]=np.deg2rad(float(defib[5].replace(",",".")))
    dist = getDist(lon,lat,defib[4],defib[5])
    if minDist==None:
        minDist=dist
        closestDefib = defib
    else:
        if dist<minDist:
            minDist=dist
            closestDefib = defib

print(closestDefib[1])
