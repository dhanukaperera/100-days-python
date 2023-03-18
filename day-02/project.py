print("Welcome to the tip calculator.")
total_bill =  float(input("What was the total bill? $ "))
tip_percentage =  float(input("What percentage tip would you like to give:? 10, 12, or 15? "))
total_people = float(input("How many people to split the bill? "))

total_price =  total_bill + ((tip_percentage * total_bill)/100)
tip_per_person = round(total_price / total_people,2)

print(f"Each person should pay: $ {tip_per_person}")