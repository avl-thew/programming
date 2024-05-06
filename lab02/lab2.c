#include <stdio.h>
#include <math.h>


int main()
{   
    
    double x, y, h;
    
    
    x = 0.0;
 
    scanf("%lf", &h);
    int n;
    n = 2 / h + 1;

    while (n)
   
    {
        if (x >= 0 && x <= 1)
        
            y = cos(x) * exp(-(x * x));
             
        if (x > 1 && x <= 2)
        
            y = log(x + 1) - sqrt(4 - x * x);
        
        printf("%f %f\n", x, y);
        x += h;
        n = n - 1;
        
    }
    
}
