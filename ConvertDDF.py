#! usr/bin/env python

import re
import sys
import os 
import csv

Usage = """
ConvertDDF.py -- version 1.0
Convert .ddf files into data format that can be run through Mus.Phys. R scripts
Run through entire directory of .ddf files, put important info into .csv
Thank you for playing. 
Usage: *.ddf > *.csv
"""

input_file_path = os.path.join(sys.argv[1])        # Read in the first argument from the bash wrapper
input_file = open(input_file_path,'r')             # Open the file for reading

filename = os.path.basename(input_file_path)       # Get the filename
filename = filename.strip(".ddf")                  # Modify filename: Get rid of .ddf extension

output_folder_path = os.path.join('CleanDDF',filename+'.csv') # Set output file pathway to CleanDDF directory 
output_file = open(output_folder_path, 'w')                   # Open output file
writer = csv.DictWriter(output_file, fieldnames=["TimeStamp", "Force (g)", "Position (mm)", "Stimulus"]) # Assings headers for each column in output file
writer.writeheader()								#writes header



#creates counter variable, RE=regular expression
RE1 = 0
Calibrator = ()
LineNumber = 0


#for loop to go through line by line, find calibration, take important information and put in output file
for line in input_file:
	if "Scale" in line:
		match_RE1 = re.match('Scale\s+\S+\s+\S+\s+(\d*\.\d+)', line) #match the RE1 regular expression
		Calibrator= match_RE1.group(1)


	if LineNumber > 22:
		line = line.strip('\n') #remove extra line ending
		ElementList = line.split('\t') #turns each row into a list- taking each element of the list that is separated by tabs
		Time = int(ElementList[0])
		TimeStamp = (Time * 0.001)
		Force = ((float(ElementList[2]) * float(Calibrator))/9.81)
		Position = float(ElementList[1])
		Stimulus = float(ElementList[11])
		
		OutputString = " %f,%f,%f,%f" % (TimeStamp, Force, Position, Stimulus)

		output_file.write(OutputString + "\n")

	LineNumber = LineNumber + 1


input_file.close() 
output_file.close()









