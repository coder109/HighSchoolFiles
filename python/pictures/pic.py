#-*-coding:UTF-8-*-
from numpy import *
import matplotlib.pyplot as plt
 
x=linspace(-1,1,100)
y=exp(exp(x))
plt.figure()
plt.plot(x,y)
#plt.savefig("easyplot.png")#导出图像入图片
plt.show()