#include <stdio.h>
#include <math.h>

int main()

{
    int a,b,c,x = -1;
    float res;
    
    FILE * nfile;
    

    
    while((a != 0) || (c != 0) || (b != 0) || (x != 0))
    {
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

            else if (a%7 != 0 && a <=x)
            {
                res = (float) a/(b+c);
                printf("%f\n" , res );
            }
               
            if (x<a)
                printf("no!\n");
            
    
        }
    
        if (a>b && b>c)
        {
            
            if (c<=x && c%7==0 )
                printf("%d\n", c);
            else if (c%7 != 0 && c <=x)
            {
                res = (float) c/(b+a);
                printf("%f\n" , res );
            }
                
            if (x<c)
                printf("no!\n");
            
        }
    
        if (b<a && a<c)
        {
            
            if (b<=x && b%7==0)
                printf("%d\n" , b);
            else if(b%7 != 0 && b <=x)
            {
                res = (float) b/(a+c);
                printf("%f\n" , res );
            }
                
            if (x<b)
                printf( "no!\n");
            
        }
        nfile = fopen("log.txt", "w+");
        fprintf(nfile, "-------\n");
        fprintf(nfile, "%d\n", a);
        fprintf(nfile, "%d\n", b);
        fprintf(nfile, "%d\n", c);
        fprintf(nfile, "%d\n", x);
        fprintf(nfile, "%f\n", res);
        
        fclose(nfile);

   
    }
   
    return 0;
}  