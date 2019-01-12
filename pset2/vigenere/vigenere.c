#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(int argc, string argv[])
{
    int j;
    int n;
    int h;
    int g;
if (argc !=2) {
    printf("Please input 1 command line argument.");
    return 1;
}
else {

    string k= argv[1];
    for (h = 0, g=strlen(k); h<g; h++) {
       if (!isalpha(k[h])) {
           printf("Command line arguments may only contain alphabetical characters.");
            return 1;
        }

    }
    printf("plaintext: ");
    string x= get_string();
    printf("ciphertext: ");
int i= 0;
for (j = 0, n=strlen(x); j<n; j++) {

    if (!isalpha(x[j])) {
        printf("%c", x[j]);
    }

    else {
        if (!isalpha(k[i])) {
            return 1;
        }
        else {
            if ((isupper(x[j]) && x[j]+toupper(k[i])-65<='Z') || (islower(x[j]) && x[j]+toupper(k[i])-65<='z')) {
                x[j]=x[j]+toupper(k[i])-65;
            }

            else if (islower(x[j])) {

                //original code x[j]=(x[j]-97+x[j]+toupper(k[i])-97)%26+97;
                x[j]=(x[j]-97 + toupper(k[i])-65)%26+97;
            }

            else if (isupper(x[j])) {

                // original code x[j]=(x[j]-65+ x[j] +toupper(k[i])-65)%26+65;
                x[j]=(x[j]-65+ +toupper(k[i])-65)%26+65;
              //  printf("in z test loop");
            }

        int w= strlen(k);
        if (i>w-2) {
            i=0;
        }
        else {
            i++;
        }
        printf("%c", x[j]);
        }
    }

}
printf("\n");
return 0;

}
}


