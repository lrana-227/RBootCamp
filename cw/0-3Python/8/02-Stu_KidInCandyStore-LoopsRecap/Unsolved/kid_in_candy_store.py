# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    print (candy)
   # print("[" +  candy_list.index(candy) + "] " + {candy})



x = "Yes"
while x == 'Yes':
    int choice = input("Select the number candy you want!")
    candy_cart.append(choice)
    allowance ++ 
    if allowance > 5:
        print("No more candy allowed!")


