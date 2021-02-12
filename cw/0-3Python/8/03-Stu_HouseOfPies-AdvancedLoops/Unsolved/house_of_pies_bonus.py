# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0,0,0,0,0,0,0,0,0,0]
tot= 0
# Pie List
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
# Loop starts here
i = 1
while shopping == "y":
    for pies in pie_list:
        #print("-------------------------------------------------------------")
        print("(" + str(i) + ")" + pies)
        i=i+1

    select = int(input("Which pie number would you like? "))
    pie_purchases[select] =  pie_purchases[select] +1
    tot= tot +1
    print("Great! We'll have that" + pie_list[select-1] +"right out for you.")
    shopping = input("Would you like to still shop? (y)es or (n)o" )
    i =1





# Loop end here
# Once the pie list is complete
print("------------------------------------------------------------------------")

z =1
for pies in pie_list:
        print(str(pie_purchases[z])+ pie_list[z] )
        z=z+1
print("You purchased a total of " + str(tot) + ".")


