def ciagzbiezny(n):
    while(n>1):
        if(n%2==0):
            print("n= ",n)
            n=n//2
            
        else:
            print("n= ",n)
            n=3*n+1
    print("ciag zbiezny do ",n)        

ciagzbiezny(15)
