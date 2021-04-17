# 0 – 25 000 15% dochodu
# 25 000 – 50 000   3 750 + 28% dochodu powyżej 25 000
# 50 000 – 75 000    10 750 + 31% dochodu powyżej 50 000
# > 75000   18500 +40% dohodu powyżej 75 000
#

def podatki(d):
    if(d<0):
        return 0
    elif(d>=0 and d<25000):
        return(d*0.15)
    elif(d>=25000 and d<50000):
        return (d-25000) *0.28 +3750
    elif(d>=50000 and d<=75000):
        return(10750+(d-50000)*0.31)
    else:
        return(18500+(d-75000)*0.75)

print('podatki od dochodu -1 ',podatki(-1))
print('podatki od dochodu 17 ',podatki(17))
print('podatki od dochodu 25000 ',podatki(25000))
print('podatki od dochodu 100000 ', podatki(100000))
print('podatki od dochodu 24999 ',podatki(24999))