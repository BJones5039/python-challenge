#Module
import os

#read csv
import csv

#set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#open the csv
with open(csvpath) as csvfile:

    # csv reader specifies delimeter and variable 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #read the header row
    csv_header = next(csvreader)

#pybank analysis
print("Financial Analysis")

print ("-------------------------------------------------------------------------------------")

#total number of months included in the dataset

#net total amount of "Profit/Losses"

#average of changes in "Profit/Losses"

#greatest increase in profits

#greatest decrease in profits

#print analysis to terminal and export file