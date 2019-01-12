/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    if (n>=0) {
        int a=0;
        while (a<n-1) {
            if (value==values[a]) {
                return true;
                a=a+n;
                printf("Found the needle!");
            }
            else if (value==values[n-1]) {
                return true;
                a=a+n;
                printf("Found the needle!");
            }
            else if (a==n-1) {
                return false;
                printf("Didn't find the needle.");
            }
            
            else if  (value!=values[a]) {
                a++;
            }
        }
    }
    else {
    return false;
      printf("Didn't find the needle.");
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    for (int i = 0; i<n-2; i++) {
        if (values[i]>values[i+1]) {
            int g=values[i];
            int j=values[i+1];
            values[i+1]=g;
            values[i]=j;
            
        }   
        
        
        
    }
    return;
}
