#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(void)
{
    printf("How much change do I owe you? Please enter in dollars.(No negative numbers)\n");
    float x = GetFloat()*100;
    if (x < 0)
    {
        do
        {
            printf("How much change do I owe you? Please enter in dollars.(No negative numbers)\n");
            x = GetFloat();
        }
        while (x < 0);
    }
    int quarter=0;
    int dime=0;
    int nickel=0;
    int penny=0;
    
     while (x>=25) {
        x=x-25;
        quarter++;
        x = roundf(x*100)/100;
        
    }
    
    while (x>=10 ) {
        x=x-10;
        dime++;

        
    }
    while (x>=5) {
        x=x-5;
        nickel++;
        
    }
    while (x>=1) {
        x=x-1;
        penny++;
        
    
    }

    printf("%i\n", quarter+dime+nickel+penny);
}