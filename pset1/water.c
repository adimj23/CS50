#include <stdio.h>
#include <cs50.h>
int main(void)
{
    
    
    printf("How long is your shower in minutes?\n");
     int magic_number = GetInt();
    printf("You use %i bottles of water everytime you shower\n", magic_number * 12 );
}