#!/bin/sh

#bash script that will run ConvertDDF.py in all .ddf files in a directory
#on command line type in bash ConvertDDFBash.sh *.ddf

for datafile in "$@"
do
   python ConvertDDF.py $datafile
done
