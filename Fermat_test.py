# very basic script for a primality test via Fermat's little theorem

print("   [Fermat Test: check if n is (probably) prime!]   ")
print("# insert n number to test & b base (Fermat witness) #")
print("-----------------------------------------------------")

cycle = 1 # counts iterations

# main loop, only stops if user gets bored
while True:
    
    # get user input --------------------------------------
    if cycle == 1: 
        n = int(input("-> insert wannabe-prime n: ")) 
        b = int(input("-> insert base b: ")) # witness
    else: 
        # if not at first iteration, I already have n
        b = int(input("-> insert new base b: "))
    print("Testing " + str(n) + " with base " +str(b), end='')
    
    # test user input & tries to continue -----------------
    rem = pow(b,n-1,n)
    
    if rem == 1: # test returns true
        print("... " + str(n) + " is probably prime! ", end='')
        if cycle != 1: 
            print("Still probable prime at cycle " + str(cycle) + ".")
        
        # is user bored enough?
        go_on = input("Want to try further? (Y=yes, N=no) ") 
        if(go_on == "N"): 
            break # then stop...
            
    else: # test failed, no need to reiterate
        print("..." + str(n) + " is NOT prime! Remainder " + str(rem) + " is not 1. [working in mod" + str(n) + "]")
        if cycle != 1: 
            print("failed at cycle " + str(cycle))
            
    cycle += 1
