#-*-coding:UTF-8-*-
#Modules
import random as rd
import sys

'''
原理备忘：
一级密钥：33-126之间随机选择数字(num_dict)，作为ASCII转换为十进制。
二级密钥：临时随机数(num_temp)。
密文：将明文的元素转为ASCII与临时随机数相乘，生成数字为该字符的密文。
'''

#Judgement
#Main
#Input
wrd=input("输入要加密的语句:")
#f=open('test.txt','r')
#wrd=f.read()
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
