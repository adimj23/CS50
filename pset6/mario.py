
import cs50
import sys

def mario():

    print("Enter pyramid height(between 0 and 23):", end=' ')
    x=cs50.get_int()
        
    bool1=False
    if x<0 or x>23:
        bool1=True
    
    while bool1==True:
        print("Enter pyramid height(between 0 and 23):", end=' ')
        x=cs50.get_int()
        if x>=0 and x<=23:
            break
    
    
    i=0
    j=0
    y=0
    
    if x>=0 and x<=23:

        for i in range(x):
        
            for j in range(x-i-1):
                print(" ", end='')
            for y in range(i+2):
                print("#", end='')
            print("")
            
        
        
if __name__ == "__main__":
    mario()