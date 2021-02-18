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
        profit.append(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        full_profit = int(row[1])
        monthly_change_profit_loss = full_profit - initial_profit
        monthly_changes.append(monthly_change_profit_loss)

        total_change = full_profit + monthly_change_profit_loss
        initial_profit = full_profit

        average_change = (total_change/total_months)

        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period

        max_change = max(monthly_changes)
        max_change_date = date[monthly_changes.index(max_change)]
        min_change = min(monthly_changes)
        min_change_date = date[monthly_changes.index(min_change)]


    print (total_months)
    print (total_profit_loss)
    print (average_change)
    print (max_change)
    print (max_change_date)
    print (min_change)
    print (min_change_date)

    


#Output into a TXT file 


