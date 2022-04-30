# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:55:30 2021

@author: Leonardo
"""

import sys
from simpy import randprime, base_solution_linear, igcd

def generateP(q,e):
    # generates P 
    p = 0
    while True:
        p = randprime(min,max)
        # phi(n)=(p-1)(q-1)
        phi = (p-1)*(q-1)
        if igcd(phi,e) == 1:
            break
        
    return p

def generateD(e,n):
    # we need d with de = 1 mod(n) <=> de = 1 + kn <=> de-kn=1...
    # (s,t)=base_solution_linear(a,b,c) solves a=sb+tc; first we
    # shall solve for 
    # a = 1
    # b = e 
    # c = -n
    # and then from b_s_l(1,e,-n)=(d,k) we shall get d
    d,_ = base_solution_linear(1,e,-n)
    return d

def main():
    # [read files] ----------------------------
    
    argc=len(sys.argv)

    if(argc!=3):
        print(sys.argv[0]+", private.key, public.key")
        return
    else:
        fileprivate=sys.argv[1]
        filepublic=sys.argv[2]
    
    # [generate numbers] ----------------------
    e = 65537 # is given
    min = 2**256
    max = 2*min
    
    # generate Q, P, D:
    q = randprime(min,max)
    p = generateP(q,e)
    n = p*q
    d = generateD(e,n)
    
    privatekey = [n,d]
    publickey = [n,e]
    # p,q get discarded    
    
    # [save numbers] --------------------------
    
    for i in privatekey:
        fileprivate.write(i)
        fileprivate.write('/n')
    
    for i in publickey:
        filepublic.write(i)
        filepublic.write('/n')
    
        
if __name__=="__main__":
    main()