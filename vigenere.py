# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:35:44 2021

@author: Leonardo
"""

import alphabet
N,S = alphabet.set_up()
lenalphabet = len(S)

# ---------- [ ENCRYPT in ALPHABET ] --------------

# encrypts key w/ alphabet.py (from letters to numbers)
# returns list to be readable output
def alphToList(key):
    return [N[key[i]] for i in range(len(key))]

# decrypts from list of numbers (from numbers to letters)
# decryption from string would be inexact
def alph(lista):
    s = ""
    templist = [S[n] for n in lista]
    for j in templist:  
    # from list of strings to string
        s += j
    return s


# ---------- [ ENCRYPT in VIGENERE ] --------------

# does both encrypt & decrypt
def crypt(string, keystream):
    L = len(string)
    localkey = [next(keystream) for i in range (0,L)]
    # but string is a string... we need numbers...
    # also, we need to iterate in (0,lenalphabet)... hence the %
    string_tolist = alphToList(string)
    temp = [(string_tolist[i]^localkey[i]) % lenalphabet for i in range(0,L)]
    
    # and then we need strings again...
    return alph(temp)

# programmer takes responsability for KEY length being the
# same as CHAR length (== 1) and KEY coming from stream!!
def cryptWithoutStream(char, key):
    char_asinteger = N[char]
    return S[(char_asinteger^key) % lenalphabet]

# ---------- [ KEYSTREAM ] --------------

# returns keystream using encrypted key w/ alphabet.py
def get_stream(key):
    while True: # infinite cycles:
       for j in range(0,len(key)):
            yield N[key[j]] # yelds encrypted key