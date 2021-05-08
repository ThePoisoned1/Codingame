import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
yValues = []
startX = None
endX = None
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if startX == None:
        startX = x
    else:
        if startX > x:
            startX = x
    if endX == None:
        endX = x
    else:
        if endX < x:
            endX = x
    yValues.append(y)

yValues=sorted(yValues)
startY=yValues[n//2]
total = endX-startX
for y in yValues:
    total+=abs(startY-y)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(int(total))
