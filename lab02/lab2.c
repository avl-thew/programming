// #include <stdio.h>
// #include <math.h>


// int main()
// {   
    
//     double x, y, h;
    
    
//     x = 0.0;
 
//     scanf("%lf", &h);
//     int n;
//     n = 2 / h + 1;

//     while (n)
   
//     {
//         if (x >= 0 && x <= 1)
        
//             y = cos(x) * exp(-(x * x));
             
//         if (x > 1 && x <= 2)
        
//             y = log(x + 1) - sqrt(4 - x * x);
        
//         printf("%f %f\n", x, y);
//         x += h;
//         n = n - 1;
        
//     }
    
// }


#include <stdio.h>
#include <math.h>

int main()
{   
    double x, y, h;
    x = 0.0;
    
    scanf("%lf", &h);
    int n;
    n = 2 / h + 1;

    // Создание временного файла для хранения данных анимации
    FILE *tempfile = fopen("temp_data.txt", "w");

    while (n)
    {
        if (x >= 0 && x <= 1)       
            y = cos(x) * exp(-(x * x));            
        if (x > 1 && x <= 2)       
            y = log(x + 1) - sqrt(4 - x * x);

        fprintf(tempfile, "%f %f\n", x, y); // Запись во временный файл
        x += h;
        n = n - 1;
    }

    fclose(tempfile);

    // Создание и сохранение анимированного графика
    FILE *gnuplotPipe = popen("gnuplot -persist", "w");
    fprintf(gnuplotPipe, "set term gif animate delay 10\n");
    fprintf(gnuplotPipe, "set output 'animated_plot.gif'\n");
    fprintf(gnuplotPipe, "plot 'temp_data.txt' with lines\n"); // График будет построен линиями
    fclose(gnuplotPipe);

    return 0;
}    