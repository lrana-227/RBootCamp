import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('Resources', 'trial.csv')

#Initilize Variable 
count = 0
candidate = []

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.



with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter=',')
    header = next(csvreader)

    
    for row in csvreader:
        myDict ={row['Voter ID'],row['County'], row['Candidate']}
        candidate.append(myDict)
        list_keys = [ k for k in myDict ]

        #The total number of votes cast
        count = count + 1
    print(list_keys)
    print (count)
    #print (candidate)
#Output into a TXT file 
