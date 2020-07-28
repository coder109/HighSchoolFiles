#-*- coding:UTF-8 -*-
import base64 as b64
s=str(input("输入要加密的内容:"))
encode=b64.b64encode(s)
print("加密结果：")
print(encode)
