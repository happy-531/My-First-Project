#include <stdio.h>

int main(){
int a;
int b;
int c;

printf("Enter first number : ");
scanf("%d", &a );

printf("Enter second number : ");
scanf("%d",&b);

printf("Select what you want :\n \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.division :\n =>");
scanf("%d",&c);

if (c==2){
    if(a>b)
    {
    printf("Result : %d \n",a-b);
    }
    if(a<b){
        printf("Result : %d \n",b-a);
    }
}
if (c==1){
printf("Result : %d \n",a+b);
}
if (c==3){
    printf("Result : %d \n",a*b);
}
if (c==4){
    if (b!=0)
    {
    float s = (float)a/b;
    printf("Result : %.3f \n",s);
    }
    else{
        printf("you can't divide with 0 \n");
    }
}
return 0;
}
