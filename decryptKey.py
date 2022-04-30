# -*- coding: utf-8 -*-
"""
Created on Mon May 24 18:51:21 2021

@author: Leonardo
"""

# --------------[ key decrypter ]------------------
# input format: [file1] [file2] [file3]
# main() decrypts session key from file2, requires
#   - file1: private key
#   - file3: session key (decrypted, progr. output)
# -------------------------------------------------

import sys

def keyFileReader(file):
    # reads data, would check for file format but I do not 
    # know how, I shall suppose it is correct... 
    # output is given as list
    reader=open(file,"r")
    x,y = reader.readlines()
    reader.close()
    return int(x,0), int(y,0)
    # 0x prefix automatically identifies read number
    # as hexadecimal
   
def cryptedFileReader(file):
    # reads data, crypted file only has one line
    reader=open(file,"r")
    [z] = reader.readlines()
    reader.close()
    return int(z,0) 
   
def main():
    # [read files] ----------------------------
    argc=len(sys.argv)
    if(argc!=4):
        print(sys.argv[0]+" requires: private.key, session.key.crypted, session.key")
        return
    else:
        fileprivate=sys.argv[1]
        filecrypted=sys.argv[2]
        filedecrypted=sys.argv[3]
    
    skey_crypt = cryptedFileReader(filecrypted)
    n,d = keyFileReader(fileprivate)
    
    # [decrypt] -------------------------------  
    skey = pow(skey_crypt,d,n)
    
    # [save data] -----------------------------
    output = open(filedecrypted,"w")
    output.write(hex(skey))
    output.close
           
if __name__=="__main__":
    main()