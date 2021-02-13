import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")

# Open and read csv
with open(cereal_csv) as csv_file:
    group  = csv.reader(csv_file,delimiter=",")

    csv_header = next(csv_file)
    #print(csv_header)

    for row in group:
        if float(row[7]) >= 5:
            print (row)

