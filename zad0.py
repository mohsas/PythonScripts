
# Obliczanie wartości f(x) =1 dla x>0; f(x)=0 dla x=0 f(x)=-1 dla x<0
import math
print('Podaj liczbę x:')
x=float(input())
def f(x):
    if(x<0):
        return -1
    elif(x==0):
        return 0
    else:
        return 1
print(f(x))
