# !/usr/bin/env python
# -*- coding:utf-8 -*-
import random,sys,time
import requests
from bs4 import BeautifulSoup
num = input("Please input number of Players : ")
num = int(num)
members = ['Player'+str(i+1) for i in range(num)]
# members.append('AI')
random.shuffle(members)
print(members,end="\n\n")
memory=[]
first_word = input("Please input the first word : ")
memory.append(first_word)
print("Let's start ...\n")
time.sleep(4)

#入力された文字が辞書内にあるか判断。(weblio)
def judge_exist_in_dictionary(input_word):
    weblio_data = requests.get("http://ejje.weblio.jp/content/"+input_word)
    soup = BeautifulSoup(weblio_data.text,'html.parser')
    word_meanings = soup.findAll("td",class_ = 'content-explanation')
    length = len(word_meanings)
    if length is 0:
        print("The word is not in dictionary. You lose.\n")
        sys.exit()
    else:
        pass

def main():
    while(True):
        for i in range(num):
            word = input("Turn of " + members[i] + " : ")
            judge_exist_in_dictionary(word)
            if word not in memory and (word[:1] == memory[-1][-1:]) and word.endswith('n') is False:
                print("OK! Please change the next Player\n")
            else:
                if word in memory:
                    print("{} is already out at the {}. You lose.\n".format(word,memory.index(word)))
                if word[:1] is not memory[-1][-1:]:
                    print("You must have put {} at Initial. You lose.\n".format(memory[-1][-1:]))
                if word.endswith('n') is True:
                    print("Not [n] at the end of the word. You lose.\n")
                sys.exit()
            memory.append(word)
            # print(memory)
if __name__ == '__main__':
    main()

#また、その単語の意味を日本語で説明する文章を表示。
