import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print(f"{rock},\n {paper},\n {scissors}")
img = [rock,paper,scissors]

user = int(input("enter 0 - rock , 1 - paper , 2 -scissors  : \n "))
print(f"your choice is : {user}")

if user >= 3 or user < 0:
    print("invalid number pleas select between 0 to 2")
else:

    print(img[user])

    robot = random.randint(0,2)

    print(f"bot choice: {robot} ")
    print(img[robot])



    if user == 0 and robot == 2:
        print("you wins !")
    elif robot == 0 and user == 2:
        print("you lose")

    elif robot > user:
        print("you lose")
    elif user > robot:
        print("you win!")

    elif robot == user:
        print("It's a draw")



