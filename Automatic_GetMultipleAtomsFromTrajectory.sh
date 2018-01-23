in='.xyz'

no_of_atoms=504
lines_per_step=$((no_of_atoms+2)) #add header

#grab multiple atoms from a single orig. file
for ((atom_incrementer=0; atom_incrementer<50; atom_incrementer++))
do
  #location of first atom w/o header
  atom_loc=201	#USER

  #increment atom loc to cycle through
  atom_loc=$((atom_loc + atom_incrementer))

  #file nameS
  fname='H'$atom_loc'_'$in

  #account for header lines
  atom_loc=$((atom_loc +2))

  #atom count
  atom_loc=$((lines_per_step - atom_loc))

  
  #generate string of \n to append to top of file based on location of atoms
  for ((i=1; i<atom_loc; i++))
  do
    blank_lines+='\n'
  done
  
  #tempfile name
  tempf=$fname'.tempf'

  #make temp file with added blank lines
  sed '1i\'$blank_lines $in >> $tempf

  #SEARCH for atoms
  #use eval to concat. arguments
  eval awk' "NR % '$lines_per_step' == 0" $tempf >> $fname'

  #remove temporary file
  rm $tempf

  #resets each time
  blank_lines=''

done
