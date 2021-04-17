#Napisać funkcję,  która dla danego n odnajduje i wyświetla wszystkie liczby całkowite 
# dodatnie <=n, których suma podzielników (łącznie z 1) jest równa tej liczbie.
# Przykład:  6 = 1 + 2 + 3
def dividers(a):
    l=range(1,int(a/2)+1)
    tab=[]
    s=0
    for i in l:
        if (a%i==0):
            s+=i
            tab.append(i)
    if(s==a):
        print("sum of dividers is equql ",a)
        print(tab)
    else:
        print("sum of dividers is different from ",a)

dividers(10)    
dividers(11)
dividers(6)    
dividers(12)