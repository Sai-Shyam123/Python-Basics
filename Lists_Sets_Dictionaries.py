# Lists
print(type([]))

num = 1
num_two = 2
num_three = 3

numbers = [1, 1, 2, 3, 4, 'hello']

numbers[5] = 'whitesheep'
# Useful List Methods

# numbers.sort()
# numbers.reverse()
# numbers.append(1000)
# print(len(numbers))
# numbers.clear()
# print(1 in numbers)
# print(1 not in numbers)
print(numbers)

# delete a item from a list
# numbers.remove(1)

# # to remove the last element
# numbers.pop()
# numbers.pop()

# # the other way to remove
# del numbers[0]

# # deleting by range(not index based)
# del numbers[0:8]
# print(numbers)

# SETS

numberList = [1, 1]
# we cannot duplicate values
numberSet = {1, 1}
print(numberSet)
# sets are not guaranteed to be in order
lettersSet = {'a', 'a', 'b', 'c', 'c'}
print(lettersSet)

# Set Intersection And Difference

# intersection prints out only common values between the 2 lists
# union prints out everything in union

lettersA = {'A', 'B', 'C', 'D'}
lettersB = {'A', 'E', 'F'}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersB - lettersA
print(lettersA | lettersB)
print(union)
print(f"Union = {union}")
print(f"Intersection = {intersection}")
print(f"Difference = {difference}")

# Dictionaries

person = {
    "name" : "Jamal",
    "age" : 20,
    "address" : "USA"
}
print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())
# person.clear()
print(person.get("age"))
person["age"] = 100
print(person)
