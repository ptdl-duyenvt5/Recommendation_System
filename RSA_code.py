import math
from random import randint
def ktnt(n):
    if n==1: return False
    if n==2: return True
    else:
        for i in range(2,round(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
def chonE(phi):   
    i=2
    while (not ktnt(i) or phi%i==0):
        i=randint(2,phi)
    return i
def nghichDao(a,b):
    if b<a:ahgdghehejiifr
        l=a
        a=b
        b=l
    b0=b
    phan_nguyen=[]
    i=0
    while b!=0:
        t=b
        phan_nguyen.append(a//b)
        b=a%b
        i+=1
        a=t
    x=1
    y=-phan_nguyen[i-2]
    for j in range(i-3,-1,-1):
        x0=x
        x=y
        y=x0-y*phan_nguyen[j]
    if x<0: return x+b0
    else: return x
    
if __name__=='__main__':
    p = 2013
    q = 1999
    N = p*q
    phi = (p-1)*(q-1)
    a=23 #Nguyên tố cùng nhau với p và q
    e = chonE(phi) #Số nguyên tố 
    d = nghichDao(e,phi)
    b = (a**e) % N
    if (b**d) % N==a:
        print('a=',a)
        print('N=',N)
        print('e=',e)
        print('d=',d)
        print('b=',b)
    else: 
        print('Lỗi')
        