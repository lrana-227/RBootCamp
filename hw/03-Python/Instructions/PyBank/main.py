import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Initialize Variables
total_months = 0
total_profit_loss = 0
initial_profit = 0

#Adding values to list 
profit = []
monthly_changes = []
date = []


def profitorloss(budget_data):
    profit_losses = int(budget_data[1])
    return profit_losses


# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    
    
    for row in csvreader:

        #The net total amount of "Profit/Losses" over the entire period
        rowprof = int(profitorloss(row))
        total_profit_loss = total_profit_loss + rowprof

        #The total number of months included in the dataset
        total_months = total_months+1

        date.append(row[0])
        profit.append(int(row[1]))

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for i in range(len(profit)-1):
        monthly_changes.append(profit[i+1]-profit[i])
        
    average_change = round((sum(monthly_changes)/(total_months-1)),2)

    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

    max_change = max(monthly_changes)
    max_change_date = date[monthly_changes.index(max_change)]
    min_change = min(monthly_changes)
    min_change_date = date[monthly_changes.index(min_change)]


    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print (f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits:  {max_change_date} (${max_change})")
    print(f"Greatest Decrease in Profits:  {min_change_date} (${min_change})")

#Output into a TXT file 

write_file = open("Analysis/result.txt", mode = 'w')

write_file.write("Financial Analysis\n")
write_file.write("--------------------------\n")
write_file.write(f"Total Months: {total_months}\n")
write_file.write(f"Total: ${total_profit_loss}\n")
write_file.write(f"Average Change: ${average_change}\n")
write_file.write(f"Greatest Increase in Profits: {max_change_date} (${max_change})\n")
write_file.write(f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n")
write_file.close()


