#! /bin/bash
# combines csv files using the header from the first file in the directory

inputdir=timeanddate
outputfile=timeanddate.tsv

counter=0
for file in `ls $inputdir/*.tsv`
do
    if [ $counter = 0 ]
    then
        head -n 1 $file > $outputfile
    fi
    tail -n +2 $file >> $outputfile
    echo >> $outputfile
    let counter=counter+1
done