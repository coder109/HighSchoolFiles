#-*-coding:UTF-8-*-
#Modules
import random as rd

#Dict
file=open('Keyword.txt','r')
dict=[i for i in file]
dict="".join(dict)
dict_add=dict.split(" ")#12
file.close()
file=open('KWORD.txt','r')
dict=[i for i in file]
dict="".join(dict)
dict_kword=dict.split("，")#18
file.close()
dict_xuci=["居然是","竟然是","原来是","穿着","持着","\n","\n","怎么会"]#8
dict_name=["洛长风","梅瑛","沈辰","宋子明"]#4
dict_clothes=["穿着月白长衫","穿着常山龙虎袍","穿着华盛顿大列巴","穿着巴山夜雨涨秋池","穿着李白同款校服","穿着床前明月光"]#6
dict_punc=[",","。","!","?"]#4

#LOOP
j=0
while j<270:
    a=rd.randint(1,10)
    b=rd.randint(1,10)
    i=a*b+a/b+j%a+1
    i=int(i)
    temp_xuci=i%8
    temp_name=i%4
    temp_add=i%12
    temp_punc=i%4
    temp_clothes=i%6
    temp_kword=i%18
    add=dict_add[temp_add]
    xuci=dict_xuci[temp_xuci]
    name=dict_name[temp_name]
    punc=dict_punc[temp_punc]
    clothes=dict_clothes[temp_clothes]
    kword=dict_kword[temp_kword]
    if i%2==0:
        print(kword+xuci+name+punc,end="")
    else:
        print(name+clothes+"在"+add+"打"+name+punc,end="")
    j=j+1
