# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:01:30 2021

@author: Leonardo
"""

# ---------------[ key crypter ]-------------------
# input format: [file1] [file2] [file3]
# main() crypts session key from file2, requires
#   - file1: public key
#   - file3: session key (crypted, progr. output)
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
   
def plainFileReader(file):
    # reads data, file only has one line
    reader=open(file,"r")
    [z] = reader.readlines()
    reader.close()
    return int(z,0) 
   
def main():
    # [read files] ----------------------------
    argc=len(sys.argv)
    if(argc!=4):
        print(sys.argv[0]+" requires: public.key, session.key, session.key.crypted")
        return
    else:
        filepublic=sys.argv[1]
        fileplain=sys.argv[2]
        filecrypted=sys.argv[3]
    
    skey = plainFileReader(fileplain)
    n,e = keyFileReader(filepublic)
    
    # [decrypt] -------------------------------  
    enc_skey = pow(skey,e,n)
    
    # [save data] -----------------------------
    output = open(filecrypted,"w")
    output.write(hex(enc_skey))
    output.close
           
if __name__=="__main__":
    main()