# all about for loop and if else





target = int(input())  
# Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

# evnn_num = 0

# for num in range(2,target + 1,2):
#   # print(num)
#   evnn_num += num
# print(evnn_num)

#second method : -
sum = 0
for num in range(1, target + 1):
  # print(num)
  if num % 2 == 0:
    sum += num
print(sum)





# for i in range(2,22,2):
#   print(i)





# total = 0
# for num in range(2,201,2):
#   # total +=1
#   # print(total)
#   print(num)





# # Input a list of student scores
# student_scores = input("enter students score : ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# heighest_score = 0
# for score in student_scores:
#   if score>heighest_score:
#     heighest_score = score
# print(heighest_score)






# # Input a list of student scores
# student_scores = input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# # print(f"The highest score in the class is: {max(student_scores)}")
#
# heighest_score = 0
#
# for score in student_scores:
#   if score > heighest_score:
#     heighest_score = score
# print(f"The highest score in the class is: {heighest_score}")







# # Input a Python list of student heights
# student_heights = input("enter students heights : ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# total_height = 0
#
# for heights in student_heights:
#   total_height += heights
# print(f"total height = {total_height}")
#
#
# number_of_student = 0
# for student in student_heights:
#   number_of_student +=1
# print(f"number of students = {number_of_student}")
#
#
# average_height = round(total_height/number_of_student)
# print(f"average height = {average_height}")
#






"""crew = ["luffy", "zoro", "sanji"]
for crew_m in crew:
    print(crew_m)
    print(crew_m + " fight")
print(crew)
"""