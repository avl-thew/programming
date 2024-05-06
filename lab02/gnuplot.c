#include <stdio.h>
#include <stdlib.h>

totalTime = 10.0

int main() {
    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
    if (!gnuplotPipe) {
        fprintf(stderr, "Не удалось запустить gnuplot\n");
        return 1;
    }

    fprintf(gnuplotPipe, "set terminal gif animate delay 100\n");
    fprintf(gnuplotPipe, "set output 'animation2.gif'\n");
    fprintf(gnuplotPipe, "set xrange [0:2]\n");
    fprintf(gnuplotPipe, "set yrange [-1:1]\n");

    for (double x = 0.0; x <= 2.0; x += 0.1) {
        fprintf(gnuplotPipe, "plot cos(x) * exp(-x**2) title 'cos(x) * exp(-x^2)' with lines, \\\n");
        fprintf(gnuplotPipe, "log(x + 1) - sqrt(4 - x**2) title 'log(x + 1) - sqrt(4 - x^2)' with lines\n");
        fprintf(gnuplotPipe, "pause 0.1\n"); 
    }

    
    fprintf(gnuplotPipe, "exit\n");
    pclose(gnuplotPipe);

    return 0;
}
set output