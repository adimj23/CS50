#include <stdio.h>
#include <cs50.h>
int main(void)
{   
    int i =0;
    
    
    printf("Enter pyramid height(between 0 and 23):\n");
    int x = GetInt();
        while ((x > 23) || (x < 0)) {
         printf("Enter pyramid height(between 0 and 23):\n");
            x = GetInt();
        }
        
    
    
    if (x>=0 && x<=23) {
    while (i<=x) {
        
    for (i=1;i<=x;i++) {
        for (int j=1;j<=(x-i);j++) {
            printf(" ");
        }
            for (int y=1; y<= i+1; y++) {
                printf("#");
            }
            printf("\n");
    }
    } 
} else { printf("Enter pyramid height(between 0 and 23):\n");
            x = GetInt();
    do {
        
    for (i=1;i<=x;i++) {
        for (int j=1;j<=(x-i);j++) {
            printf(" ");
        }
            for (int y=1; y<= i+1; y++) {
                printf("#");
            }
            printf("\n");
    }
    } while (i<=x);
}
}