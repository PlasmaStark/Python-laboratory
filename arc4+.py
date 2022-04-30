# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:57:59 2021

@author: Leonardo
"""

# ----------------------------------------------------------------
# ho provato a renderlo più veloce...
# prima importando numpy per il modulo, ma sembrava quasi barare, 
# quindi l'ho tolto; allora mi sono dato alle variabili ripetute
# ed ho testato com timeit la velocità
# ----------------------------------------------------------------

iteratore = range(256)
S = bytearray(iteratore)

def setup(key):
    # sets up S for ARC4
    j = 0
    k = len(key)
    
    for i in iteratore:
        j = (j + S[i] + key[i % k]) % 256 
        S[i], S[j] = S[j], S[i]

def print_state():
    # prints state S
    Str = S.hex()
    for i in range(8):
      # print(Str[32*i : 32*(i + 1) - 1]) <--- CORRETTO ERRORE!
        print(Str[32*i : 32*(i + 1)])
        
def key_stream(L):
    # returns keystream from length L
    out=bytearray(L)
    i = j = 0
    
    for k in range(L):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out[k] = S[(S[i] + S[j]) % 256]
    return out

def tr_buffer(buffer):
    # returns translated buffer
    L = len(buffer)
    keystream = key_stream(L)
    
    # encrypt/decrypt with bytewise XOR
    for i in range(L): 
        buffer[i] = buffer[i] ^ keystream[i]
    return buffer