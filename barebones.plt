#!/usr/bin/gnuplot

set xlabel 'k-points'
set ylabel 'energy (eV)'
set title 'SPE k-point convergence'
set timestamp
set style line 1 lt -1 lw 1 pt 7 ps 1
plot 'energies.log' with linespoints ls 1
set terminal pngcairo
set output "out.png"
replot
quit


