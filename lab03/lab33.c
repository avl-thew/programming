#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void fill(int n, int a[])
{
    int i;
    for (i = 0; i < n; i++)
        a[i] = rand() % 10;
}
void printt(int n, int a[])
{
    int i;
    for (i = 0; i < n; i++)
        printf("%6d", a[i]);
    printf("\n");
}

void printff(int n, int arr[])
{
    int imax1, imax2, imax3;
    int max1 = arr[0], max2 = arr[0], max3 = arr[0];
    for (int i = 1; i < n; i++)
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
    
    printf("\n");
    int sum = max1 + max2 + max3;
    int product = max1 * max2 * max3;
    int index = ( imax1 + imax2 + imax3 ) % n;
    printf("max1 = %d\n", max1);
    printf("max2 = %d\n", max2);
    printf("max3 = %d\n", max3);
    printf("imax1 = %d\n", imax1);
    printf("imax2 = %d\n", imax2);
    printf("imax3 = %d\n", imax3);

    printf("product - sum = %d\n", product - sum);

    printf("index = %d\n", index);
    
}

int main()
{
    srand(time(NULL));
    

    int n;
    printf("n -> ");
    scanf("%d", &n);
    int arr[n];
    fill(n,arr);

    printt(n, arr);
    printff(n, arr);
    printf("arr = ");

    printt(n, arr);
    printf("\n");
    
    return 0;
}