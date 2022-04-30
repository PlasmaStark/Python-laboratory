# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:50:31 2021

@author: Leonardo
"""

import alphabet

A,N = alphabet.set_up()
len_alphabet = len(N)

# works with affine encrypt. function y = a*x + b
# decrypt. done via function (y-b)/a
# ------------------------
# CRYPT PARAMETERS: (a,b)
# DECRYPT PARAMETERS: (1/a,-b/a)

def get_fun(a,b):
    return lambda n: (a*n + b)%len_alphabet

def look_up(a,b):
    encrypt = get_fun(a,b)
    return {N[i] : N[encrypt(i)] for i in range(0,len_alphabet)}
