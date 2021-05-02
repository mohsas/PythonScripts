<#EBieleninikPWr WIZ136. Napisać program, który tworzy listę 20 liczb 
wg poniższego schematu:fn=  2   dla n = 0
1                dla n = 1
fn-1+ fn-2 dla n > 2
Na podstawie pierwszej listy tworzy listę drugą wypełnioną wg schematuf2/f1,  f3/f2,  ........ fn/fn-1Wyświetla obie listy.Uwaga: Wykorzystać informacje
 o listach zamieszczone w pliku Python_cz_2
#>
def Fibonacci(n):
    t=[0]x20
    f0=2
    f1=1
    for i in range(1,20):
        fn=f0+f1
        f1=f0
        f0=fn
set