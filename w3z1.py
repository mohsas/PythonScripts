import math
import random

def stat (d):
    x=0
    y=0
    l=0
    while(l<d):
        x=print(random.randint(1, 4))
        if x==1:
            x+=1
        if x==2:
            y+=1
        if x==3:
            x-=1
        if x==4:
            y-=1
        r=x*x+y*y
        l=math.sqrt(r)
        print(d)
stat(10)