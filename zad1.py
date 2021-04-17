
# Obliczanie wartości F(x) =0 dla x<0; 
# F(x)=1/4 dla 0<=x<1 
# F(x)=3/4 dla 1 <= x < 2 , 
# F(x)=1 dla x>=2
import math
print('Podaj liczbę x:')
x=float(input())
def F(x):
    if(x<0):
        return 0
    elif(x>=0 and x<1):
        return 1/4
    elif(x>=1 and x<2):
        return 3/4
    else:
        return 1
print(F(x))