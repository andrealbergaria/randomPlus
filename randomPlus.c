/*
 * random.c

 */


#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void printArray(char listOfDigits[],int sizeOfDigitsList) {
	printf("\n[ ");
	for (int i =0 ;  i < sizeOfDigitsList; i++) {
		printf(" %x ",listOfDigits[i]);
	}
	printf("] \n");
}

u_char *getRandom(int numberOfDigits) {


	char *arrayOfDigits = (u_char *) malloc(numberOfDigits);


	int fdRandom = -1;

	fdRandom = open("/dev/random",O_RDONLY);

	if (fdRandom < 0 ) {
		printf("\nERROR FILE descriptor");
		exit(-1);
	}


	u_char buf = 0;
	int returnRead = 0;

	//Better than just srand(time(NULL))
	//
	char firstPart;
	char secondPart;



	for (int i=0; i < numberOfDigits; i++) {
		while (1) {
			returnRead = read(fdRandom,&buf,1);

			if (returnRead < 0 ) {
				printf("\nread() function didnt read all bytes required");
				exit(-1);
			}


			firstPart = buf & 0b00001111;
			secondPart = buf & 0b11110000;

			secondPart >>= 4;

			if (firstPart <= 9 && firstPart >= 0) {
				arrayOfDigits[i] = firstPart;
				if ( (i+1) < numberOfDigits) {
					if (secondPart <= 9 && secondPart >=0)
						arrayOfDigits[i+1] = secondPart;

				}
				break;
			}



		}



	}

	close(fdRandom);
	return arrayOfDigits;
}

int main(void)
{
	for (int i=0; i < 10 ; i++) {
		u_char *arrayOfDigits = getRandom(10);
		printArray(arrayOfDigits,10);
		free(arrayOfDigits);
	}
	return 0;
}

