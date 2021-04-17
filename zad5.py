#
# Program calculates if year us a lead year and howmany days has a month
# Think about February
#
#
choices = {'January':31,'February':28, 'March':31, 'April':30, 'May':31, 'June':30,'July':30,'August':31,'September':30,'October':31, 'November':30,'December':31}
def lead(year,month):
    m=choices.get(month)
    if((year%4==0 and year%100 !=0) or year%400==0):
        if(m==28):
            m=m+1
        print(year,' is a lead year', ' Month ',month,' has ',m,' days')
    else:
        print(year,' is not a lead year', ' Month ',month,' has ',m,' days')
lead(2020,'January')
lead(2000,'February')
lead(1600,'February')
lead(2021,'January')
lead(2021,'February')
lead(4000,'February')    
lead(2400,'February')
