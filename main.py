# https://www.pcstore.com.tw/adm/psearch.htm?store_k_word=[base64編碼]&slt_k_option=1
import base64
import requests
from bs4 import BeautifulSoup
USERinput = base64.b64encode(input("Search:").encode('utf-8'))
url = "https://www.pcstore.com.tw/adm/psearch.htm?store_k_word="+str(USERinput,'utf-8')+"&slt_k_option=1"
Response = requests.get(url)
Response.encoding = 'Big5'

# print(url)
# print(Response.status_code)
# print(Response.text)

soup = BeautifulSoup(Response.text, "html.parser")
find = soup.select("div.pic2t.pic2t_bg a")
for print_ in find:
    print("-----------------------------------")
    print(print_.text, print_.get('href'))
