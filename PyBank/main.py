# First we'll import the os module
import os
# Module for reading CSV files
import csv
# import stadistics functions
import statistics

csvpath = os.path.join('Resources', 'budget_data.csv')

#function to calculate average in a list
def average(list):
    ave_result= statistics.mean(list) 
    return ave_result

#function to search for date in the file
def search_date (amount):
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        # Read the header row first
        csv_header = next(csvreader)
        for row in csvreader:
            if float(row[1]) == amount:
                date =row[0]
                break
    return date
    
# reading the csv file and saving values to calculate results
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(csvreader)
    #initial Variables
    month=0
    total_proloss=0.00
    list_proloss=[]
    new_data=[]
    # Read each row of data after the header
    for row in csvreader:
        month=month+1
        proloss=float(row[1])
        total_proloss=total_proloss+proloss
        list_proloss.append(proloss)
        
# look for the profit/losses change to create a list of change values
pfchange=[]
i=0
len=len(list_proloss)
for i in range(len-1):
        if float(list_proloss[i]) != float(list_proloss[i+1]):
            change=float(list_proloss[i+1])-float(list_proloss[i])
            pfchange.append(change)

#calculating 
ave_value= average(pfchange)
max_value=max(list_proloss)
date1=search_date(max_value)
min_value=min(list_proloss)
date2=search_date(min_value)

#print usings values
#print("                   Financial Analysis                ")
#print("_____________________________________________________")
#print (f"Total Month:  {month}")
#print (f"Total Profit & Losses:  {total_proloss}")
#print (f"Average Profit & Losses:  {ave_value}")
#print (f"Greatest Increase in Profits:  {max_value} {date1}")
#print (f"Greatest Decrease in Profits:  {min_value} {date2}")
#print("______________________________________________________")


#create a file .txt and saved all the Financial Analysis results
filepath = os.path.join("output","financial_analysis.txt")
_, filename = os.path.split(filepath)
file = open(filepath, "w")
file.write("                  Financial Analysis                 " + "\n")
file.write("-----------------------------------------------------" + "\n")
file.write("Total Month: "  + str(month) + "\n")
file.write("Total Profit & Losses: " + str(total_proloss) + "\n")
file.write("Average Profit & Losses: " + str(ave_value) + "\n")
file.write("Greatest Increase in Profits: "  + str(max_value) + " " + str(date1) + "\n")
file.write("Greatest Decrease in Profits: "  + str(min_value) + " " + str(date2) + "\n")
file.write("-----------------------------------------------------" + os.linesep)
file.close()

#Print using the file .txt created
print()
file = open(filepath, "r")
linesFile = file.readlines()
for line in linesFile:
    print (line)
file.close