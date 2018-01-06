#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import random

def Chatbot_reserch_from_dictionary(initial_word):
    Chatbot_dictionary = []
    html = requests.get("http://learnersdictionary.com/3000-words/alpha/"+initial_word+"/"+str(3))
    soup = BeautifulSoup(html.text,"html.parser")
    string_include_kakko = soup.findAll("a",href=re.compile("/definition/"))
    for i in range(len(string_include_kakko)):
        string = string_include_kakko[i].text.strip().replace(" ","")
        if '(' in string:
            moji = string[:string.index("(")]
        else:
            moji = string

        # moji = string[:string.index("(")]
        # print(moji)
        Chatbot_dictionary.append(moji)

    print(random.choice(Chatbot_dictionary))

Chatbot_reserch_from_dictionary("a")
