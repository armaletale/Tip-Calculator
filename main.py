#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcom to the tip calculator.")

bill = input("What was the total bill? $")

percentage_of_tip = input("What percentage of tip would you like to give? 10, 12, or 15? ")

num_of_people = input("How many people are to split the bill? ")

a = float(bill)
b = int(percentage_of_tip)
per_b = b / 100

c = int(num_of_people)

amount = a * per_b

amount_1 = a + amount

amount_to_be_paid = round(amount_1 / c, 2)

print (f"Each person should pay: ${amount_to_be_paid}")





