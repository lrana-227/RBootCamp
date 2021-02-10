# Take input of you and your neighbor
your_name= input("What is your name?")
neighbor_name = input("What is your neighbor's name?")

# Take how long each of you have been coding
your_length= int(input("How long has "+ str(your_name)+ " been coding in years?"))
neighbor_length= int(input("How long has "+ str(neighbor_name)+ " been coding in years?"))

# Add total month
total_month = your_length*12 +neighbor_length*12

# Print results
print(f"The total amount of months {your_name} and {neighbor_name} have coded is {total_month}")
