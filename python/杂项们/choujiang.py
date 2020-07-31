# -*- coding:UTF-8 -*-

#Import
import random as rd

#MainProcedure

#Loop
i,n,r=0,0,1
while r<=10000:
    rnum=rd.randint(0,10000)
    if rnum==10000:
        #print("SSR!")
        i=i+1
    elif rnum<10000:
        #print("LOSER!")
        n=n+1
    r=r+1
print(str(i)+"   "+str(n))