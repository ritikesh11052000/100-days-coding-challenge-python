
print("welcome to the roller coaster")
height = int(input("what's you height : "))
bill = 0

if height >= 120:
  print("you can ride")
  age = int(input("what's your age : "))
  if age <= 4:
    bill = 3
    print("please pay $4")
  elif age <=12:
    bill = 5
    print("please pay $5,")
  elif age <= 18:
    bill = 8
    print("please pay $7")
  elif age>=45 and age <=55:   #and logical operator
      print("free ride")
  else:
    bill = 10
    print("please pay $12.")

  photo = input("do you want a photo ? Y / N : ")
  if photo == "Y":
    bill += 3
    print(f"your bill is {bill}")
else:
  print("you are under age or you height is less")






"""print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
    bill += 20
else :
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill +=2
  else:
    bill +=3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")



"""


"""print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")"""







"""
#print("welcome to the roller coaster")
height = int(input("what's you height : "))
bill = 0

if height >= 120:
  print("you can ride")
  age = int(input("what's your age : "))
  if age <= 4:
    bill = 3
    print("please pay $4")
  elif age <=12:
    bill = 5
    print("please pay $5,")
  elif age <= 18:
    bill = 8
    print("please pay $7")
  else:
    bill = 10
    print("please pay $12.")

  photo = input("do you want a photo ? Y / N : ")
  if photo == "Y":
    bill += 3
    print(f"your bill is {bill}")
else:
  print("you are under age or you height is less")
"""

















"""# Which year do you want to check?
year = int(input("Enter the year : "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
"""






"""print("welcome to the coster")
height = int(input("what's you height :"))

if height >= 120:
  print("you can ride")
  age = int(input("what's your age"))
  if age <= 4:
    print("please pay $4")
  elif age <=12:
    print("please pay $5,")
  elif age <= 18:
    print("please pay $7")
  else:
    print("please pay $12.")


else:
  print("you are under age or you height is less")"""











"""# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
  print(number)
else:
  print("This is an odd number.")
  print(number)"""

