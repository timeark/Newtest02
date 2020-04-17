# -*- coding: utf-8 -*-
def in_func(num01):
    return num01.isdigit() 



num_in = input("請輸入一個整數：")

while (in_func(num_in) == False):
    num_in = input("請輸入一個整數：")
else:
    print(num_in)








