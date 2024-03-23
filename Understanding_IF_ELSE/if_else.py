
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


