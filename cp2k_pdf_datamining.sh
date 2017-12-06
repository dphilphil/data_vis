#!/bin/bash
#Program for use with cp2k *-pos-1.xyz file type

printf "***** WARNING: Input file cannot contain blank lines. Use :g/^$/d in vim to remove them. *****\n"

for (( timesteps=0; timesteps<=3; timesteps++ )) #number of MD step
do
  #H in MH surface
  #506 = 504 atoms + 2lines between each trajectory
  pos1=$(echo "203+($timesteps*506)" | bc )
  pos2=$(echo "$pos1+49")
  awk 'NR=='$pos1',NR=='$pos2'' *-pos-1.xyz >> ' HinSurfaceLayer.dat' 

  #H in ammonia
  pos3=$(echo "503+($timesteps*506)" | bc )
  pos4=$(echo "$pos3+2")
  awk 'NR=='$pos3',NR=='$pos4'' *-pos-1.xyz >> 'HinNH3.dat' 
done
