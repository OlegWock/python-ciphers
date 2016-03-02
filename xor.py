#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from base import rus_abc_we, rus_cabc_we

def encrypt(text, key):
    txt = text.replace("Ё", "Е").replace("ё", "е")
    newtext = ""
    for x in txt:
        l = x.islower()
        cur = x.upper()
        if cur in rus_abc_we:
            el = rus_cabc_we[ (rus_abc_we[cur] ^ key)  ]
            newtext += el.lower() if l else el
        else:
            newtext += x
    return newtext


decrypt = lambda t, k: encrypt(t, k)

if __name__ == "__main__":
    text = input("Text: ")
    key = int(input("Key [0-31]:"))
    print(encrypt(text, key))