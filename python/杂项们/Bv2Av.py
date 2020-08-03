#-*-coding:UTF-8-*-
#Modulues
from tkinter import *
from tkinter.messagebox import *

#Main
#Create
window=Tk()

#Geometry
window.geometry("400x400")

#Alphabet
alphabet = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'

#Functions
def dec():#Decode
    try:
        x=etr_enc.get()
        r = 0
        for i, v in enumerate([11, 10, 3, 8, 4, 6]):
            r += alphabet.find(x[v]) * 58**i
        temp=(r - 0x2_0840_07c0) ^ 0x0a93_b324
        showinfo("结果",str(temp))
    except:
        showerror("ERROR!","ERROR!")
    
def enc():#Encode
    try:
        x=etr_dec.get()
        tmp_li=[]
        for i in list(x):
            try:
                int(i)
                tmp_li.append(i)
            except:
                pass
        x="".join(tmp_li)
        x=int(x)
        x = (x^ 0x0a93_b324) + 0x2_0840_07c0
        r = list('BV1**4*1*7**')
        for v in [11, 10, 3, 8, 4, 6]:
            x, d = divmod(x, 58)
            r[v] = alphabet[d]
        temp=''.join(r)
        showinfo("结果",str(temp))
    except:
        showerror("ERROR!","ERROR!")


#GUI
#Label
lbl_enc=Label(window,text="输入BV号")
lbl_enc.grid(column=0,row=0)
lbl_dec=Label(window,text="输入AV号:")
lbl_dec.grid(column=0,row=1)

#Entry
etr_enc=Entry(window,width=20)
etr_enc.grid(column=1,row=0)
etr_dec=Entry(window,width=20)
etr_dec.grid(column=1,row=1)

#Button
btn_enc=Button(window,command=enc,text="AV变BV")
btn_enc.grid(column=0,row=2)
btn_dec=Button(window,command=dec,text="BV变AV")
btn_dec.grid(column=1,row=2)

#Mainloop
window.mainloop()