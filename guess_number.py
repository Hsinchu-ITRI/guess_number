# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:44:18 2021

@author: Win10
"""
''' 產生一個 隨機整數 1~ 100 (不要印出來)
讓使用者重複輸入數字去猜
猜對的話 印出 "終於猜對了 !!"
猜錯的話 要告訴他 比答案大或小  '''

import random

r = random.randint(1, 10)
count = 0
while True:
    number = int(input('請輸入整數數字 1~10 之間 : '))
    count +=1
    print('這是你猜的第', count, '次')
    if number == r:
        print('你猜中了!!')
        break
    elif number > r:
        print('猜的數字比答案大')
    else:
        print('猜的數字比答案小')
