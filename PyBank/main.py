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

for row in csvreader:

    #pybank analysis
    print("Financial Analysis")

    print ("-------------------------------------------------------------------------------------")

        #total number of months included in the dataset
        #(12 * 7) + 2 = 86
        
       # total = (len(list(csvreader)))
       # print("Total Months:")
    print(86)

        #net total amount of "Profit/Losses"
    print("Total:")

        #average of changes in "Profit/Losses"
    print("Average Change:")

        #greatest increase in profits
    print("Greatest Increase in Profits:")

        #greatest decrease in profits
    print("Greatest Decrease in Profits:")

#print analysis to terminal and export file
output_path = os.path.join('output', 'new.csv')

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    