#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void fill(int n, int a[])
{
    int i;
    for (i = 0; i < n; i++)
        a[i] = rand () % 101 - 50;
}


int main()
{
    srand(time(NULL));
    

    int n, imax1, imax2, imax3;
    printf("n -> ");
    scanf("%d", &n);

    

    int arr[n];
    for (int i = 0; i < n; i++)

    {
        scanf("%d", &arr[i]);
    
    }
    
    int max1 = arr[0], max2 = arr[0], max3 = arr[0];
    for (int i = 1; i<n; i++)
    {
        if (arr[i] > max1)
        {
            max3 = max2;
            max2 = max1;
            max1 = arr[i];
            imax1 = i;
        }
        else if (arr[i] > max2)
        {
            max3 = max2;
            max2 = arr[i];
            imax2 = i;
        }
        else if (arr[i] > max3)
        {
            max3 = arr[i];
            imax3 = i;
        }
    }
    
    int sum = max1 + max2 + max3;
    int product = max1 * max2 * max3;
    
    
   
    int index = ( imax1 + imax2 + imax3 ) % n;
    
    printf("%d\n", product - sum);

    printf("%d\n", index);
    
    return 0;
}