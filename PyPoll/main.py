#modules
import os
import csv
from pathlib import Path
#set path for polling data file
csvpath = Path(__file__)/"..\Resources/election_data.csv"

#open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #strip off headers
    header = next(csvreader)
    
    #output variables
    elec_results = []

    for row in csvreader:
        #transfer names into a list
        elec_results.append(row[2])
       
    #total number of votes
    vote_count = len(elec_results)

    #sort list so can get names easily
    elec_results.sort() 
    
    name_results = []
    vote_results = []
    name_hold = ""  #initialize with empty string
    vote_tmp = 0
    first = True

    for i in elec_results:
        if name_hold != i:
            name_results.append(i)
            name_hold = i
            if first == False:
                vote_results.append(vote_tmp)
            else:
                first = False
            vote_tmp = 1
        else:
            vote_tmp = vote_tmp + 1

    vote_results.append(vote_tmp)  #final vote count would not print in loop

    print("Election Results")
    print("-----------------------")
    print(f"Total Votes: {vote_count}")
    print("-----------------------")
    for i in range(len(name_results)):
        percent = round((vote_results[i]/vote_count)*100,3)
        print(f"{name_results[i]}: {percent}%  ({vote_results[i]})")
    
    print("-----------------------")

    max_vote = max(vote_results)
    winner = name_results[vote_results.index(max_vote)]
    print(f"Winner: {winner}")
    print("-----------------------")

#open output file
textpath = Path(__file__)/"../analysis/result.txt"
result_file = open(textpath, "w")

#write results to file
result_file.write("Election Results\n")
result_file.write("-----------------------\n")
result_file.write(f"Total Votes: {vote_count}\n")
result_file.write("-----------------------\n")
for i in range(len(name_results)):
    percent = round((vote_results[i]/vote_count)*100,3)
    result_file.write(f"{name_results[i]}: {percent}%  ({vote_results[i]})\n")
    
result_file.write("-----------------------\n")
result_file.write(f"Winner: {winner}\n")
result_file.write("-----------------------\n")

#close output file 
result_file.close()
    