#include<stdio.h>

int main()
{
    int i ;
    
    printf("ENTER A NUMBER:");
    scanf("\t%d",&a);
        printf("FACTOR OF %d:",a);
        for(i=1;i<=a;i++)
    {
        if(a%i==0);
         {

         printf("\t%d",i);
        }
        

    }
    return 0;
}