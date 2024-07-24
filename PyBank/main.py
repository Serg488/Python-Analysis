import os 
import csv
#import csv file path
csv_file_path = os.path.join("Resources", "budget_data.csv")
#open file path
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    #loop through each row of csv reader
    total_months = 0
    net_total = 0
    changes = []
    previous_profit = 0
    profit_data = []
    #set for and if statements for months and profits
    for i in csv_reader:
        total_months += 1
        profit = int(i[1])
        net_total += profit
        profit_data.append((i[0], profit))
        if total_months > 1:
                change = profit - previous_profit
                changes.append(change)
        previous_profit = profit
    #caculate average change
    average_change = sum(changes) / len(changes)
    #print all of the Totals for months, average change and titles
    print("Financal Analysis")
    print("-----------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    #caculate the greatest increase
    greatest_increase = float('-inf')
    greatest_increase_date = ""
    #create for and if statement
    for date, profit in profit_data:
        if profit - previous_profit > greatest_increase:
            greatest_increase = profit - previous_profit
            greatest_increase_date =date
        previous_profit = profit
    #print greatest_increase_date
    if greatest_increase_date:    
        print(f"Greatest Increase in Profits {greatest_increase_date} (${greatest_increase})")
    greatest_decrease = float('inf')
greatest_decrease_date = ""
    #figure out the date and profit
for date, profit in profit_data:
    if profit - previous_profit < greatest_decrease:
        greatest_decrease = profit - previous_profit
        greatest_decrease_date = date
    previous_profit = profit
#caculate greatest decrease in profits
if greatest_decrease_date:
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    