#!/bin/bash

#find all nitrogens in coordination file
nitrogen=$(grep -E "N" *.xyz)

#separate nitrogens depending on the ammonia they belong to
for (( timesteps=0; timesteps<=100; timesteps++ ))
do
  even=$(echo "($timesteps*2)" | bc )
  odd=$(echo "$even+1")
  
  #find line numbered NR
  #correct way is to include "{ print; exit }" to quit after finding the desired line 
  echo "$nitrogen" | awk 'NR=='$even' { print; exit } ' >> nitrogen1.dat
  echo "$nitrogen" | awk 'NR=='$odd' { print; exit } ' >> nitrogen2.dat
done
