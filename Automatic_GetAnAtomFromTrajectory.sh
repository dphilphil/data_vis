in='XX.xyz'
#504 is total number of lines in file. 502+2
lines_per_step=504

#idx of atom to get
atom_no=238
outp_preffix='H238_'

###

#add header lines
atom_no=$((atom_no +2))

#generate string of \n to append to top of file
blank_lines=''

#atom count
atom_no=$((lines_per_step - atom_no))

for ((i=1; i<atom_no; i++))
do
  blank_lines+='\n'
done

#tempfile name
tempf=$in'.tempf'

#make temp file with added blank lines
sed '1i\'$blank_lines $in >> $tempf

#SEARCH for atoms
awk 'NR % 504 == 0' $tempf >> $outp_preffix$in

#remove temporary file
rm $tempf
