import requests
from bs4 import BeautifulSoup

header={'User-Agent':'bilibili Security Browser'}
response=requests.get('http://120.92.217.120/api/admin',headers=header)
response.encoding='UTF-8'
html=response.text
print(html)