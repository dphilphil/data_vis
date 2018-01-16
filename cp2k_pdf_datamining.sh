#!/bin/bash

infile="Md_xx.xyz"
#lines in each timestep
lines_per_step=510

tot_lines=$(wc -l < $infile)
iter=$((tot_lines/lines_per_step))


list_of_lines="time sed -n "
suffix="p'"
comma=","
pre=" -e '"


#using for loop ONLY to generate list of lines to get
for ((i=1; i<=iter; i++))
do
  #end line of each timestep
  end_line=$((i*$lines_per_step))
  
  #ID
  l0=$pre$((end_line-509))$comma
  l1=$((end_line-508))$suffix
 
  #2xNH3
  l2=$pre$((end_line-7))$comma
  l3=$((end_line))$suffix
  #

  
  list_of_lines+="$l0$l1$l2$l3"

done

list_of_lines+="  $infile >> 2xNH3_Md_xx.xyz"

eval $list_of_lines
