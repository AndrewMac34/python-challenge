# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module
TotalMoney = []
MonthsTotal = []
d = []
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Total = 0
    Counting = 0
    AvgChange = 0
    # Read each row of data after the header
    for row in csvreader:
        #TotalMoney.append(int(row[1]))
        Total += int(row[1])
        TotalMoney.append(row[1])
        MonthsTotal.append((row[0]))
        AvgChange += float(row[1])-float(row[1])
    print(Total)
        #print(f"The Months Total is {Counting}")
    print(len(MonthsTotal))
    print(AvgChange)
    #print((TotalMoney))


    
    
    
    

        
        
    
