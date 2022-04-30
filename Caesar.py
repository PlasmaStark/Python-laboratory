# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:39:42 2021

@author: Leonardo
"""

import alphabet

A,N = alphabet.set_up()
len_alphabet = len(N)

def get_fun(int):
    return lambda n: (int + n)%len_alphabet

def look_up(int):
    encrypt = get_fun(int)
    return {N[i] : N[encrypt(i)] for i in range(0,len_alphabet)}