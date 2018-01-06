# !/usr/bin/env python
# -*- coding:utf-8 -*-
import random,sys,time,re
import requests
from bs4 import BeautifulSoup

#出た単語の記憶装置
memory=['Shiritori']
#名前の登録
members=['You','Chatbot']

#入力された文字が辞書内にあるか判断。(weblio)
def judge_exist_in_dictionary(input_word):
    global number
    weblio_data = requests.get("http://ejje.weblio.jp/content/"+input_word)
    soup = BeautifulSoup(weblio_data.text,'html.parser')
    word_meanings = soup.findAll("td",class_ = 'content-explanation')
    length = len(word_meanings)
    if length is 0:
        print("The word is not in dictionary. {} lose. Continued {} times\n".format(members[number%2],number))
        sys.exit()

#ChatBotがwordを見つける。
def ChatBot(initial_word):
    Chatbot_dictionary = []
    html = requests.get("http://learnersdictionary.com/3000-words/alpha/"+initial_word+"/"+str(random.randint(1,4)))
    soup = BeautifulSoup(html.text,"html.parser")
    string_include_tag_a_href = soup.findAll("a",href=re.compile("/definition/"))
    for i in range(len(string_include_tag_a_href)):
        string = string_include_tag_a_href[i].text.strip().replace(" ","")
        if '(' in string:
            moji = string[:string.index("(")]
        else:
            moji = string
        Chatbot_dictionary.append(moji)
    return random.choice(Chatbot_dictionary)

#メイン
#ユーザー側の入力とChatBot側の入力
#入力値が　既存、Initialが違う、最後がn　の場合負け。
def main():
    global number
    number=0
    while(True):
        if number%2 is 0:
            word = input("Turn of " + members[number%2] + " : ")
        else:
            print("Turn of Chatbot :",end=" ")
            word = ChatBot(memory[-1][-1:])
            print(word)
        judge_exist_in_dictionary(word)
        if word not in memory and (word[:1] == memory[-1][-1:]) and word.endswith('n') is False:
            print("OK! Please change the next Player\n")
        else:
            if word in memory:
                print("{} is already out at the {}. {} lose. Continued {} times\n".format(word,memory.index(word),members[number%2],number))
            if word[:1] is not memory[-1][-1:]:
                print("You must have put [{}] at Initial. {} lose. Continued {} times\n".format(memory[-1][-1:],members[number%2],number))
            if word.endswith('n') is True:
                print("Not [n] at the end of the word. {} lose. Continued {} times\n".format(members[number%2],number))
            sys.exit()
        memory.append(word)
        number+=1
        # print(memory)
if __name__ == '__main__':
    # Ready_to_do_Shiritori()
    main()

#また、その単語の意味を日本語で説明する文章を表示。
