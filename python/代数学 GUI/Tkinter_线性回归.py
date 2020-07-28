#-*-coding:UTF-8-*-
#import
from tkinter import *
from tkinter import messagebox as msg
from xianxinghuigui import *

#Create
window=Tk()
window.geometry("400x400")

#Labels
lbl_xi=Label(window,text="xi:")
lbl_xi.grid(column=0,row=0)
lbl_yi=Label(window,text="yi:")
lbl_yi.grid(column=3,row=0)
lbl_method=Label(window,text="Type SPACE among the numbers.")

#Entry
enter_xi=Entry(window,width=15)
enter_xi.grid(column=1,row=0)
enter_yi=Entry(window,width=15)
enter_yi.grid(column=4,row=0)

#Function
def calc():

    #Input Process
    li_temp=enter_xi.get().split()
    lis_temp=enter_yi.get().split()
    li=[]
    lis=[]

    #Judge Str?
    try:
        for i in li_temp:
            li.append(float(i))
        for i in lis_temp:
            lis.append(float(i))
    except:
        msg.showerror(title="ERROR",message="Type legal values!")
    else:
        #Judge
        if len(li)<2 or len(lis)<2 or li_temp==lis_temp or len(li)!=len(lis):
            msg.showerror(title="ERROR!",message="Error!")
        else:
        #Module Time!
            try:
                result=huigui(li,lis)
            except:
                msg.showerror(title="ERROR!",message="Check the numbers you type!")
            else:
                #Func Output Process
                a=result[0]
                b=result[1]
                result_ei=" ".join('%s' %id for id in result[2])
                R2=result[3]

                #Output
                msg.showinfo(title="Result:",message="f(x)="+str(b)+"x+"+str(a)+'\n'+"The list of ei:"+result_ei+'\n'+"R2 is"+str(R2))

#Button
btn=Button(window,text="Calculate",command=calc)
btn.grid(column=5,row=0)

#Loop
window.mainloop()