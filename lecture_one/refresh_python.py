"""
Write a Python program that can do the following:
- You have $50
- You buy an item that is $15, that has a 3% tax
- Using the print()  Print how much money you have left, after purchasing the item.
--------------------------------------------------
amount = 50
new_item = 15 + (15*0.03)
print(amount - new_item)


String Assignment. (This can be tricky so feel free to watch solution so we can do it together)
- Ask the user how many days until their birthday
- Using the print()function. Print an approx. number of weeks until their birthday
- 1 week is = to 7 days.
-------------------------------------------------
days_until_birthday = int(input("How many days until your birthday?"))
print(round(days_until_birthday/7))


# Lists are collection of data ordered and of any type
-----------------------------
my_list = [80, 96, 72, 100, 8]
print(my_list)
my_list.append(200)
print(my_list)
my_list.insert(2,17)
print(my_list)
my_list.remove(100)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)


# Sets are unordered and cannot contain duplication
------------------------
my_set = {1,2,3,4,5}
print(my_set)
my_set.discard(3)
print(my_set)
my_set.clear()
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([4,5,2])
print(my_set)


# Tuples are unmutable
--------------------
my_tuple = (5,3,1,2)
print(my_tuple)
print(my_tuple[1])
"""

"""
- Create a list of 5 animals called zoo
- Delete the animal at the 3rd index.
- Append a new animal at the end of the list
- Delete the animal at the beginning of the list.
- Print all the animals
- Print only the first 3 animals
--------------------------------------------------
zoo = ['jiraf', 'lion', 'bee', 'whale', 'horse']
print(zoo)
zoo.pop(3)
print(zoo)
zoo.append('cat')
print(zoo)
zoo.pop(0)
print(zoo)
print(zoo[:3])
"""

"""
- Create a variable grade holding an integer between 0 - 100
- Code if, elif, else statements to print the letter grade of the number grade variable
Grades:
A = 90 - 100
B = 80 - 89
C = 70-79
D = 60 - 69
F = 0 - 59
Example:
if grade = 87 then print('B')
----------------------------
grade = 87
if 90 <= grade <= 100:
    print('A')
elif 80 <= grade <= 89:
    print('B')
elif 70 <= grade <= 79:
    print('C')
elif 60 <= grade <= 69:
    print('D')
else:
    print('F')
    

Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements, use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
-------------------------------
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
i = 0
while i != 3:
    i += 1
    for element in my_list:
        if element == 'Monday':
            continue
        print(element)
        

#Dictionaries are key value pairs. We need to use .copy() when we are going to duplicate a dictionary
to don't modify the initial dictionary
------------------------------------------
user_dict = {
    "username": "valensag",
    "name": "valentina",
    "age": 27
}
# print(user_dict.get("username"))
user_dict["married"] = False
# print(user_dict)
# user_dict.pop("age")
# print(user_dict)
# user_dict.clear()
# print(user_dict)
# del user_dict

user_dict_2 = user_dict.copy()
# print(user_dict_2)
user_dict_2.pop("age")
print(user_dict)
print(user_dict_2)


Based on the dictionary:
- Create a for loop to print all keys and values
- Create a new variable vehicle2, which is a copy of my_vehicle
- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
- Delete the mileage key and value from vehicle2
- Print just the keys from vehicle2
------------------------------------
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
for key,value in my_vehicle.items():
    print(key,value)

vehicle2 = my_vehicle.copy()
vehicle2['number_of_tires'] = 4
vehicle2.pop('mileage')
print(vehicle2.keys())


# Imports
------------------------------------
import random, math
types_drink = ['soda', 'coffee', 'water', 'tea']
print(random.choice(types_drink))

square_root = math.sqrt(64)
print(square_root)


# OOP Paradigm with concepts of object
_______________________________________
You can define objects by:
- Behavior (walk, bark, run)
- State (4 legs, 2 ears, 5 years old, yellow) 
Four Pillars
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
2 subques created in different projects, and there is a issue with the ids
this could be a network issue
2 different subques creating in 2 different projects with the same id


# Abstraction
Is a flashlight with on off switch
We don't know how it works, we just know that when is on it is going to generate light
- Abstraction means that we want to hide the implementation and only show necessary details to the user

# Constructors
Create and initialize an object of a class with or without starting values
Types of Constructors:
- Empty
- No argument
- Parameter

"Encapsulation
__ is going to convert public in private
we need to create get and set functions

# Inheritance
Process of acquiring properties from one class to another classes
Creates a hierarchy between classes
- Method overriding is when a child class has its own method already present in the parent class

# Self vs Super
- Self is used to refer to the current object that is created or being instantiated
- Super is used to refer to the parent class

# Polymoorphism
Many ways to do something

# Composition
A way to create objects made up of another objects
A class contains one or more objects of another class as instance variables

# Virtual env
1. Install python 3.11

2. Create the venv
python3.11 -m venv venv

3. Activate the venv
source venv/bin/activate

4. Deactivate the venv
deactivate

# Install other libraries
pip install fastapi
pip install "uvicorn[standard]"

"""














