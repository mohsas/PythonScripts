#Wzorując się na przykładzie 6  napisać funkcję obliczającą sumę poniższego
#  szeregów:
# a)   f( ) =  1 + 1/2 + 1/3 +1/4 + ......
# b)   f( x ) = x –x3/3! + x5/5! –x7/7! + ....
# Uwaga szereg A jest rzbieżny
# W szeregu B można obliczyć element szeregu z elementu poprzedniego
# np a1(x)=x, a3(x)=-a1(x)*x^2/(3*2)
# Czyli można uogólnić wzór a_1(x)=x
# a_(2n+1)(x)=-a_(2n-1)*x^2/(2n+1)(2n) dla n=1,2,3....
#Pytanie : kiedy zakończymy obliczene?
#Odpowiedź np. kiedy dodając nowego członka nie wpływa na wynik
import math

def szeregA(eps):
    x1=1
    x2=0.5
    s=x1+x2
    i=0
    while(abs(x2-x1)>eps):
        x1=x2
        x2=x1/(1+x1)
        s=s+x2
        i+=1
    print("Liczba iteracji: ",i)
    return(s)
print("szeregA(0.1): ", szeregA(0.1))
print("szeregA(0.1): ", szeregA(0.01))
print("szeregA(0.1): ", szeregA(0.001))
print("szeregA(0.1): ", szeregA(0.00001))
print("szeregA(0.1): ", szeregA(0.000000001))
print("szeregA(0.1): ", szeregA(0.0000000001))


def szeregB(x,eps):
    x1=float(x)
    i=1
    s=x
    print(abs(x))
    #print(-x1* (math.pow(x,2)))/(i+3)
    while(abs(x1)>eps):
        i2=float(2*i)
        i3=i2*(i2+1)
        x3=-(math.pow(x,2))*x1/i3
        s=s+x3
        x1=x3
        i+=1
    print("liczba iteracji: ",i)
    print("Suma jest równa: ", s)
    print("Bląd jest równy ",eps)

szeregB(1.74,0.0001)
szeregB(3.14,0.00001)
szeregB(3.14,0.000001)

    