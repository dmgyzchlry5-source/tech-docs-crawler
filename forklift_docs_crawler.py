import requests
from bs4 import BeautifulSoup
url="https://blog.csdn.net/weixin_45678901/article/details/123456789"
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text
