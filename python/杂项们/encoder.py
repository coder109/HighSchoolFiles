#-*-coding:UTF-8-*-
#Modules
import random as rd
import sys

#Judgement
#Main
#Input
wrd=input("输入要加密的语句:")
if len(wrd)==0:
    sys.exit(1)

else:
    #GenerateDict
    i=0
    lis=[]
    while i<20:
        num_dict=rd.randint(33,126)#65,122
        chac=chr(num_dict)
        lis.append(chac)
        i=i+1
    keyword="".join(lis)#length=20

    #Encode
    wrd=list(wrd)
    resu=[]
    dbl_key=[]
    for i in wrd:
        num_temp=rd.randint(0,19)
        res=ord(i)*ord(lis[num_temp])
        resu.append(str(res)+" ")
        dbl_key.append(str(num_temp)+" ")
    result="".join(resu)
    deblk="".join(dbl_key)

    #Output
    print("一级秘钥："+keyword)
    print("二级秘钥："+deblk)
    print("结果是："+result)

