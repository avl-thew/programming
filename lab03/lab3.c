#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)

{   
    
     
    int M [100];
    int n;
    scanf("%d", &n);
    for ( int i = 0; i < n; i = i + 1 )

    scanf("%d", &M [i] );


    {
        int imax1 = 0;
        
        for (i = 1; i < n; i++)
            if ( M [i] > M[imax1] )
                imax1 = i;
        
        int imax2 = 0;

        for (i = 1; i < n; i++)
            if ( M [i] > M[imax2] )
                imax2 = i;
        
        int imax3 = 0;

        for (i = 1; i < n; i++)
            if ( M [i] > M[imax3] )
                imax3 = i;

        int ipro = imax1 * imax2 * imax3;
        int isum = abs( imax1 + imax2 + imax3 );
        int irac = ipro - isum;

    }
    printf("\n");
  return 0;
}