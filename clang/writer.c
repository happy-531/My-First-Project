#include <stdio.h>
#include <stdlib.h>

int main(){
	char file1[100] , txt[1000] , cat[100] ;

	printf("Writer is a program written in c language that can be used to create and write in a file.")

	printf("Enter the file name with extension : ");
	scanf(" %s",file1);

	FILE *fptr;

	fptr = fopen(file1,"a");

	if(fptr == NULL){
		printf("\033[1;31m [ERROR]\n \033[0m \n");
		return 1;
	}

	printf("Enter the text you want to write in the file : \n");
	scanf(" %[^\n]s",txt);

	fprintf(fptr,"\n%s\n\n",txt);
	fclose(fptr);

	sprintf(cat,"cat %s",file1);

	printf("\033[1;32m [SUCCESSFULLY SAVED] \033[0m \n \n \033[1;34m Opening the file and showing the content of the file \033[0m \n");

	fflush(stdout);

	system(cat);

	return 0;
}
