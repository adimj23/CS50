import cs50
import sys

if len(sys.argv)!=2:
    print("Please input integer in command line.")
    
    
else:
    k =int(sys.argv[1])
    while True:
        print("Please input a non-negative integer in command line.")
        if k>=0 and str.isdigit(sys.argv[1]):
            break
        
    print("plaintext: ", end="")
    x= cs50.get_string()
    print("ciphertext: ", end="")
    for i in range(len(x)):
        if (str.isalpha(x[i])):
            if (str.isupper(x[i])):
                if ord(x[i])+k<=ord('Z'):
                    y= ord(x[i])+k
                    #str(chr()) converts int to char with corresponding ASCII value Ref:https://stackoverflow.com/questions/3673428/convert-int-to-ascii-and-back-in-python
                    y=str(chr(y))
                    print(y, end="")
                
                else:
                    yupper = (((ord(x[i]))-65+k)%26)+65
                    yupper=str(chr(yupper))
                    print(yupper, end="")
            
    
    
            elif(str.islower(x[i])):
                if ord(x[i])+k<=ord('z'):
                    ylower= ord(x[i])+k
                    ylower=str(chr(ylower))
                    print(ylower, end="")
                
            
                else: 
                    ylower2 = ((ord(x[i])-97+k)%26)+97
                    ylower2 = str(chr(ylower2))
                    print(ylower2, end="")
            
    
        else: 
            print(x[i], end="")
    
    

print("\n")
    
   
 
 