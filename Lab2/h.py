from dis import dis
import math


mypoint = input().split()
myx = int(mypoint[0])
myY= int(mypoint[1])

Distli = []

n = int(input())
for i in range(n):
    points = input().split()
    Xpoint = int(points[0])
    Ypoint = int(points[1])
    helper = f'{Xpoint} {Ypoint}'
    dist = math.sqrt((myx-Xpoint)*(myx-Xpoint) + (myY-Ypoint) * (myY-Ypoint))
    Distli.append((dist,helper))
Distli.sort()
for vls in Distli:
    print(vls[1])

