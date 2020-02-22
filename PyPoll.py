# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
from collections import defaultdict
from collections import Counter

csvpath = os.path.join('.', 'Resources', 'election_data.csv')

VoteID = []
County = []
Candidates = []



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
        Candidates.append((row[2]))
        #Total += int(row[0])
        County.append(row[1])
        VoteID.append((row[0]))
        month += 1
    X = Counter(Candidates)
    
    A = X["Khan"]
    B = X["Correy"]
    C = X["Li"]
    D = X["O'Tooley"]

    KahnPerc = A/len(VoteID) * 100
    CorreyPerc = B/len(VoteID) * 100
    LiPerc = C/len(VoteID) * 100
    OTooleyPerc = D/len(VoteID) * 100
    Maximum = max(A,B,C,D)
    
    print(Maximum)
    
    
    #VotingTable = {csv_header[0]: VoteID,
                  # csv_header[1]: County,
                   #csv_header[2]: Candidates,    
    #}
    
    print(len(VoteID))
    
   
        
    
        
   

    print("Election Analysis")
print("----------------------------")
print(f"Total Votes: {len(VoteID)}")
print("----------------------------")
print(f"Khan: {round(KahnPerc,3)}% ({(str(A))})")
print(f"Correy: {round(CorreyPerc,3)}% ({(str(B))})")
print(f"Li: {round(LiPerc,3)}% ({(str(C))})")
print(f"O'Tooley: {round(OTooleyPerc,3)}% ({(str(D))})")
print("----------------------------")
print(f"Winner: Kahn")
print("----------------------------")


# Output files

output_file = os.path.join( ".", "Resources", "Homework3 Text Files", "Election_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Election Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(VoteID)}")
    file.write("\n")
    
    file.write("\n")
    file.write(f"Kahn: {round(KahnPerc,3)}% ({(str(A))})")
    file.write("\n")
    file.write(f"Correy: {round(CorreyPerc,3)}% ({(str(B))})")
    file.write("\n")
    file.write(f"Li: {round(LiPerc,3)}% ({(str(C))})")
    file.write("\n")
    file.write(f"O'Tooley: {round(OTooleyPerc,3)}% ({(str(D))})")
    file.write("\n")
    file.write(f"Winner: Kahn")
    