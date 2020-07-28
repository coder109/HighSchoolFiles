#-*-coding:UTF-8-*-

#input
a=int(input("请输入左上角："))
b=int(input("请输入右上角："))
c=int(input("请输入左下角："))
d=int(input("请输入右下角："))
n=a+b+c+d
K2=n*(a*d-b*c)**2/(a+b)/(a+c)/(d+c)/(b+d)

#output
print(K2)