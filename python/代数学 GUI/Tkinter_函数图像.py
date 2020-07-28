#-*-coding:UTF-8-*-
#Modules
from numpy import *
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox as msg

#CreateAWindow
window=Tk()
window.geometry("600x600")

#Function
def calc():
    try:
        li_temp=etry_linspace.get().split()
        lis_temp=etry_num.get().split()
        lis=[]
        li=[]
        for i in li_temp:
            li.append(int(i))
        for j in lis_temp:
            lis.append(int(j))
        min=li[0]
        max=li[1]
        num=lis[0]
        x=linspace(min,max,num)
        plt.figure()
        plt.plot(x,eval(etry_function.get()))
        plt.show()
    except:
        msg.showerror(title="ERROR!",message="ERROR!")

#Labels
lbl_function=Label(window,text="函数解析式：")
lbl_function.grid(column=0,row=0)
lbl_linspace=Label(window,text="函数区间：")
lbl_linspace.grid(column=0,row=1)
lbl_num=Label(window,text="拟合点数：")
lbl_num.grid(column=0,row=2)
lbl_warn=Label(window,text="函数区间格式：最小值 最大值（用空格隔开）")
lbl_warn.grid(column=0,row=3)

#Entrys
etry_function=Entry(window,width=20)
etry_function.grid(column=1,row=0)
etry_linspace=Entry(window,width=20)
etry_linspace.grid(column=1,row=1)
etry_num=Entry(window,width=20)
etry_num.grid(column=1,row=2)

#Button
btn=Button(window,text="开始！",command=calc)
btn.grid(column=2,row=1)


#Mainloop
window.mainloop()