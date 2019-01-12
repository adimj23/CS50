#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
int main(int argc, string argv[])
{
    if (argc!=2) {
        printf("Please input integer in command line.\n");
        return 1;
    }

    else {
        int k =atoi(argv[1]);
        if (k < 0) {
         printf("Please input a non-negative integer in command line.\n");
        return 1;
        }
        printf("plaintext: ");
        string x= get_string();
        printf("ciphertext:");
    for (int i = 0, n = strlen(x); i < n; i++) {

        if (isalpha(x[i])) {
            if (isupper(x[i])) {
                if(x[i]+k<='Z') {
                    char y= x[i]+k;
                    printf("%c", y);
                }
            else {
                //k=(x[i]+k)%26;
                char yupper = ((x[i]-65+k)%26)+65;
                printf("%c", yupper);
            }

    }
        else if(islower(x[i])) {
             if(x[i]+k<='z') {
                char ylower= x[i]+k;
                printf("%c", ylower);

            }
            else {
                char ylower2 = ((x[i]-97+k)%26)+97;
                printf("%c", ylower2);

            }

        }

    }
    else {
        printf("%c",x[i]);
    }
    }
}
  printf("\n");
  return 0;
    }

