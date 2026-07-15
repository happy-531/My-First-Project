#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
char name[50];
char command[100];
char o[100];
int choice;
char d[100];
char rm[100];
char r[100];
char cf[100];
char f[100];
char create[100];
char show[100];

printf("File creator is a program written in c language that creates a folder and then open it then ask you to create, delete and See items in a folder or directory.");

system("cd && ls");

printf("Enter the name of the folder you want to create: ");
scanf(" %s",name);

sprintf(command,"mkdir %s",name);

printf("\033[1;33m creating the folder : %s ... \033[0m \n",name);
fflush(stdout);
sleep(3);

system(command);

printf("\033[1;32m [done] folder created successfully. \033[0m \n");
fflush(stdout);
sleep(1);

printf("opening the folder... \n");
fflush(stdout);
sleep(1);

do{

sprintf(o,"ls -d %s",name);
system(o);

printf("choose the option :\n 1.Delete file\n 2.Create file \n 3.see directory or folders \n 67.Enter 67 to exit.\n =>");
scanf(" %d",&choice);
fflush(stdout);

if (choice == 1){
printf("choose the directory");
fflush(stdout);

system("cd && ls");
printf("Enter the exact name of the directory : ");
scanf(" %s",d);
fflush(stdout);

sprintf(rm,"cd ~/%s && ls",d);

system(rm);

printf("Enter the exact name of file to delete : ");
scanf(" %s",f);
fflush(stdout);

sprintf(r,"rm -rf %s",f);
system(r);
printf("deleted successfully\n");
} else if(choice==2){

printf("choose the directory");
fflush(stdout);

system("ls");
printf("Enter the exact name of the directory : ");
scanf(" %s",d);
fflush(stdout);

printf("Enter the name of file : ");
scanf(" %s",cf);
fflush(stdout);

sprintf(create,"cd ~/%s/ && touch %s && ls",d,cf);
system(create);
sprintf(show,"cd %s && ls",d);
printf("opening the folder and showing the files...\n\n");
fflush(stdout);
system(show);
sleep(4);
} else if (choice==3){
system("cd && ls");
printf("if you want to see the file enter the name of folder or directory to see files inside it : ");
scanf(" %s",d);
fflush(stdout);

sprintf(rm,"cd %s && ls",d);
system(rm);
}

} while(choice!=67);

return 0;
}
