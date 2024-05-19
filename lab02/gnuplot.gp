set term gif animate
set output 'animation.gif'

totalTime = 10.0

do for [t=0:100] {
    h = 3.0 / 100.0 * t
    eps = h / 2.0
    
    set xrange [0:2]
    set yrange [-1.5:1.5]
    
    set title sprintf("Time: %.2f s", t / 10.0)
    set xlabel "x"
    set ylabel "y"
    
    plot '+' u 1:(x <= 1 + eps ? (cos(x) * exp(-x**2))  : (log(x + 1) - sqrt(4 - x**2))) w l notitle
    
    pause 0.1
}

set output


# sudo apt update
# sudo apt install gnuplot