#modules
import os
import csv
from pathlib import Path

#set path for financial data file
csvpath = Path(__file__)/"..\Resources/budget_data.csv"

#open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #strip off headers
    header = next(csvreader)
    #variables for output
    netprofit = 0
    m_count = 0
    avg_profit = []
    avg_hold = 0
    copy_list = []

    #read off rows
    for row in csvreader:
        netprofit = netprofit + int(row[1])
        m_count = m_count + 1
        copy_list.append(row)

        if m_count == 1:
            avg_hold = int(row[1])
        else:
            avg_profit.append(int(row[1])-avg_hold)
            avg_hold = int(row[1])
        


    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {m_count}")
    print(f"Total: ${netprofit}")

    avg_round = sum(avg_profit)/len(avg_profit)
    avg_round = round(avg_round, 2)
    print(f"Average Change: ${avg_round}")

    max_profits = max(avg_profit)
    min_profits = min(avg_profit)
    max_index = avg_profit.index(max_profits)
    min_index = avg_profit.index(min_profits)
    max_month = copy_list[max_index+1]  #index needs to increase by one because 
    min_month = copy_list[min_index+1]  #avg_profit starts at second month
    print(f"Greatest Increase In Profits: {max_month[0]} (${max_profits})")
    print(f"Greatest Decrease In Profits: {min_month[0]} (${min_profits})")

#open output file
textpath = Path(__file__)/"../analysis/result.txt"
result_file = open(textpath, "w")

result_file.write("Financial Analysis\n")
result_file.write("--------------------------\n")
result_file.write(f"Total Months: {m_count}\n")
result_file.write(f"Total: ${netprofit}\n")
result_file.write(f"Average Change: ${avg_round}\n")
result_file.write(f"Greatest Increase In Profits: {max_month[0]} (${max_profits})\n")
result_file.write(f"Greatest Decrease In Profits: {min_month[0]} (${min_profits})\n")
#close output file
result_file.close()