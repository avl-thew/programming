#include <stdio.h>
#include <math.h>
#include "gnuplot_i.h" 

int main()
{
    double x, y, h;
    x = 0.0;
    scanf("%lf", &h);
    int n;
    n = 2 / h + 1;

    // Инициализируем gnuplot
    gnuplot_ctrl *gc = gnuplot_init();

    // Устанавливаем параметры графика
    gnuplot_cmd(gc, "set xrange [0:2]");
    gnuplot_cmd(gc, "set yrange [-1:1]");
    gnuplot_cmd(gc, "set title 'График функции'");
    gnuplot_cmd(gc, "set xlabel 'x'");
    gnuplot_cmd(gc, "set ylabel 'y'");

    // Создаем файл для анимации
    gnuplot_cmd(gc, "set term gif animate");
    gnuplot_cmd(gc, "set output 'animation.gif'");

    // Цикл для построения графика и анимации
    while (n)
    {
        if (x >= 0 && x <= 1)
            y = cos(x) * exp(-(x * x));
        else if (x > 1 && x <= 2)
            y = log(x + 1) - sqrt(4 - x * x);

        // Отправляем точку на график
        gnuplot_plot_xy(gc, x, y, "");

        // Задержка для анимации
        gnuplot_cmd(gc, "pause 0.1");

        x += h;
        n--;
    }

    // Закрываем gnuplot
    gnuplot_close(gc);

    return 0;
}
