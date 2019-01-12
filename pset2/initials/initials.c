#include <stdio.h>
#include <cs50.h>
#include <string.h>
int main(void)
{

    string s = get_string();
    int i=0;


     if (s[0]>='A' && s[0] <='Z') {
        printf("%c",s[0]);}

        else {
                char first_letter=s[0];
                char first_caps= 'A'+first_letter-'a';
                printf("%c",first_caps);

        }
    for (i=0; i<strlen(s); i++) {
         if (s[i]== ' ') {

            if (s[i+1]>='A' && s[i+1] <='Z' ) {
                char initials= s[i+1];
                printf("%c", initials);
            }
            else {
                char initial_1= s[i+1];
                char upper= 'A' +initial_1-'a';
                printf("%c",upper);
            }
        }



    }
    printf("\n");
}