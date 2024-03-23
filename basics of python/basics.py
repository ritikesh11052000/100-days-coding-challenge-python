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















"""def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)"""






"""temp = input("enter ur temp")
temp = float(temp)
print(temp)
temp = temp + 1.5
print(type(temp))
print(temp)
"""













"""M_list = [1,2,3,4]
count = 1
for item in M_list:
    if item == 4:
        print("item matched")
        count +=1
        break
print("found at loaction", count)
"""










#list1 = [4,3,5,1,2]
#list2 = ['LUFFY','ZORO','SANJI','JINBE']
#del list2[3]
#print(list2)
#list3 = list2.copy()
#list2.pop()
#print(list2)
#print(list3)
#list2.reverse()
#print(list2)
#list1.sort()
#print(list1)
#print(list2.count('ZORO'))
#print(list2.index('ZORO'))
#list2.insert(1,'CHOPPER')
#list2.remove('JINBE')
#list2.clear()
#print(list2)
"""list2.append('CHOPPER')
list.extend(list2)
print(list2)
print(len(list2))"""




















"""one_piece = list(('LUFFY',17,True))
print(one_piece[0])
print(type(one_piece))"""


















"""sentance = input('enter your sentance : ')
print('your sentance is: '+sentance)
world = input('enter the word to replace: ')
word1 = input('enter the word to replace: ')
print(sentance.replace(world,word1))"""


















"""
name = input('enter your name : ')
age = int(input('enter you age : '))

#print('so your name is ' + name + ' and your age is ' +str(age) + ' years old')
#print('so your name is ' + name + ' and your age is ', age)
"""
