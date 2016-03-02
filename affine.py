#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from base import rus_abc, rus_cabc
import sys

# Extended Euclidean algorithm
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def encrypt(text, a, b):
    newtext = ""
    if not a in a_maybe:
        raise ValueError("a and m is not coprime")
    for x in text:
        l = x.islower()
        cur = x.upper()
        if cur in rus_abc:
            el = rus_cabc[(a*rus_abc[cur] + b) % 33]
            newtext += el.lower() if l else el
        else:
            newtext += x
    return newtext

def decrypt(text, a, b):
    newtext = ""
    if not a in a_maybe:
        raise ValueError("a and m is not coprime")
        return None
    for x in text:
        l = x.islower()
        cur = x.upper()
        if cur in rus_abc:
            el = rus_cabc[(modinv(a, 33) * (rus_abc[cur] - b)) % 33]
            newtext += el.lower() if l else el
        else:
            newtext += x
    return newtext

if __name__ == "__main__":
    text = input("Text: ")
    mode = int(input("Encrypt/decrypt [0/1]: "))
    a_maybe = [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32]


    a = int(input("Enter a [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32]: "))
    if not a in a_maybe:
        print("error")
        sys.exit(1)
    b = int(input("Enter b: "))


    newtext = ""

    if mode == 0: # Encrypt 
        print(encrypt(text, a, b))
    else:
        print(decrypt(text, a, b))