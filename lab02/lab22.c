#include <stdio.h>
#include <math.h>


int main()
{   
    
    double x, y, h;
    x = 0.0;
    scanf("%lf", &h);
    int n, i;
    n = 2 / h ;

    for(i =0; i <= n; i++)
    {
      if (x >= 0 && x <= 1)
          y = cos(x) * exp(-(x * x));
      if (x>1 && x <= 2)
          y = log(x + 1) - sqrt(4 - x * x);
      printf("%lf %lf\n", x, y);
      x += h;
    
    }
}


