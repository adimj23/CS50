/**
 * Implements a dictionary's functionality.
 */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>


#include "dictionary.h"
#define hashsize 65631
typedef struct node
{
    char word[LENGTH + 1]; // LENGTH is 45
    struct node* next;
}
node; 

    /**
 * Hash function via reddit user delipity:
 * https://www.reddit.com/r/cs50/comments/1x6vc8/pset6_trie_vs_hashtable/cf9nlkn
 */
int hash_it(char* needs_hashing)
{
    unsigned int hash = 0;
    for (int i=0, n=strlen(needs_hashing); i<n; i++)
        hash = (hash << 2) ^ needs_hashing[i];
    return hash % hashsize;
}

node *hashtable[hashsize];
/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    int length= strlen(word);
    char word1[length+1];
    for(int z=0;z<length;z++) {
        word1[z]=tolower(word[z]);
        
    }
    word1[length]='\0';
    
    int hashed=hash_it(word1)%hashsize;
    
    if(hashtable[hashed]==NULL) {
        
        return false;
    }
    
    node *cursor=hashtable[hashed];
    
    while(cursor!=NULL) {
    
    if (strcmp(cursor->word, word1) == 0) {
        
        return true;
    }
    
    
    cursor=cursor->next;
}
    
    return false;
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
int word_counter=0;
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    //char word[LENGTH +1];
    if (dict== NULL) {
        printf("Could not load dictionary.");
        return false;
    }
    
    while(feof(dict)==0) {
        
        word_counter++;
        node *node1=malloc(sizeof(node));
        if(node1==NULL) {
            unload();
            return false;
        }
        fscanf(dict, "%s", node1->word);
        unsigned int hashed=hash_it(node1->word);
        //first spot is available
        if (hashtable[hashed]==NULL) {
            
            hashtable[hashed]=node1;
            node1->next=NULL;
        }
        
        else {
            node1->next=hashtable[hashed];
            hashtable[hashed]=node1;
        
        }
        
    }
    fclose(dict);
    return true;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    if(word_counter>0) {
        return word_counter-1;
    }
    else {
        return 0;
    }
    return true;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
 
bool unload(void)
{
    int index=0;
    while(index<hashsize) {
        if(hashtable[index]==NULL) {
        
            index++;
        
        }
    
        else {
         
           while (hashtable[index]!=NULL)  {
        
            node *temp = hashtable[index];
            hashtable[index]=temp->next;
            free(temp);
        
            }
        index++;
        }
    }
return true;
}