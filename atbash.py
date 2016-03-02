#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from base import rus_abc, rus_cabc

rev_en = {rus_cabc[k]:rus_cabc[32-k] for k in range(33)}
rev_de = {rus_cabc[32-k]:rus_cabc[k] for k in range(33)}

def encrypt(text):
    newtext = ""
    for x in text:
        l = x.islower()
        cur = x.upper()
        if cur in rus_abc:
            el = rev_en[cur]
            newtext += el.lower() if l else el
        else:
            newtext += x
    return newtext

decrypt = lambda t: encrypt(t)

if __name__ == "__main__":
    text = input("Text: ")
    print(encrypt(text))