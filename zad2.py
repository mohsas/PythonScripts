#boki trojkata musza spelnić nierówność
# dowolny  bk musi byc mniejsze niż sumę pozostałych
#Czyli dla boków a,b,c zachodza nierówności
# a<b+c; b<a+c; c<a+b
import math
print('Podaj bok a')
a=float(input())
print('Podaj bok b')
b=float(input())
print('Podaj bok c')
c=float(input())
def czytajBoki(a,b,c):
    t=(a<(b+c) and b<(a+c) and c<(a+b))
    return t

def obliczObwod(a,b,c):
    if(czytajBoki(a,b,c)):
        return a+b+c
    else:
        print('Nie można zbudować trójkąta')
        return -1
def obliczPole(a,b,c):
    if(czytajBoki(a,b,c)):
        o=(a+b+c)/2
        p=math.sqrt(o*(o-a)*(o-b)*(o-c))
        return p
    else:
        print('Nie można zbudować trójkąta')
        return -2

def jakiTrojkatBoki(a,b,c):
    if(czytajBoki(a,b,c)):
        if(a==b and b==c):
            print('Trójkąt równoboczny')
        elif((a==b and b!=c) or(a==c and b!=c) or (b==c and a!=c) ):
            print('Trójkąt równoramienny')
        else:
            print('Trójkąt dowolny')
    else:
        print('Nie można zbudować trójkąta')


def jakiTrojkatKaty(a,b,c):
    if(czytajBoki(a,b,c)):
        a2=a*a
        b2=b*b
        c2=c*c
        if(a2+b2==c2 or a2+c2==b2 or b2+c2==a2):
            print('mamy trójkąt prostokątny')
        elif(a2+b2<c2 or a2+c2<b2 or b2+c2<a2):
            print('mamy trójkąt ostrokątny')
        else:
            print('mamy trójkąt rozwartokątny')
    else:
        print('Nie można zbudować trójkątna')

czytajBoki(a,b,c)
obliczObwod(a,b,c)
obliczPole(a,b,c)
jakiTrojkatBoki(a,b,c)
jakiTrojkatKaty(a,b,c)