# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
found = False
with open (csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    for row in csvReader:
        if(video == row[0]):
            print( row[0] + " is rated "+ row[1]+ " with a rating of "+ row[5])
            found = True
            break
        #print(row)
if found is False:
    print("Video not Found")