def doctor():
    name = (input("Enter your name: "))
    print ("welcome doctor", name)

def patient():
    name = (input("Enter your name: "))
    print ("Welcome ", name)
    patient_decision = (input("press 1 for book an appointment\npress 2 to know the available doctors\n"))

given_input = (input("If you're a doctor press 1 or if you're patient press 2:"))

if given_input == 1:
    doctor()
elif given_input == 2:
    patient()
else:
    print("Invalid input")

# ___________________________________________________________________________________________________________ #
import random

lower_bound = 1
upper_bound = 100
max_attempts = 10

target_number = random.randint(lower_bound, upper_bound)

for attempt in range(max_attempts):
    guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too High")
    else:
        print("Congratulations! You guessed the number!")
        break
# ___________________________________________________________________________________________________________ #

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print (arr)

# ___________________________________________________________________________________________________________ #
import numpy as np

arr = np.array([]) 


Question = Element("Question_place")
opt_a = Element("opt_a")
opt_b = Element("opt_b")
opt_c = Element("opt_c")
opt_d = Element("opt_d")
questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which bird is known for its colorful feathers and tail?",
        "Parrot", "Peacock", "Crow", "Sparrow", 2
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    
    print (question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
            elif(i == 9):
            money = 320000
            elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break 
        
    print(f"Your take home money is {money}")            

# ================================================================================================================ #
from scipy import constants #Install 'scipy' using 'pip'

print(constants.pi)
print(constants.minute)
print(constants.year)
print(constants.hour)
print(constants.day)
print(constants.Julian_year)

print(dir(constants))
# ================================================================================================================ #
from tkinter import * #install 'tk' using 'pip'
root = Tk()

root.geometry('350x200')

root.title("Welcome to python programming")

menu = Menu(root)
item = Menu(root)

menu.add_cascade(label="File", menu = item)
item.add_command(label="New")

root.config(menu=menu)

lbl= Label(root, text="Are you a student??")
lbl.grid()

given_txt = Entry(root, width=10)
given_txt.grid(column=1, row=0)

def clicked():
    res = "You wrote "+ given_txt.get()
    lbl.configure(text = res)

butn = Button(root, text="click me", fg="red", command=clicked)
butn.grid (column=2, row=0)

root.mainloop()
# ================================================================================================================ #
import numpy as np #install 'numpy' using 'pip'

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([50, 40, 30, 20, 10])
resultArr = np.add(arr1, arr2)
print (resultArr)
resultArr = np.subtract(arr1, arr2)
print (resultArr)
resultArr = np.multiply(arr1, arr2)
print (resultArr)
resultArr = np.divide(arr1, arr2)
print (resultArr)
resultArr = np.power(arr1, arr2)
print (resultArr)

# ================================================================================================================ #
import  #no need for installing using pip

nigger = random.randrange(0, 100, 10)
print(nigger)
# ================================================================================================================ #
import random 
nigger = random.choice('Random Module') #a string 
print(nigger) 
nigger = random.choice([23, 54, 765, 23, 45, 45]) #a list 
print(nigger) 
nigger = random.choice((12, 64, 23, 54, 34)) #a set 
print(nigger)
# ================================================================================================================ #
import random
nigger = [34, 56, 69, 77, 70]
random.shuffle(nigger)
print(nigger)
# ================================================================================================================ #
nigger, temp = [5, 7, 8, 4, 10, 250], 0

print ('Elements of array before sorting: ')

def arrayPrinter():
    for i in range(0, len(nigger)):
        print(nigger[i], end=" ")

arrayPrinter()

print ('\n\nElements after sorting array in increasing order: ')

for i in range(0, len(nigger)):
    for j in range (i+1, len(nigger)):
        if (nigger[i] > nigger[j]):
            temp = nigger[i]
            nigger[i] = nigger[j]
            nigger [j] = temp

arrayPrinter()

print ('\n\nElements after sorting array in decreasing order: ')


for i in range(0, len(nigger)):
    for j in range (i+1, len(nigger)):
        if (nigger[i] < nigger[j]):
            temp = nigger[i]
            nigger[i] = nigger[j]
            nigger [j] = temp

arrayPrinter()
# ================================================================================================================ #
# x = "Nigga maaney" ##remove one hash to execute try statement 
try:
    print(x)
except:
    print("Nah! there's no variable called x")
# ================================================================================================================ #
#example

nigger = ["Orange", "Apple", "Banana", "Mustard Apple"]
print(nigger)

try: 
    nigger.remove["gulab Jamun"]
except:
    print(" nah, nah baba there's no gulab jamun in this list")
finally:
    print ("hal")

#example
nigger = ["Gulab Jamun", "Gulab Jal", "Gulab"]
print(nigger)

try:
    nigger.remove["Gulab Jamun"]
    print(nigger)
except:
    print("Why crying, Gulab jamun waise bhi not in your aukat")
finally:
    print("hal")

# ================================================= Code Not Working =================================================== #
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print("select from the following options: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    choice = input("Enter Option: ")

    if choice in ('1', '2', '3', "4"):
        num1 = input("Enter first operand: ")
        num2 = input("Enter Second operand: ")
        
    if choice == 1:
        print(add(num1, num2))
    
    elif choice == 2:
        print(subtract(num1, num2))
    
    elif choice == 3:
        print(multiply(num1, num2))
    
    elif choice == 4:
        print(divide(num1, num2))
    
    elif choice == 5:
        print("Thank you for choosing our calc")
        break

    else:
        print("Invalid Choice")   
        break 

# =============================================================================================================================================== #

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

person1 = Person("Raoul", 20)
person2 = Person("SAR", 21)

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)
# =============================================================================================================================================== #
class A (object):
    def __new__ (cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__ (self):
        print ("init is called")

A()
# =============================================================================================================================================== #
class quadriLateral:
    def __init__(self, a, b, c, d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d

    def parameter(self):
        p = self.side1 + self.side2 + self.side3 + self.side4
        print("Parameter = ", p)

q1 = quadriLateral(7, 4, 5, 6)
q1.parameter()

class rectangle(quadriLateral):
    def __init__ (self, a, b):
        super().__init__(a,b, a, b)

r1=rectangle(10, 20)
r1.parameter()
# =============================================================================================================================================== #
class A:
    def explore(self):
        print("explore() method from class A")

class B:
    def explore(self):
        print("explore() method from class B")

b_obj = B()
a_obj = A()

b_obj.explore()
a_obj.explore()
# =============================================================================================================================================== #
import re

pattern = "^a...s$"
text = "abyss"
result = re.match (pattern, text)
if result:  
    print("search succesful")
else:
    print("search unsuccesful")
# =============================================================================================================================================== #

import re 

s = "Mother wins all battles"
result = re.findall(r"[aeiou]", s)
print (result)
# =============================================================================================================================================== #
import re 
matcher = re.finditer("a", "abaabaababaa")
for match in matcher:
    print(match.start(), "........", match.group())
# =============================================================================================================================================== #
import re

words = ('seven', 'even', 'prevent', 'revenge', 'maven', 'eleven', 'amen', 'event')

pattern = re.compile(r."even")
for word in words:
    if re.match(pattern, word):
        print(f"The {word} matches")
# =============================================================================================================================================== #
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello My name is " + self.name)

p1 = person("John", 30)
p1.myfunc()
print(p1.age)
# =============================================================================================================================================== #
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

coordinates = (1, 2, 3, 4, 5)
for point in coordinates:
    print(point)

dictionary = {"Name":"a person's identity which is assign to him at the birth", "Age":"The number of person's years passed by after his birth"}

for realWords in dictionary:
    print (realWords)

print ("\n")

for meaning in dictionary.values():
    print (meaning)

print("\n")

for realWords, meaning in dictionary.items():
    print (realWords, meaning, sep=": ")

odd_numbers = {1, 3, 5, 7}
for numbers in odd_numbers:
    print (numbers)

the_string = "Hello niggesh! how are you?"
for words in the_string:
    print(the_string)

the_string = "Hello niggesh! how are you?"
for i in range(0, 3):
    print (the_string)

pairs = [(1, 2), (3, 4), (5, 6)]
for x, y in pairs:
    print(x, y)

# Sample list
animals = ["dog", "cat", "rabbit", "hamster"]

# Using a for loop to print each element
for animal in animals:
    print(animal)

year2024 = ["sigma", "rizzler", "Goat" "gyatt", "skibidi"]
for brainrot in year2024:
    print(brainrot, end=" ")

# =========================================================== A large integer =================================================================== #
large_num = 10**100  # A huge integer
print(large_num)
# =============================================================================================================================================== #
a = 0.1 + 0.2
print(a)  # Output will be 0.30000000000000004, not exactly 0.3 due to precision limits
b = 0.4 + 0.5
print(b)
# =============================================================================================================================================== #
z = 3 + 4j
print(abs(z))  # Output: 5.0 (the magnitude of the complex number)
print(z.conjugate())  # Output: (3-4j)

if condition:
    # This block is indented and executed if the condition is true
    print("Condition is true")
# =============================================================================================================================================== #
integer_value = 42
string_value = str(integer_value)
print(type(string_value))
# =============================================================================================================================================== #
# Explicit type conversion
float_value = 5.67

# Converting float to integer
int_value = int(float_value)
print("Integer value:", int_value)  # Outputs: 5

# Converting string to float
str_value = "3.14"
float_from_str = float(str_value)
print("Float value from string:", float_from_str)  # Outputs: 3.14

for i in range(10):
    if i == 11:
        break
    print(i)
else:
    print("Loop completed without break")
# =============================================================================================================================================== #

# Taking input from the user
name = input("Enter your name: ")

# Displaying the input back to the user
print("Hello, " + name + "!")

for i in range(5):
    if i % 2 == 0:
        pass  # Placeholder for future code
    else:
        print(i)

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Outputs: [1, 2, 5, 9]

# Given list of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() and lambda to compute the squares
squares = map(lambda x: x**2, numbers)

# Converting the map object to a list and printing the squares
print(list(squares))

# =============================================================================================================================================== #

# Initial list
fruits = ["apple", "banana", "cherry"]

# Adding elements
fruits.append("date")
fruits.insert(1, "blueberry")  # Insert 'blueberry' at index 1
print("After adding elements:", fruits)

# Replacing elements
fruits[2] = "blackberry"  # Replace 'banana' with 'blackberry'
print("After replacing elements:", fruits)

# Removing elements
fruits.remove("apple")  # Remove 'apple' by value
popped_fruit = fruits.pop(3)  # Remove and return the element at index 3
print("After removing elements:", fruits)
print("Popped fruit:", popped_fruit)

# Sorting the list
fruits.sort()
print("After sorting:", fruits)

# Reversing the list
fruits.reverse()
print("After reversing:", fruits)

# Final list
print("Final list of fruits:", fruits)

def get_min_max(numbers):
    return (min(numbers), max(numbers))

min_max = get_min_max([1, 2, 3, 4, 5])
print(min_max)  # Outputs: (1, 5)

# =============================================================================================================================================== #
SAQ: Write a Python program to find the intersection and union of two sets.

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the intersection of the two sets
intersection = set1 & set2  #(or) intersection = set1.intersection(set2)

# Find the union of the two sets
union = set1 | set2 #(or) union = set1.union(set2)

# Print the results
print(f"Intersection of set1 and set2: {intersection}")
print(f"Union of set1 and set2: {union}")

# =============================================================================================================================================== #
LAQ: Write a program to create a class Student that stores 
     roll number, name and marks of three different subjects and 
     display the information roll number, name, marks

class student:
    def __init__ (self, roll_number, name, marks1, marks2, marks3):
        self.roll_number = roll_number
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def printer(self):
        print (f"Roll number: {self.roll_number}")
        print (f"Name: {self.name}")
        print (f"Marks in subject 1: {self.marks1}")
        print (f"Marks in subject 2: {self.marks2}")
        print (f"Marks in subject 3: {self.marks3}")

student1 = student(106, "Zaid", 100, 100, 100)

student1.printer()

# =============================================================================================================================================== #
LAQ: Write a program that has a class Person storing name and 
     date_of_birth of a person. The program should subtract the DOB from todays 
     date to find the person is eligible to vote or not

from datetime import datetime
class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age
    
    def is_eligible_to_vote(self):
        age = self.calculate_age()
        return age >= 18

person1 = Person("GigaChad", "2010-11-21")
person2 = Person("Nigga", "1969-06-09")

print (f"{person1.name} is {"eligible" if person1.is_eligible_to_vote() else "not eligible"} to vote")
print (f"{person2.name} is {"eligible" if person2.is_eligible_to_vote() else "not eligible"} to vote")
# =============================================================================================================================================== #
class Father:
    def work(self):
        print("Working")

class Mother:
    def cook(self):
        print("Cooking")

class Child(Father, Mother):
    def play(self):
        print("Playing")

# Creating an object of Child class
child = Child()
child.work()  # Inherited from Father
child.cook()  # Inherited from Mother
child.play()  # Child class method
# =============================================================================================================================================== #
# Single inheritance
class Father:
    def work(self):
        print ("Work")

class Mother:
    def cook(self):
        print("Cook")

father = Father()
mother = Mother()

father.work()
mother.cook()

# Multiple Inheritence
class Father:
    def work(self):
        print("Working in office")

class Mother:
    def cook(self):
        print("cooking Biryani")

class child(Father, Mother):
    def playing(self):
        print("Playing Playstation")

child1 = child()

child1.playing()
child1.cook()
child1.work()

# Multilevel Inheritance:
class Grandfather:
    def reading (self):
        print("Reading Newspaper") 

class Father(Grandfather):
    def working(self):
        print("Working in office")

class child(Father):
    def playing(self):
        print ("Playing Playstaion")

child1 = child()

child1.playing()
child1.working()
child1.reading()

# Hierarchical Inheritance:
class Father:
    def working(self):
        print("Working in office")

class Child1(Father):
    def studying(self):
        print("Studying for exams")

class Child2(Father):
    def playing(self):
        print("Playing games")

child1 = Child1()
child2 = Child2()

child1.studying()
child1.working()

child2.playing()
child2.working()

# Hybrid Inheritance:
class A:
    def method_A(self):
        print ("This is from A")

class B(A):
    def method_B(self):
        print ("This is from B")

class C(A):
    def method_C(self):
        print ("This is from C")

class D(B, C):
    def method_D(self):
        print ("This is from D")

d = D()

d.method_A()
d.method_B()
d.method_C()
d.method_D()
# =============================================================================================================================================== #
"""LAQ: Write a Python program to create a Class person which includes attributes 
        name, country and date of birth. Implement a method to determine the persons age."""

from datetime import date

class person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def ageCalculator(self):
        birth_year, birth_month, birth_day = map(int, self.date_of_birth.split("-"))
        dob = date(birth_year, birth_month, birth_day)
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

    def info(self):
        print (f"Name: {self.name}")
        print (f"Country: {self.country}")
        print (f"Date of birth: {self.date_of_birth}")
        print (f"Age: {self.ageCalculator()} Years")

person1 = person("SSAR", "KSA", "2005-07-11")
person2 = person("SAR", "USA", "2003-12-20")

person1.info()
person2.info()

# =============================================================================================================================================== #
LAQ: Write a program that has a dictionary of names of students and a list of marks in 4 subjects.

CSE_B_students = {
    "brainrot" : [85, 90, 50, 20],
    "Nigga" : [69, 77, 55, 69],
    "GigaChad" : [99,89,96, 75]
}

def AverageNTotal():
    for students, marks in CSE_B_students.items():
        totalMarks = sum(marks)
        average = totalMarks / len(marks)
        print (f"{students}: Marks = {marks}, Total = {totalMarks}, Average = {average}")

AverageNTotal()

# =============================================================================================================================================== #

LAQ: Create another dictionary that has name of the students and their total marks.
     Find the topper and his/her score.

CSE_B_students = {
    "brainrot" : [85, 90, 50, 20],
    "Nigga" : [69, 77, 55, 69],
    "GigaChad" : [99,89,96, 75]
}

studentTotalMarks = {}

for student, marks in CSE_B_students.items():
    totalMarks = sum(marks)
    studentTotalMarks[student] = totalMarks

topper = max(studentTotalMarks, key=studentTotalMarks.get)
topper_score = studentTotalMarks[topper]

print(f"The topper is {topper} with total score of {topper_score}")
print(studentTotalMarks)

# =============================================================================================================================================== #

# Polymorphism Example:

class animal:
    def sound(self):
        print ("Animal makes a sound")

class dog(animal):
    def sound(self):
        print ("Dog Barks (Bhow Bhow)")

class cat(animal):
    def sound(self):
        print ("Cat meows (meow meow)")

Animal = animal()
Dog = dog()
Cat = cat()

Animal.sound()
Dog.sound()
Cat.sound()

# =============================================================================================================================================== #

name = input("Enter student's name: ")
percentage = input("Enter student's percentage marks: ")

student_info = {}

student_info["Name"] = name
student_info["Percentage"] = percentage

print("Student's Info: ")

for key, value in student_info.items():
    print(f"{key} : {value}")
# =============================================================================================================================================== #

"""LAQ: Write a Program to find Number of Occurrences 
        of each Vowel present in the given String?"""

userWords = input("Enter any sentence to count how many vowels are in the sentence: ").lower()

vowelCount= {"a":0, "e":0, "i":0, "o":0, "u":0}

for char in userWords:
    if char in vowelCount:
        vowelCount[char] = vowelCount[char] + 1

print("Vowel Occurences: ")

for vowel, count in vowelCount.items():
    print (f"{vowel} : {count}") 

# =============================================================================================================================================== #
Q: What is the output of below code

dictlang = { 'c ': 6, 'GO': 89, 'flython': 4, 'Rust':10 } 
for _ in sorted(dictlang): 
    print (dictlang[_])

# =============================================================================================================================================== #
"""LAQ: Discuss how to access dictionary items. 
        Illustrate the use of get ( ), keys (), values( ), items( ) 
        in dictionary with suitable example program """

brainrot = {"a" : 10, "b" : 69, "c" : 74, "d" : 10}
print(brainrot)

# get() Method:
print(brainrot.get('a'))
print(brainrot.get('z'))

# keys() method:
print(brainrot.keys())

# values() method:
print(brainrot.values())

# items() method:
print(brainrot.items())
# =============================================================================================================================================== #
LAQ :Explain the concept of 
     traversing dictionary elements with suitable example program

CSE_B_students = {
    "brainrot" : [85, 90, 50, 20],
    "Nigga" : [69, 77, 55, 69],
    "GigaChad" : [99,89,96, 75]
}

print("Keys: ")
for key in CSE_B_students:
    print(key)

print("Values: ")
for values in CSE_B_students.values():
    print(values)

print("Keys:Values: ")
for keys, values in CSE_B_students.items():
    print(f"Key:{keys} : Value{values}")
# =============================================================================================================================================== #
"""LAQ: a) Illustrate the following Set methods with an example. 
        1) intersection () 2) union() 3) issubset() 4) difference() 
        5) update() 6) discard() 7)issuperset 8)remove() """

# 1. Intesection:
skibidi = {1, 2, 3, 69, 96, 666}
brainrot = {69, 700, 666, 545}
print(skibidi.intersection(brainrot))

# 2. Union:
skibidi = {"GOAT", "GYATT", "Shawty"}
brainrot = {"Rizzler", "Nigga", "Gigachad"}
print(skibidi.union(brainrot))

# 3. Subset:
skibidi = {1, 2, 3, 69, 96, 666}
brainrot = {69, 700, 666, 545}
print(skibidi.issubset(brainrot))

# 4. superset:
skibidi = {1, 2, 3, 4} 
brainrot = {2, 3} 
print(skibidi.issuperset(brainrot))

# 5. difference()
skibidi = {1, 2, 3, 69, 96, 666}
brainrot = {69, 700, 666, 545}
print(skibidi.difference(brainrot))

# 6. update():
skibidi = {1, 2, 3, 69, 96, 666}
brainrot = {69, 700, 666, 545}
skibidi.update(brainrot)
print(skibidi)

# 7. discard():
brainrot = {"Rizzler", "Nigga", "Gigachad"}
brainrot.discard("Nigga")
print(brainrot)

# 8. remove():
skibidi = {"GOAT", "GYATT", "Shawty"}
skibidi.remove("Shawty")
print(skibidi)
# =============================================================================================================================================== #
"""LAQ: Write a program that creates a dictionary of radius 
        of a circle and its circumference."""

circle_data = {}

radii = [1, 2, 3, 4, 5]

for radius in radii:
    circumference = 2*3.14*radius
    circle_data[radius] = round(circumference, 2)

print(circle_data)

print("Radius and circumference Dictionary:")
for radius, circumference in circle_data.items():
    print(f"Radius: {radius}, Circumference: {circumference}")

# =============================================================================================================================================== #
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "Your_username",
    password = "your_password"
)

cursor = conn.cursor()

cursur.execute("SHOW DATABASES")
databases = cursor.fetchall()

print("Databse Available: ")
for db in databases:
    print(db[0])

cursor.close()
conn.close()
# =============================================================================================================================================== #
'''SAQ: List out steps to connect Python with MySQL. Steps to 
        Connect Python with MySQL'''
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

databases = cursor.fetchall()

for dc in databases:
    print(dc[0])

cursor.close()
conn.close()
# =============================================================================================================================================== #
"""SAQ: Write a python snippet to Delete a 
        table,explain with example?"""

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost", 
    user = "your_user",
    password = "ypur_password"
)

cursor = conn.cursor

cursor.execute("DROP TABLE IF EXISTS students")

conn.commit()
cursor.close()
conn.close()

# =============================================================================================================================================== #
"""SAQ: Write a python snippet to Truncate a table,
        explain with example?"""

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user  = "Your_user",
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("TRUNCATE TABLE students;")

conn.commit()
cursor.close()
conn.close()

# =============================================================================================================================================== #
"""SAQ:Write a python snippet to 
        Drop a table,explain with example?"""

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost", 
    user = "your_user",
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS gigganigga;")

conn.commit()
cursor.close()
conn.close()
# =============================================================================================================================================== #
#data defination command (DDL)

CREATE TABLE employees(
    id INT PRIMARY KEY, name VARCHAR(50), salary DECIMAL(10, 2)
);

ALTER TABLE employees ADD COLUMN department
VARCHAR(50);
# =============================================================================================================================================== #
"""SAQ: Write a python snippet to CREATE DATABASE Using MySQL? 
        Python Snippet to Create a Database:"""

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS brainrot;")

cursor.close()
conn.close()
# =============================================================================================================================================== #
"""SAQ: Write a python snippet to DISPLAY DATABASE Using MySQL? 
        Python Snippet to Display Databases::"""

import mysql.connector
conn = myslq.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES;")

databases = cursor.fetchall()

for db in databases:
    print(db[0])

cursor.close()
conn.close()

# =============================================================================================================================================== #
"""SAQ: Write a python snippet to DROP DATABASE Using MySQL? 
        Python Snippet to Drop a Database:"""

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost", 
    user = "your_user", 
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("DROP DATABASE brainrot;")

conn.commit()
cursor.close()
conn.close()
# =============================================================================================================================================== #
#Data manipulation commands (DML)
INSERT INTO giganigga (id, name, age) VALUES (1, "Rizzler", 69);

UPADTE giganiggas SET age = 21 WHERE id = 1;
# =============================================================================================================================================== #
import mysql.connect

conn = mysql.connector.connect(
    host = "localhost", 
    user = "your_user", 
    password = "your_password"
    database = "your_database"
)

cursor = conn.cursor

cursor.execute("SELECT DATABASE()")

result=cursor.fetchone()

print ("Connected tod database: ", result)

cursor.close()
conn.close()
# =============================================================================================================================================== #
"""LAQ: Following Python code show how to use DELETE 
        statement to delete any record?"""

import mysql.connect

conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM students WHERE id = 1;")

conn.commit()
cursor.close()
conn.close()
# =============================================================================================================================================== #
"""LAQ: Update existing records in a table by using the
        "UPDATE" statement?"""

import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user", 
    password = "your_password"
)

cursor = conn.cursor

cursor.execute ("UPDATE gigganigga SET age = 21 WHERE id = 1;")

conn.commit()
cursor.close()
conn.close()
# =============================================================================================================================================== #
"""LAQ: Write a Python programme, 
        show how to use ALTER TABLE using MySQL?""" 

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password",
    database = "your_database"
)

cursor = conn.cursor()

cursor.execute("ALTER TABLE Gigachad ADD COLUMN VARCHAR(5);")

conn.commit()
cursor.close()
conn.close()
# =============================================================================================================================================== #
"""LAQ: Write a Python programme, 
        show how to use RENAME TABLE using MySQL?""" 

import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password",
    database = "your_database"
)

cursor = conn.cursor()

cursor.execute("RENAME TABLE gigachad TO sigmamale;")

conn.commit()
cursor.close()
conn.close()
# =============================================================================================================================================== #
"""LAQ: Write a Python program to CREATE and DISPLAY 
        database using MySQL?""" 

import mysql.connect
conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user", 
    password = "your_password",
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS brainrot")

print ("Database "brainrot"created succesfully")

cursor.execute ("SHOW DATABASEs:")

print("database:")
for db in cursor:
    print(db[0])

cursor.close()
conn.close()
# =============================================================================================================================================== #
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "your_user",
    password = "your_password"
    database = "your_database"
)

cursor = conn.cursor

cursor.execute("CREATE TABLE IF NOT EXISTS nigga(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    marks INT
);")

print ("Table "nigga" has created sucessfully")

insert_query = "INSERT INTO nigga(name, age, marks) VALUES (%s, %s, %s)"
values = [
    ("Alice", 20, 85)
    ("Sigma", 69, 69)
    ("Alpha", 20, 90)
]

cursor.execute(insert_query, values)

conn.commit()
print("Values inserted into the "nigga" table")

update_query = "UPDATE nigga SET marks 95 WHERE name="Sigma";"

cursor.execute (update_query)

conn.commit()

print("Data updates succesfully")

cursor.execute("SELECT * FROM nigga;")
print ("Table 'student'content")
for row.in cursor.fetchall():
    print(row)

cursor.close()
conn.close()

# =============================================================================================================================================== #
"""LAQ: Explain in details Database Errors 
        using Python Programming?"""

import mysql.connector

from mysql.connector import Errors

try:
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Password",
        databas = "your_database"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT FROM niggas")

except mysql.connector.ProgrammingError as ie:
    print("Connecting Error", ie)
except Error as e:
    print("Database Error;", e)

finally:
    if connection.is_connected():
        cursor.close()
        conn.close

# =============================================================================================================================================== #
import numpy as np

python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)

print (numpy_array)
# =============================================================================================================================================== #
LAQ: What is the purpose of the drop () method in Pandas?

import pandas as pd 
data = {"Name":["Alice", "Bob", "Charlie"], "Age":[25, 30, 35]}
df = pd.DataFrame(data)

df_dropped_column = df.drop(1, axis=0)
df_dropped_row = df.drop(1, axis=0)

print(df_dropped_column)
print(df_dropped_row)
# =============================================================================================================================================== #
import numpy as np

arr = np.arr([10, 20, 30, 40, 50])

second_element=arr[1]
print(second_element)
# =============================================================================================================================================== #
import pandas as pd

data = {
    "Name" : ["John", "Alice", "Bob", "Charlie"],
    "Age" : [55, 20, 10, 12],
    "score" : [100, 89, 10, 30]
}

df = pd.DataFrame(data)

print (df. describe())
print("Mean Age:", df['Age']. mean())
print("Total score", df["score"]. sum())
# =============================================================================================================================================== #

s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

result = s1 + s2
print (result)

# =============================================================================================================================================== #

s1 = pd.Series([10, 20, 30], index=["a", 'b', 'c'])
s2 = pd.Series([5, 15, 25, 35], index=["b", "c", "d", "e"])

result = s1 + s2
print(result)
print (s1)
# =============================================================================================================================================== #
import pandas as pd

df1 = pd.DataFrame({
    "A" : [1, 2],
    "B" : [3, 4]
}, index = ["a", "b"])

df2 = pd.DataFrame({
    "B" : [5, 6],
    "C" : [7, 8]
}, index=['b', 'c'])

result = df1 + df2

print(result)
print("\n")
print(df1)
print("\n")
print(df2)
# =============================================================================================================================================== #
import numpy as np

arr = np.array([[1, 2, 3, ], [2, 3, 4], [3, 4, 5]])
value = arr[1,2]
print(value)