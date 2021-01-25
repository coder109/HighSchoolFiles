#-*-coding:UTF-8-*-
from numpy import *
import matplotlib.pyplot as plt
 
x=linspace(0,10,50000)
y=x/2-cos(x)-pi/4
plt.figure()
plt.plot(x,y)
plt.savefig("easyplot.png")#导出图像入图片
plt.show()