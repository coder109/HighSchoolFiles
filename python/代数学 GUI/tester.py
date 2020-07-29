#-*-coding:UTF-8-*-
#Modules
from numpy import *
import matplotlib.pyplot as plt
import pylab

#Main
seat_num=1
list_num=[]
list_res=[]
while seat_num<=100:
    tempo=0
    i=0
    while i<=seat_num:
        tempo=tempo+1
        i=i+2
    list_num.append(seat_num)
    list_res.append(tempo)
    seat_num=seat_num+1
        
 
#MainModule
if __name__=="__main__":
    x=list_num
    y=list_res
    z1 = polyfit(x, y, 10)              # 曲线拟合，返回值为多项式的各项系数
    p1 = poly1d(z1)                    # 返回值为多项式的表达式，也就是函数式子
    print(p1)
    y_pred = p1(x)                        # 根据函数的多项式表达式，求解 y
    # print(np.polyval(p1, 29))             根据多项式求解特定 x 对应的 y 值
    # print(np.polyval(z1, 29))             根据多项式求解特定 x 对应的 y 值    
    plot1 = pylab.plot(x, y, '*', label='original values')
    plot2 = pylab.plot(x, y_pred, 'r', label='fit values')
    pylab.title('')
    pylab.xlabel('')
    pylab.ylabel('')
    pylab.legend(loc=3, borderaxespad=0., bbox_to_anchor=(0, 0))
    pylab.show()
    pylab.savefig('p1.png', dpi=200, bbox_inches='tight')                   