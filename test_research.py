# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

input_word = input("input word: ")
weblio_data = requests.get("http://ejje.weblio.jp/content/"+input_word)
soup = BeautifulSoup(weblio_data.text,'html.parser')
word_meanings = soup.findAll("td",class_ = 'content-explanation')
len2 = len(word_meanings)
if len2 is 0:
    print("Nothing")
else:
    print("True")
# for i in range(len2):
#     print(word_meanings[i].text)
