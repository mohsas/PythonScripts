import math
def prime(n):
    i=2
    while(math.pow(i,2)<=n):
        if(n%i==0):
            print(n," is not prime ")
            print("Number of iterations: ", i-1)
            return 0
            break
        else:
            i+=1
    else:
        print(n, " is prime ")
        print("Number of iterations:", i-1)
        return 1
        

#prime(10)
#prime(9)
#prime(8)
#prime(17)
#prime(15)
#prime(19)
#prime(4)
