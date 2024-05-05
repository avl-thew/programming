set term gif animate
set output 'animation.gif'

totalTime = 2.0

do for [t=0:100] {
    h = 2.0 / 100.0 * t
    eps = h / 2.0
    
    set xrange [0:2]
    set yrange [-2:2]
    
    set title sprintf("Time: %.2f s", t / 5.0)
    set xlabel "x"
    set ylabel "y"
    
    plot '+' u 1:(x <= 1 + eps ? (cos(x) * exp(-(x * x))) : (log(x + 1) - sqrt(4 - x * x))) w l notitle
    
    pause 0.1
}

set output