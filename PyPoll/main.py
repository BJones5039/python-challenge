#Module
import os

#read csv
import csv

#set path for file
csvpath = os.path.join('Resources', 'election_data.csv')

#open the csv
with open(csvpath) as csvfile:

    # csv reader specifies delimeter and variable 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #read the header row
    csv_header = next(csvreader)