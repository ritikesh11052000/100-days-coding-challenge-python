#Day 2 - udemy python course task/Project: -
print("welcome to the tip claculator")
bill = float(input("what was the total bill-"))
tip = int(input("what percentage tip would you like to give ? 10, 12, or 15? : -"))
people = int(input("how many people to spilt the bill-"))

bill_with_tip = tip/100 * bill +bill
#tip_as_percent = tip/100
#total_tip_amount = bill * tip_as_percent

#total_bill = bill + total_tip_amount

bill_per_person = bill_with_tip/people
final_amount = "{:2f}".format(bill_per_person)
print(int(input(f" each person should pay- {final_amount}")))

