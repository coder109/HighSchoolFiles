#-*-coding:UTF-8-*-
from numpy import *
import matplotlib.pyplot as plt
 
x=linspace(0,10,5000)
y=sin(x)**2*sin(2*x)
plt.figure()
plt.plot(x,y)
plt.savefig("easyplot.png")#导出图像入图片
plt.show()