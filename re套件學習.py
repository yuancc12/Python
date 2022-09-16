# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:47:18 2022

@author: User
"""
import re
def checkEmail1(email):

    a=re.compile(r"(^\D{1,4}\w{1,8})@\D{3,5}.[a-z]{3,5}")
    b=a.findall(email)
    if b==[]:
        return None
    else:
        return b



print(checkEmail1('abcd@hasdr.com.com')) #abcd
print(checkEmail1('abcd@hasdr.com')) #abcd
print(checkEmail1('abc5@hasdr.com')) # abc5
print(checkEmail1('abcd@h3sdr.com')) #None
print(checkEmail1('abcd@hasdr.c4m')) #None
print(checkEmail1('abcd@hasdrw.com')) #None
print(checkEmail1('ab@hasdr.com')) #ab
print(checkEmail1('abecd@hasdr.com')) #abecd
print(checkEmail1('1bcd@hasdr.com.com')) #None
print(checkEmail1('abcd@hasdr.co.com')) #None 
