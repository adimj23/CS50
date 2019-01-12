import cs50
import sys

j=0
n=0
h=0
g=0
if len(sys.argv)!=2: 
    print("Please input 1 command line argument.")

else:
    
    k= str(sys.argv[1])
    for h in range(len(k)):
        if str.isalpha(k[h])==False:
            print("Command line arguments may only contain alphabetical characters.")
            exit(1)
    print("plaintext: ")
    x= cs50.get_string()
    print("ciphertext: ")
    i= 0
    for j in range(len(x)):
    
        if str.isalpha(x[j])==False:
            print(x[j], end="")
    
        else:
            if str.isalpha(k[i])==False:
                print("Please enter a string in the command line.")
                exit(1)
        
            else:
                if (str.isupper(x[j]) and ord(x[j])+ord(str.upper(k[i]))-65<=ord('Z')) or (str.islower(x[j]) and ord(x[j])+ord(str.upper(k[i]))-65<=ord('z')):
                    c=ord(x[j])+ord(str.upper(k[i]))-65
                    c=str(chr(c))
                    print(c, end="")
            
                elif str.islower(x[j]):
                    qe=(ord(x[j])-97+ord(str.upper(k[i]))-65)%26+97
                    qe=str(chr(qe))
                    print(qe, end="")
                elif str.isupper(x[j]):
                    upp=(ord(x[j])-65+ord(str.upper(k[i]))-65)%26+65
                    upp=str(chr(upp))
                    print(upp, end="")
                w= len(k)
                if (i>w-2):
                    i=0
                else:
                    i=i+1
                
                #print(x[j], end="")
            
print("")