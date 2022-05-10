WEEK 3

numbers=[1,2,3,4,5]
food=["noodle", "sushi", "mushrooms", "eggs", "oranges"]
animals=["cat", "dog", "zebra", "elephant", "lion"]
print("My favourite food is:", food[1:4])
print("My favourite animals is", animals[1:4])
print("My favourite numbers is", numbers[1:4])
food.append("apple")
food.append("grapes")
print (food)
animals.insert(1,"snake")
print(animals)
print(max(numbers))
print(min(numbers))


list1 = [1, 203, 36, 28, 4000, 49]
print ("sum:", max(list1)+min(list1))
list1.append(max(list1))
list1.append(min(list1))
print(list1)


first=input("What is your first name?")
last=input("What is your last name?")
list2 = ["your", "first", "name", "is", "and", "your", "last", "name", "is", "."]
list2.insert(4, str(first))
list2.insert(-1, str(last)) 
print (list2)


list1 = [1, 203, 36, 28, 4000, 49]
list1.append(25)
list1.insert(3, 65)
print (list1)
print(min(list1), max(list1), sum(list1))