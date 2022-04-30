# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:21:08 2021

@author: Leonardo
"""

import sys
from getpass import getpass as getp
import vigenere as vig

def main():   
    if len(sys.argv)!=2:
        print(sys.argv[0]+" fileout")
        return 0
    else:      
        # ---------- [ GET KEYSTREAM ] --------------
        key= getp('Password:')
        if len(key)==0:
            # keystream NOT OK
            print("La chiave non può essere vuota!")
        else:
            # keystream OK
            KeyStream=vig.get_stream(key)
            fileout=sys.argv[1]
            f=open(fileout,"w")
            
            # ---------- [ GET MESSAGE ] --------------
            print("Inserisci il messaggio da registrare. Finisci con EOF")
            
            for line in sys.stdin:
                for car in line:
                    localstream = int(next(KeyStream))
                    f.write(vig.cryptWithoutStream(car,localstream))
            f.close()
        
        
if __name__=="__main__":
    main()
