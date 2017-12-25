# -*- coding:utf-8 -*-
print("---- Input your name ----\n")
members=[]
count=0
while(True):
    try:
        members.append(input("What's your name ? : "))
        count+=1
    except EOFError:
        print("\n")
        break
print(members)
