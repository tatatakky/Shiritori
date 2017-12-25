#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
def AI_reserch_from_dictionary(initial_word):
    html = requests.get("http://tokoton-eitango.com/eitango/wordindex/"+initial_word)
    soup = BeautifulSoup(html.text,"html.parser")
    string_include_tag = soup.findAll("td",style="width: 50%; text-align: left; padding-left: 10px;")
    for i in range(len(string_include_tag )):
        print(string_include_tag[i].text)

AI_reserch_from_dictionary("B")
