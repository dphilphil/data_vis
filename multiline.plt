#!/usr/bin/gnuplot

set title 'Pseudopotential Cutoff Energy Convergence'
set xlabel 'Cutoff Energy (eV)'
set ylabel 'Force on H1x (eV/A)'
set style line 1 lt -1 lw 1 pt 7 ps 1
set style line 2 lt -1 lw 1 pt 5 ps 1

set datafile separator whitespace	#most important

set term svg enhanced mouse size 600,400
set output "out.svg"

plot 'x.dat' using 1:2 title 'Qc5' with linespoints ls 1, 'x.dat' using 1:3 title 'Ultrasoft' with linespoints ls 2
quit #must always quit to generate .svg, otherwise the image is not generated correctly
