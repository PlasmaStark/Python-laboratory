# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:57:59 2021

@author: Leonardo
"""

iteratore = range(256)
S = bytearray(iteratore)

def setup(key):
    j = 0
    k = len(key)
    
    for i in iteratore:
        j = (j+S[i]+key[i % k]) % 256
        S[i],S[j] = S[j], S[i]

def print_state():
    for i in range(8):
        print(S.hex()[32*i:32*(i+1)-1])
        
def key_stream(L):
    out=bytearray(L)
    i = j = 0
    for k in range(L):
        i = (i+1) % 256
        j = (j + S[i]) % 256
        S[i],S[j] = S[j], S[i]
        out[k] = S[(S[i]+S[j]) % 256]
    return out

def tr_buffer(buffer):
    L = len(buffer)
    keystream = key_stream(L)
    for i in range(L):
        buffer[i] = buffer[i]^keystream[i]
    return buffer