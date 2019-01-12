#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char *argv[])
{
	
	if(argc != 2){
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }
	unsigned char buffer[512];
	int counter = 0;
		
		
	FILE* f = fopen(argv[1], "rb");	
	FILE* outptr = NULL;

	if(f == NULL)
		{	
			fclose(f);
			fprintf(stderr, "Cardfile could not be opened.\n");
			return 1;
		}
		
	while (fread(buffer, sizeof(buffer), 1, f) == 1) {
	
	
		if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] == 0xe0 || buffer[3] == 0xe1)) {
			
			if (outptr != NULL) {
				
				fclose(outptr);
				outptr=NULL;
			}
		
			char jpeg[8];
			sprintf(jpeg, "%03d.jpg", counter);
		
			outptr = fopen(jpeg, "wb");
            if (NULL == outptr)
            {
              printf("Could not open %s.\n", jpeg);
              return 1;
            }                     

            fwrite(buffer, sizeof(buffer), 1, outptr);
        	counter++;
		}
		
		else {
				if(NULL!=outptr) {
               fwrite(buffer, sizeof(buffer), 1, outptr);                              
			}
		}
	}
	
			if (outptr!=NULL) {
				fclose(outptr);
			}
				fclose(f);
			
	return 0;
	}
