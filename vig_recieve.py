# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:41:33 2021

@author: Leonardo
"""

import sys
from getpass import getpass as getp
import vigenere as vig


def main():
    if len(sys.argv)!=2:
        print(sys.argv[0]+" filein")
        return 0
    else:
        # ---------- [ GET KEYSTREAM ] --------------
        key=getp('Password:')
        if len(key)==0:
            print("La chiave non può essere vuota!")
        else:
            KeyStream=vig.get_stream(key)
            filein=sys.argv[1]
            
            # ---------- [ DECODE & PRINT ] --------------
            f=open(filein,"r")
            lines=f.readlines()
            for car in lines:
                for c in car:
                    localstream = int(next(KeyStream))
                    print(vig.cryptWithoutStream(c,localstream),end='')
            print()
            f.close()
        
if __name__=="__main__":
    main()