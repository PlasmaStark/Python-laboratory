# this library will contain code & functions to operate with our 
# new alphabet; we will use it in crypt. algorythms

# set up letters and our version of the ascii code 

def set_up():
    lista=[chr(x) for x in range(32,127)]
    extra = ['à','è','é','ì','ò','ù','€','\n']
    lista += extra
    
    dizionario={chr(x):x-32 for x in range(32,127)}
    for i in range(len(extra)):
        dizionario[extra[i]]=95+i
        
    return dizionario,lista
