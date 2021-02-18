import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_profit_loss = 0

def profitorloss(budget_data):
    profit_losses = int(budget_data[1])
    return profit_losses

    
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    #The greatest increase in profits (date and amount) over the entire period

    #The greatest decrease in losses (date and amount) over the entire period











# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
         #print_budget_data(row)
         rowprof = int(profitorloss(row))
         total_profit_loss = total_profit_loss + rowprof
         total_months = total_months+1
    print(total_months)
    print (total_profit_loss)



#Output into a TXT file 


