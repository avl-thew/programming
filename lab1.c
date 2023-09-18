#include <stdio.h>
#include <math.h>

int main()
{
    int a,b,c,x;
    printf("Enter a -> ");
    scanf("%d", &a);
    printf("Enter b -> ");
    scanf("%d", &b);
    printf("Enter c -> ");
    scanf("%d", &c);
    printf("Enter x -> ");
    scanf("%d", &x);

    
    
    if (a<b && b<c)
    {
        if (a<=x && a%7==0)
            printf("%d\n", a);
        else
            printf("%d\n" , a/b+c );

    }

    if (a>b && b>c)
    {
        if (c<=x && c%7==0 )
            printf("%d\n", c);
        else
            printf("%d\n" , c/b+a);
    }

    if (b<a && a<c)
    {
        if (b<=x && b%7==0)
            printf("%d\n" , b);
        else
            printf("%d\n" , b/a+c);
    }
    return 0;
}



    





