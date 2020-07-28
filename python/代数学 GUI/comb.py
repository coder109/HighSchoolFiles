#-*-coding:UTF-8-*-
from scipy.special import comb,perm

#输入
print("请输入下方数字：")
down=int(input())
print("请输入上方数字:")
up=int(input())

#判断
if type(down)==type(1) and type(up)==type(1):
    pass
else:
    print("请输入数字！")

#选择
print("请输入模式：")
print("1.组合")
print("2.排列")
choice=int(input())

#判断
if choice==1:
    result=comb(down,up)
    print(result)
if choice==2:
    result=perm(down,up)
    print(result)
else:
    print("请输入有效数字！")