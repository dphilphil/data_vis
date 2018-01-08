#!/bin/bash

infile="31550.dat"
#lines in each timestep
lines_per_step=506

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
  end_line=$((i*506))
 
  #
  #lines to get
  l1=$pre$((end_line-303))$comma
  l3=$((end_line-254))$suffix
  #
  
  list_of_lines+="$l1$l3"
done

list_of_lines+="  $infile >> HonTop.dat"

#execute generated string
eval $list_of_lines
