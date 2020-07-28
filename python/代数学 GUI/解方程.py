import sympy as sp
from fractions import Fraction
x = sp.Symbol('x')#设置自变量
print("写个方程：")
f =input()#输入方程
d=sp.solve(f)#解方程
print(d)
