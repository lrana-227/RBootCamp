import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('Resources', 'election_data.csv')

#Initilize Variable 
count = 0
vote_count = []
candidate = []
percent = []


with open(poll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # The total number of votes cast
    for row in csvreader:
        count = count + 1

        #person voted for 
        person = row[2]

        #A complete list of candidates who received votes
        #Check if person has other votes and continue to add to the counter, else make a new spot for the person
        if person in candidate:
            candidate_index = candidate.index(person)
            vote_count[candidate_index] = vote_count[candidate_index]+1
        else:
            candidate.append(person)
            vote_count.append(1)

max_vote = vote_count[0]
max_index = 0
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

for num in range(len(candidate)):
    vote_percent = (vote_count[num]/count)*100
    percent.append(round(vote_percent,3))  
    if vote_count[num] > max_vote:
        max_vote = vote_count[num]
        max_index = num
candidate_winner = candidate[max_index]



print("Election Results")
print("--------------------------")
print(f"Total Votes: {count}")
for x in range(len(candidate)):
    print(f"{candidate[x]}: {percent[x]}% ({vote_count[x]})")
print("---------------------------")
print(f"Winner: {candidate_winner}")
print("---------------------------")


#Output into a TXT file 

write_file = open("Analysis/result.txt", mode = 'w')

write_file.write("Election Results\n")
write_file.write("--------------------------\n")
write_file.write(f"Total Votes: {count}\n")
for x in range(len(candidate)):
    write_file.write(f"{candidate[x]}: {percent[x]}% ({vote_count[x]})\n")
write_file.write("---------------------------\n")
write_file.write(f"Winner: {candidate_winner}\n")
write_file.write("---------------------------\n")
write_file.close()

