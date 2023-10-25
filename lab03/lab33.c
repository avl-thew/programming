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
}

int main()
{
    srand(time(NULL));
    

    int n, imax1, imax2, imax3;
    printf("n -> ");
    scanf("%d", &n);
    int arr[n];
    fill(n,arr);
    double index;

    
    
    
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
    printt(n, arr);
    printf("\n");
    int sum = max1 + max2 + max3;
    int product = max1 * max2 * max3;
    index = ( imax1 + imax2 + imax3 ) % n;
    printf("%d\n max1 = ", max1);
    printf("%d\n max2 = ", max2);
    printf("%d\n max3 = ", max3);
    printf("%d\n imax1 = ", imax1);
    printf("%d\n imax2 = ", imax2);
    printf("%d\n imax3 = ", imax3);

    printf("%d\n product - sum = ", product - sum);

    printf("%f\n index = ", index);
    printf("arr = ");
    printt(n, arr);
    printf("\n");
    return 0;
}