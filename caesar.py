#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from base import rus_abc, rus_cabc

def encrypt(text, ch):
    newtext = ""
    for x in text:
        l = x.islower()
        cur = x.upper()
        if cur in rus_abc:
            el = rus_cabc[ (rus_abc[cur] + ch) % 33]
            newtext += el.lower() if l else el
        else:
            newtext += x
    return newtext

def decrypt(text, ch):
    newtext = ""
    for x in text:
        l = x.islower()
        cur = x.upper()
        if cur in rus_abc:
            el = rus_cabc[ (rus_abc[cur] - ch) % 33]
            newtext += el.lower() if l else el
        else:
            newtext += x
    return newtext

if __name__ == "__main__":
    text = input("Text: ")
    mode = int(input("Encrypt/decrypt [0/1]: "))
    ch = int(input("Shift: ")) % 33

    if mode == 0: # Encrypt 
        print(encrypt(text, ch))
    else:
        print(decrypt(text, ch))