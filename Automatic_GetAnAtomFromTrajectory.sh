in='XX.xyz'

outp_preffix='H500_'

#504 is total number of lines in file. 502+2
lines_per_step=504

#idx of atom to get
atom_no=502

####################################


#add header lines
atom_no=$((atom_no +2))

echo $atom_no

#generate string of \n to append to top of file
blank_line=''


#atom count
atom_no=$((lines_per_step - atom_no))

#if statement due to failure of awk to correctly add a single \n when atom_no=1. Otherwise awk  incorrectly adds \n\n

if [ "$atom_no" != "1" ]
then
  for ((i=1; i<atom_no; i++))
  do
    blank_lines+='\n'
  done
else
  blank_lines+='\'
fi

#tempfile name
tempf=$in'.tempf'

#make temp file with added blank lines
sed '1i\'$blank_lines $in >> $tempf

#SEARCH for atoms
awk 'NR % 504 == 0' $tempf >> $outp_preffix$in

#remove temporary file
rm $tempf
