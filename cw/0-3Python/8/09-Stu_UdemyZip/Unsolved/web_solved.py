import os
import csv

udemy_csv = os.path.join("..", "Resources", "web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

#sheet = zip(title,price,subscribers,reviews,review_percent,length)
# Use encoding for Windows
with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscribers.append(row[5])
        reviews.append(row[6])
        review_percent.append(round(int(row[6])/int(row[5]),2))
        length.append(row[9].split(" ")[0])

newList = zip(title,price,subscribers,reviews,review_percent,length)

output_file = os.path.join("web_final.csv")
with open(output_file,"w", newline='', encoding='utf-8') as writefile:
   
    csvWriter= csv.writer(writefile)
    csvWriter.writerow(["Title", "Price", "Subscriber Count","Number of Review","Review Percentage","Course Lenght"])
    csvWriter.writerows(newList)



# OR below one for MAC
# with open(udemy_csv, newline='') as csvfile: