#-*-coding:UTF-8-*-
#Main
#Input
keyword=input("输入一级秘钥：")
deblk=input("输入二级秘钥：")
wrd=input("输入要解密的语句:")

#Input2List
keyword=list(keyword)
deblk=deblk.split(" ")
wrd=wrd.split(" ")

#Decode
result=[]
i=0
while i<len(wrd):
    res=int(wrd[i])/ord(keyword[int(deblk[i])])
    result.append(chr(int(res)))
    i=i+1

#Output
print("解密结果："+"".join(result))