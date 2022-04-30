# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:55:30 2021

@author: Leonardo
"""

# -------------------------------------------------
# MODIFIED RSA with FIXED VALUE for e = 65537
# -------------------------------------------------
# input format: [file1] [file2]
# main() generates RSA keys, output format:
#   - private key (p*q,d) on 1st file
#   - public key (p*q,e) on 2nd file
# p,q get discarded for security reasons, but could 
# easily be saved in private key
# -------------------------------------------------

import sys
from simpy import randprime, base_solution_linear, igcd

def generateP(q,e,min,max):
    p = 0
    # it does seem wonky and slow, but for big values 
    # of q a true random p is very likely to be 
    # such that gdc(phi(n),e)=1
    while True:
        p = randprime(min,max)
        # phi(n) = (p-1)(q-1)
        phi = (p-1)*(q-1)
        if igcd(phi,e) == 1:
            break
    return p

def generateD(e,phi):
    # we need d with de = 1 mod(phi) <=> de = 1 + k(phi) 
    #                                <=> de-k(phi)=1
    # where phi := phi(n)...
    # (s,t)=base_solution_linear(a,b,c) solves a=sb+tc; first we
    # shall solve for 
    # a = 1
    # b = e 
    # c = -phi
    # and then from bas_sol_lin(1,e,-phi)=(d,k) we shall get d...
    # a = sb + t( c )
    # 1 = de - k(phi)
    
  # s,t = base_solution_linear(a,b, c)
    d,_ = base_solution_linear(1,e,-phi)
    return d

def writeListOfDataOnFile(lista, file):
    # writes list of keys on file, input has 
    # requested format (hexadec, has /n, etc)
    writer=open(file,"w");
    for i in lista:
        writer.write(hex(i))
        writer.write('/n')
    writer.close()

def main():
    # [read files] ----------------------------
    argc=len(sys.argv)
    if(argc!=3):
        print(sys.argv[0]+" requires: private.key, public.key")
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
    p = generateP(q,e,min,max)
    n = p*q
    phi = (p-1)*(q-1)
    d = generateD(e,phi)
    
    privatekey = [n,d]
    publickey = [n,e]
    # p,q get discarded    
    
    # [save numbers] --------------------------
    writeListOfDataOnFile(privatekey, fileprivate)
    writeListOfDataOnFile(publickey, filepublic)
           
if __name__=="__main__":
    main()