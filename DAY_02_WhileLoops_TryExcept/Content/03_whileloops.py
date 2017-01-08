# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 02:01:41 2017

@author: james
"""

word = ""
sentence = ""

while(word != "done"):
    word = input("Enter a new word. Enter done to see whole sentence: ")
    sentence = sentence + " " + word
    
print(sentence)
    