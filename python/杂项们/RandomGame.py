#-*-coding:UTF-8-*-
import numpy as np
s=0
i=1
while i<=2020:
    temp=2*np.sin(i*np.pi/2/180+np.pi/3/180)
    s=s+temp
    i=i+1
print(s)