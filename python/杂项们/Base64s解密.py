#-*- coding: UTF-8 -*-
import base64 as b64
s=str(input("输入要解密的内容："))
decode=b64.b64decode(s)
print("解密结果:")
print(decode)
