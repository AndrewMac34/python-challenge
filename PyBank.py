# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module
TotalMoney = []
MonthsTotal = []
MonthChange = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Total = 0
    Counting = 0
    
    
    # Read each row of data after the header
    month = 0
    for row in csvreader:
        #TotalMoney.append(int(row[1]))
        Total += int(row[1])
        TotalMoney.append(row[1])
        MonthsTotal.append((row[0]))
        month += 1
    print(Total)
        #print(f"The Months Total is {Counting}")
    print(len(MonthsTotal))
    #print(TotalMoney)
    GreatInc = TotalMoney[0]
    GreatDec = TotalMoney[0]
    
    for i in range(len(TotalMoney)-1):
        MonthChange.append(int(TotalMoney[i+1]) - int(TotalMoney[i]))
    GreatInc = max(MonthChange)
    GreatDec = min(MonthChange)
    LargestMonth = MonthsTotal[MonthChange.index(GreatInc)+1]
    SmallestMonth = MonthsTotal[MonthChange.index(GreatDec)+1]
        
    print(GreatInc)
    print(GreatDec)
    print(LargestMonth)
    print(SmallestMonth)

    print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(MonthsTotal)}")
print(f"Total: ${Total}")
print(f"Average Change: {round(sum(MonthChange)/len(MonthChange),2)}")
print(f"Greatest Increase in Profits: {LargestMonth} (${(str(GreatInc))})")
print(f"Greatest Decrease in Profits: {SmallestMonth} (${(str(GreatDec))})")

# Output files

output_file = os.path.join( ".", "Resources", "Homework3 Text Files", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(MonthsTotal)}")
    file.write("\n")
    file.write(f"Total: ${Total}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(MonthChange)/len(MonthChange),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {LargestMonth} (${(str(GreatInc))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {SmallestMonth} (${(str(GreatDec))})")


     
               


    
    
    
    

        
        
    
