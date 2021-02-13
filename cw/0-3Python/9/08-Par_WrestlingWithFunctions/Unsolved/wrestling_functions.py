import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def wrestlerData (wrestlerData):
# Find the total number of matches wrestled
    totalnum = int(wrestlerData[1])+int(wrestlerData[2])+int(wrestlerData[3])
# Find the percentage of matches won
    winpercent = (int(wrestlerData[1] )/ totalnum) *100
# Find the percentage of matches lost
    lostpercent = (int(wrestlerData[2]) / totalnum) *100
# Find the percentage of matches drawn
    drawnpercent = (int(wrestlerData[3] )/ totalnum)*100

    if lostpercent > 50:
        wrest_type = "Jobber"
    else:
        wrest_type = "Superstar"
# Print out the wrestler's name and their percentage stats
    print (f"{ wrestlerData[0]} Wins% {winpercent}  Lost%  {lostpercent} Draws% {drawnpercent} {wrest_type}")
# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            wrestlerData(row)
