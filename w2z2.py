#Napisać funkcję, która oblicza i wyświetla liczby pierwsze 
# z podanego zakresu [a, b]. Wartości a, b wczytać z klawiatury. 
# Uwaga: wykorzystać zad 1.
from w2z1 import prime
a=(int)(input('Type a number a: '))
b=(int)(input('Type a number b: '))
c=[]
for x in range(a, b):
    if(prime(x)):
        print(x)
        c.append(x)
print(c)


