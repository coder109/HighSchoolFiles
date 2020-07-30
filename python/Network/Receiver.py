#-*-coding:UTF-8-*-

#Modules
from tkinter import *
from tkinter import messagebox as msg
from requests import *

#Function
def start():
    global usr
    url="http://www."+etry_url.get()
    a=usr.get()
    if a==0:
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
    elif a==1:
        headers = {'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'}
    elif a==2:
        headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
    else:
        headers={}
    r=get(url,headers=headers)

#CreateWindow
window=Tk()
window.geometry("500x500")

#Labels
lbl_url=Label(window,text="Url:")
lbl_url.grid(column=0,row=0)

#Entry
etry_url=Entry(window,width=20)
etry_url.grid(column=1,row=0)

#Header_RadioBtn
usr=IntVar()
usr_agt1=Radiobutton(window,text="Win/Mozilla",value=0,variable=usr)
usr_agt1.grid(column=1,row=1)
usr_agt2=Radiobutton(window,text="IE9.0",value=1,variable=usr)
usr_agt2.grid(column=2,row=1)
usr_agt3=Radiobutton(window,text="MAC/Mozilla",value=2,variable=usr)
usr_agt3.grid(column=3,row=1)
usr.set(1)

#Button
btn=Button(window,command=start)
btn.grid(column=2,row=0)

#Mainloop
window.mainloop()