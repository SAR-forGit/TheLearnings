def welcomer(a):
    print ("="*70)
    print ("\n"*4)

    print (" "*20, "="*30)
    print ("Days With Python".center(70))
    print (a.center(70))
    print ("~SAR".center(90))
    print (" "*20, "="*30)

    print ("\n"*4)
    print ("="*70)

    print("\n")

date = "29 November 2024"
welcomer(date)

###################################################################################################################
# # # dayA={"mon","tue","wed","thur"}


# # # dayB={"mon","sun","tue","wed","thur"}


# # # subset=dayA<=dayB


# # # superset=dayB>=dayA
# # # print(subset)
# # # print(superset)



# # # Subset=dayA.issubset(dayB)


# # # Superset=dayB.issuperset(dayA)


# # # print(Subset)


# # # print(Superset)


# # x=set()


# # x.add("abc")


# # x.add("def")


# # x.update(["aaa","bbb"])


# # print(x)


# list=[-10,-20,-30,40,-50]



# if all([abs(i)<0 for i in list]):


#     print("Hi")


# else:


#     print("bye")


# dayA={"mon","tue","wed","thur"}


# dayB={"mon","sun","tue","wed","thur"}

############################################



FirstName = 'Syed'


SecondName = 'Abdur'


LastName = 'Rasheed'



print (FirstName + SecondName + LastName)


print ("First Name is:", end=" ")


print (FirstName, end= " ") 


print ("Other half Name is: " + SecondName + LastName)

print (" ")


############## Comments #####################



"""print ("FirstName)"""



########## Type of and complex ##############



aComplex, AnotherComplex, YetAnotherComplex = 33+3j, complex(47, 54), complex(77) #Only 'J' is working



print (aComplex)


print (type(aComplex))


print (aComplex.real) #this will display real


print (aComplex.imag) #this will display Imaginary



print (AnotherComplex) #Declared using complex function


print (YetAnotherComplex) #If another value isn not given then it will assign it as 0

print (" ")


################ Boolean ##################



a, b = True, False #here T is capital letter 
print(a) 


print(type(a)) 
print (b)



print (3==100)

print (" ")


################ Arrays, Tuple & Sets ##################



AnArray = [10, 20, 100, 'ThisIsAnArray']


aTuple = (10, 20, 100, "ThisIsATuple")


aSet = {10, 20, 100, "ThisIsASet"}



print (AnArray)


print (aTuple)


print (aSet)



print (end='\n')


################ Dictionary ##################



aDict = {"FirstName":"Syed", "Age":20, "FullName":"Syed Abdur Rasheed"}


#FirstName, FullName & Age are called Keys whereas Syed, 20 & Syed Abdur Rasheed are values


print (aDict.get("FullName"))


print (aDict.get ("Age"))
print (" ")


print ("Full Info: ")


print (aDict)

print (" ")


############## Input function ##################


# Name = eval(input ("Name"))



# print (Name)


# print (type(Name))



############## Sep Parameter ##################


string1, string2 = "Happy", "Birthday"



print (string1, string2)


print (string1, string2, sep=("")) #For No spaces between


print (string1, string2, sep= "! ") #For Exclamation mark in between

print (" ")


############## id (formaly known as pointer) ##################



aVariable =  'ChintukleMuntukle' #There is nothing like pointer in python but if want to find an address of a variable then we use id
print (id(a))



print (end="\n")


############## cmp ##################


# a, b = 10, 20


# print (cmp(a,b))


# #cmp is not in python 3


#btw if a<b = -1, a>b = 1, a=b = 0;


############## str(), repr(), type() ##################



aVariable = "Python"



print (aVariable)


print (type(aVariable))


print (str(aVariable))


print (repr(aVariable))


print (type(str(aVariable)))



print (' ')


############# Arithmetic Operator ##################

a, b = 3, 5

print ("Arithmetic Addition", + a+b) #Arithmetic Addition

print ("Arithmetic Subtraction", + a-b) #Arithmetic Subtraction

print ("Arithmetic Multiplication", + a*b) #Arithmetic Multiplication

print ("Arithmetic Power", + a**b) #Arithmetic Power

print ("Arithmetic Division (Float)", + a/b) #Arithmetic Division (float)

print ("Arithmetic (Floor)", + a//b) #Arithmetic Division (floor)

print ("Arithmetic Remainder", + a%b) #Arithmetic Remainder

print (" ")
############# Compressional Operator ##################


a, b = 10, 20



# Compressional Operator prints true or false accordingly 


print ("a is greater than b:", a>b)


print ("a is smaller than b:", a<b)


print ("a is equals to b:", a==b)


print ("a is not equals to b:", a!=b)


print ("a is greater than or equal to b:", a>=b)


print ("a is smaller than or equals to b:", a<=b)

print (" ")


############# Logical Operators ##################


a, b = 50, 70



print ((a>b) and (a<b))


print ((a>b) or (a<b))


print (not(a>b) and (a<b))


print (not(a>b) or (a<b))

print (" ")


############# Assignment Operators ##################


a = 3 


b = 5 



a += b # a = a + b 


a -= b 


a *= b 


a **= b 


a /= b 


a //= b 


a %= b 


# a &= b 


# a |= b 


# a ^= b 


# a >>= b 


# a <<= b

print(" ")


############# Bitwise Operators ##################


a, b = 5, 6


print (a&b)

print (a|b)

print (a^b)

print (a>>b)

print (a<<b)

print (" ")

############# identity Operators ##################

a, b = "Abdur", "ABDUR"

print (a is b)
print (a is not b)


a = b = 10

print (a is b)
print (a is not b)

print (" ")

############# Membership Operators ##################

a = "My Name Is Syed Abdur Rasheed"


print ("Abdur" in a)

print ("ABDUR" in a)

print (" ")

############# Conditional Statements ##################


a = int(input("Write the value of a"))

b = eval(input("Write the value of b"))


if (a == b):

    print ("a is equals to b")

else:

    print ("a is not equals to b")

print (" ")

############# Example code: even or odd ##################


usersNumber = int(input("Enter a number to check whether its odd or even: "))


if (usersNumber % 2 == 0):

    print ("even")

else:
    print ("odd")

print (" ")


############# elif Code ##################


VotersAge = int(input("Enter your age to check whether you are eligible or not: "))


if ((VotersAge>17) & (VotersAge<89)):

    print ("You are Eligible for Voting\nHappy Voting")

elif (VotersAge>89):

    print ("You aint dead already?")

else:

    print ("You are not eligible for voting\nSad Voting")

print (" ")

############# Example of nested if Code ##################

a = int (input("Enter a number for a"))

b = int (input("Enter a number for b"))


if (a>=b):

    if (a>b):

        print ("a is greater")

    else:

        print ("both are equal")

else:

    print ("b is greater")

print(" ")

########################## While ###########################

a = 1

b = int(input("Enter a number to print till: "))


while (a<b):
    print (a)

    a = a+1

print (" ")

########################## Example of While ###########################

Password = 12345

Input_password = int(input("Enter password:")) 

while password != input_password: 

    Input_password=input("enter password:") 

else: 

    print ("unlocked!!!!!!!!!") 


########################## for loop ###########################

b = int(input("Enter the value of b: "))


for a in range (1, b+1):
    print (a)

print (" ")

################ for loop with 1 range value ####################

b = int(input("Enter the value of b: "))


for a in range (b+1):
    print (a)

print (" ")

######################### For loop example 1 ####################

givenNum = int(input("Enter a number to print table of: "))

print ("The table for", givenNum, "is:\n")
for i in range (1, 12+1):

    print (givenNum, "x", i, "=", givenNum * i)

print (" ")
######################### For loop example 2 ####################

givenNum = int(input("Enter a number to print table of: "))

print ("The table for", givenNum, "is:\n")
for i in range (1, givenNum+1):
    for j in range (1, 12+1):
        print (i, "x", j, "=", givenNum * j)
    print ("\n")

print (" ")
######################### Continue statement ####################

givenNum = int(input("Enter a number to print odd numbers till: "))

for i in range (1, givenNum+1):
    if (i%2==0):
        continue
    else:
        print (i)

print (" ")
######################### pass statement ####################

if "a" in "India":
    pass

print (" ")
######################### function ####################

def HelloPrinter():
    print ("Hello")

HelloPrinter()
HelloPrinter()
HelloPrinter()
HelloPrinter()
##################### Functions example ####################
def ArithmeticFun(a, b):    
    print ("Arithmetic Addition", + a+b) #Arithmetic Addition

    print ("Arithmetic Subtraction", + a-b) #Arithmetic Subtraction

    print ("Arithmetic Multiplication", + a*b) #Arithmetic Multiplication

    print ("Arithmetic Power", + a**b) #Arithmetic Power

    print ("Arithmetic Division (Float)", + a/b) #Arithmetic Division (float)

    print ("Arithmetic (Floor)", + a//b) #Arithmetic Division (floor)

    print ("Arithmetic Remainder", + a%b) #Arithmetic Remainder

givenNum1, givenNum2 = int(input("Enter a value to see its all arithmetic operations: ")), int(input("\nEnter second value to see its all arithmetic operations to be done with:"))

ArithmeticFun(givenNum1, givenNum2)

print (" ")
##################### Functions example ####################
def NameWelcomer(ism):
    print ("Welcome to Python", ism, sep=" ")

Name = str(input("Enter your name: "))

NameWelcomer(Name)

print (" ")
##################### return statement ####################
def adder(a, b):
    return a+b

givenNum1, givenNum2 = int(input("Enter first number to add it: ")), int(input("Enter second number to add it with: "))

sum = adder(givenNum1, givenNum2)

print (sum)

print (" ")
############## return statement example 1 #################

def NamerCaller(naam):
    return "My Name is" #Note how Name is not getting printed because after return statement nothing got executed
    print (naam)

Name = str(input("Enter your name:"))

NamerCaller(Name)

print (" ")
############## 1. Positional Argument #################

def data(name, rollno): 
    print("my name is:",name,"my roll no is :", rollno) 
data("SAR", 118) 
data(118, "SAR")

print (" ")
############## 2. Keywords Argument #################

def student(name, rollno, secson): 
 print('Student Details:', name, rollno, secson) 

student(rollno=118, secson="B",name='SARtheGreat') 

print (" ")
############## 3. Default Argument #################

# function with keyword arguments i.e., section 

def student(name, rollno , section="B"): 
    print("Student Details:\nName: ", name,", Roll Number: ", rollno,", Section: ", section, sep="") 
 
# without passing section Passing only the mandatoryarguments 
student('SAR', 118 )
student ("Raoul", 1, "Rockstar") #It will overwrite Shadaan in place of B for section
student('SAR', 118 ) #It returns Section as B as no value is passed

print (" ")
#####################################################################

def CheckSahab(Checku):
    for item in Checku:
     print (item, end=" ")

Names = ("Me", "Abba", "Mummy", "Sha", "ZZ")
CheckSahab(Names)

print (" ")
################### Lambda Functions (or) Anonymous Function ################################
def double(changu):
    return x*2

#They Both are equal

Double = lambda changu: changu*2 

#Instead of writing in 2 lines we can execute in 1 line

givenNum = int(input("Enter a number to print it's double"))
print (Double(givenNum))

#Another Example 

AverageMuntu = lambda Muntu, Chintu: int(( Muntu*Chintu ) / 2)

print (AverageMuntu (10, 20))

#Lambda Function can also take multiple inputs

print (" ")
################### Function Recursion ################################
def Name():
    print ("SAR")
    Name()

Name()

#Warning Infinite recuriosn
print (" ")
############## Q. Factorial Using Recursion #####################

def factorial(x):
    if (x==1):
        return 1
    else:
        return x * factorial(x-1)

givenNum = int(input("Enter a number to find its factorial: "))

print ("The Factorial of", givenNum, "is", factorial(givenNum))

print (" ")
############## Factorial Using Recursion #####################
a=eval(input("enter no:")) 
print(a) 

######################### Exec() ###################################
#exec() runs Python code dynamically. 
exec('a=2;b=3;print(a+b)') 

######################### Hex() ###################################
#Hex() Python built-in functions, converts an integer to hexadecimal. 
hex(16)

######################### id() ###################################
#id() returns an object’s identity(address).
orange = 10 
print (id(orange))

######################### len() ###################################
#We’ve seen len() so many times by now. It returns the length of an object. 
an_array = (10, 20, 50, 70)

print (len(an_array))
######################### max() ###################################
#max() returns the item, in a sequence, with the highest value of all. 
an_array = (10, 20, 50, 70)

print (max(an_array))
######################### min() ###################################
#min() returns the item, in a sequence, with the smallest value of all.
an_array = (10, 20, 50, 70)

print (min(an_array))
######################### pow() ###################################
#pow() takes two arguments- say, x and y. It then returns the value of x to the power of y. 
x, y = 2, 3

print (pow(x, y))
######################### pow() ###################################
#repr() returns a representable string of an object. 
repr("Hello") 

######################### sorted() ###################################
#Like we’ve seen before, sorted() prints out a sorted version of an iterable. It does not, however, alter the iterable. 
sorted('Python') 

######################### sum() ###################################
#The function sum() takes an iterable as an argument, and returns the sum of all values. 
sum([3,4,5]) #We can add with only an array 
sum ([10, 2, 3], 3) #We can add using combination of an array ands single element
######################### type() ###################################
#We have been seeing the type() function to check the type of object we’re dealing with. 
a = 10
print (type(a)) 
######################### other functions ###################################
#   int(), float(), str(), complex( ), list ( ) , tuple ( ) , set ( ) 

print(int(10.5)) #converting float value to int 
print(int("10")) #converting string to int
print(float(10)) #converting int to float 
print(float("10.5")) #converting string to float
print(str(10))  #converting int to str
print(str(10.5)) #converting float to str 
print(complex(1,2.3)) #converting int and float numbers to complex
print(list((1,2.4,"btech")))  #converting tuple to list     
print(tuple([1,2.4,"btech"]))  #converting list to tuple 
print(set([1,2.4,"btech"])) #converting list to set

################################ string arrays #######################################
aVariable = "Hello Chicha"

print (aVariable[0])
print (aVariable[1])
print (aVariable[2])
print (aVariable[3])
print (aVariable[4])
print (aVariable[5])
print (aVariable[6])
print (aVariable[7])
print (aVariable[8])
print (aVariable[9])
print (aVariable[10])

print (" ")
################################ print string arrays variables using loop #######################################
aVariable = "Hello Chicha"

for x in aVariable:
    print (x)

print (" ")
################################ print string length #######################################
aVariable = "Hello Chicha"

print (len(aVariable))

print (" ")
################################ Q: To check whether certain alphabet/word is in the word/sentence #######################################
def CharChecker(word, character):
    if character in word:
        print ("Yes it's in the word/sentence")
    else:
        print ("No, Sorry, It's not in the word/sentence")

givenWord = str(input("Write a word or sentence: "))
givenChar = str(input("Enter a alphabet/wod to find to in the word/sentence: "))

CharChecker (givenWord, givenChar)

print (" ")
################################ String slicing #######################################
print ("Enter your name to get its initials:")
firstName, middleName, LastName = str(input("Enter a First Name")), str(input("Enter a Middle Name")), str(input("Enter a Last Name"))

print ("Your Names initials are:\n", firstName[0:1], middleName[ :1], LastName[0:1])

print (" ")
################################ Reverse (Negative Indexing) #######################################
print ("Name Reverser: ")
Name = str(input("Enter a Name to reverse it:"))

reverser = Name[ ::-1]
print (reverser)

print(" ")
################################ UpperCase and Lowercase #######################################
print ("Mix Cases to Lowercases and Uppercases:")
Name = str(input("Enter a name: "))

print (Name.lower())
print (Name.upper())

print (" ")
################################ Strip #######################################
print ("remove the blank spaces from starting and end")
givenSentence = str(input("Enter a sentence: "))

print ("Normal Sentence:", givenSentence, end="\n")
print ("Stripped Sentence:", givenSentence.strip())


print (" ")
################################ the replacer #######################################
givenWord = ("Niggesh")

changed = givenWord.replace("i", "a") 

print (changed.replace("g", "r"))
################################ the replacer example 2 #######################################
givenWord = ("Niggesh")

print (givenWord.replace("g", "r", 1))

print (" ")
################################ string concatenation #######################################
HelloPrinter = "Hello"
Name = str(input("Enter your name: "))
niggaPrinter = "Nigga"

print (HelloPrinter + niggaPrinter + Name, sep=" ")

print (" ")
################################ string format #######################################
Name = str(input("Enter your name"))
NameWelcomer = 'Hi there {} niggesh'

print (NameWelcomer.format(Name))

print (" ")
################################ string format #######################################
givenSentence = "Then he said: \"I'm so sad\" with tears "
print (givenSentence)

print (" ")
################################ string comparison #######################################
a="hyderabad" 
b="india" 
print( a is b) 
print( a is not b) 
print(a==b) 
print(a!=b) 
print (a>b)
print (a<b)

print (" ")
################################ list #######################################
theList, theNumList = [1, "Argue", "b", "Argue", 0.05], [1, 2, 5, 0.05]

print (len(theList))
print (max(theNumList))
print (min(theNumList))
print (theList, theNumList)
print (theList[1])
theList.append ("Argue")
print (theList)

print (" ")
################################ Replace an item from list #######################################
theList, theNumList = [1, "Argue", "b", "Argue", 0.05], [1, 2, 5, 0.05]
theList[3] = "Latin"
print (theList)
print (theList[3])
#replacing multiple items
theList [0:2] = ["One", "aWord", "Bee", "LetsSee"]
print (theList)
print (theList[3])

print (" ")
################################ remove, pop, del #######################################
#using remove
theList = [1, "Argue", "b", "Argue", 0.05]
theList.remove("Argue")
print (theList)
theList.remove("Argue")
print (theList)

#using pop
theList = [1, "Argue", "b", "Argue", 0.05]
theList.pop(1)
print (theList)

#using del
theList = [1, "Argue", "b", "Argue", 0.05]
del theList[1]
print (theList)

print (" ")
################################ count(), index() #######################################
theList = [1, "Argue", "b", "Argue", 0.05]
print (theList.count("Argue"))
print (theList.index("Argue"))

print (" ")
################################ copy #######################################
theList = [1, "Argue", "b", "Argue", 0.05]

theNumList = theList.copy()
print (theNumList)

theThirdList = theList[ : ]
print (theThirdList)

print (" ")
########################### Copy if word starts with a ################################
theList = [1, "Argue", "b", "Argue", 0.05]

# theNumList = word for word in theList if word.starts with ("A")

################################ Unpacking #######################################
Names = ["Abba", "Mummy", "Sha", "Me"]
Name1, Name2, Name3, Name4 = Names #If adding one more variable will give an error
print (Name1)
print (Name2)
print (Name3)
print (Name4)

print (" ")
################################ sort(), reverse() #######################################
theNumList = [2, 3, 5, 7, 4, 8, 9, 1, 10]

theNumList.sort()
print (theNumList)

theNumList.reverse()
print (theNumList)

#or

theNumList = [2, 3, 5, 7, 4, 8, 9, 1, 10]

theNumList.sort(reverse=True)
print (theNumList)

print(" ")
################################ Tuple #######################################
aTuple = (1, 5.8, "Charger", "B")
aList = [1, 5.8, "Charger", "B"]

print(type(aTuple))
print(type(aList))

#finding in tuple
print (aTuple.index("B"))
print (aTuple.count("B"))

#Copying a tuple
AverageMuntu = aTuple
print (AverageMuntu)

aTuple = tuple(("Juice", "Pila", "do", "Mosambi", "ka")) #Another way of initializing a tuple
print (aTuple)
" We cannot perform append(), insert(), pop(), because we cannot perform any changes in Tuple once we create Tuple because they're immutable "

################################################################# Sets ###############################################################################
#   Sets are used to store multiple items in a single variable. 
#   Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc. 
#   Set are represented by { } 
 
aSet = {"Apple", "Banana", "Orange"}

print(aSet) 
print(type(aSet)) 
print(len(aSet)) 

#• The elements in the set cannot be duplicates. 
#• The elements in the set are immutable(cannot be modified) but the set as a whole is mutable. 
#• There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

aSet = set(("Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka")) #another way of initializing set
print (aSet)
print (type(aSet))

#   In above example "Mosambi" is repeated twice but it will not allow duplicates, so it will display “Mosambi” only once.
#   Also is unordered
#   Also is unchangeable

aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
for x in aSet: 
    print(x) 

#   To check if "Mosambi" is in the set
aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
print ("Mosambi" in aSet)
print ("Orange" in aSet)

#   Once a set is created, you cannot change its items, but you can add new items. To add one item to a set use the add() method. 
#   To remove an item in a set, use the remove(), or the discard() method. 
aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
aSet.add("Orange")
aSet.remove("Mosambi") #Note: If the item to remove does not exist, remove() will raise an error.
aSet.discard("Juice") #Note: If the item to remove does not exist, discard()will NOT raise an error. 

print (aSet)

#   To add items from another set into the current set, use the update() or union() method. 
aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
aTuple = (1, 5.8, "Charger", "B")

aSet.update(aTuple) #The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.). 
print (aSet)

aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
aTuple = (1, 5.8, "Charger", "B")

aSet2 = aSet.union(aTuple)  
print (aSet2)

" Note: Both union() and update() will not include any duplicate items "

#   The del keyword will delete the set completely:
aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
print (aSet)
del aSet
#   print (aSet) #this will raise an error because the set no longer exists 

" You can also use the pop() method. Sets are unordered, so when using the pop() method, you do not know which item that gets removed.so don't use pop() method in sets. "

#   The intersection() method will return a new set, that only contains the items that are present in both sets. 
aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
aSet2 = {"Chin", "tapak", "Dum", "Mosambi", "Dum", "ka"}

a = aSet.intersection(aSet2)
print (a)

aSet.intersection_update(aSet2)
print (aSet)

#   The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets. 
aSet = {"Juice", "Pila", "do", "Mosambi", "ka", "Mosambi", "ka"} 
aSet2 = {"Chin", "tapak", "Dum", "Mosambi", "Dum", "ka"}

a = aSet.symmetric_difference(aSet2)
print (a)

aSet.symmetric_difference_update(aSet2)
print (aSet)

################################################################# Dict ###############################################################################
aDict={"Name": "SAR", "rollno": "160923733118", "age": 20} #Dictionaries cannot have two items with the same key: 
print(aDict) 
print(len(aDict)) 
print(type(aDict)) 

aDict={"Name": "SAR", "Name": "SAR","rollno": "118","age": 20,"age": 20} 
print(aDict) # “age” repeated twice but it will print only one key with is given at last so you will get output “key”:21

aDict = dict({"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}) #another way of initializing 
print(aDict["Name"]) 
#or
print (aDict.get("Branch"))

print (aDict.keys()) #The keys() method will return a list of all the keys in the dictionary.
print (aDict.values()) #The values() method will return a list of all the values in the dictionary.
print (aDict.items()) #The items() method will return each item in a dictionary, as tuples in a list

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}

aDict["Name"] = "Sha"
aDict["Branch"] = str(input("Enter your Branch: ")) #Taking Input from user 

print (aDict)
print (aDict.items())

#Q: To check if keys are present in Dict
aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}

if "Name" in aDict:
    print ("Yes, it's in there")
else:
    print ("No, It's Not there")

#   Q: Practice Code
aDict = {"Name" : " ", "Branch" : "", "Section" : ""}
aDict["Name"] = str(input("Enter your name: "))
aDict["Branch"] = str(input("Enter your Branch: "))
aDict["Section"] = str(input("Enter your Section:"))

if aDict["Name"] is "" or " ":
    print ("Please Enter your name")

#####   Update
aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B"}
aDict.update ({"Roll No": 118})
print (aDict)

#####   Ways to Remove
aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
aDict.pop("RollNo")
print (aDict)

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
aDict.popitem()
print (aDict)

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
del aDict["Name"]
print (aDict)

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
del aDict
print (aDict) #will print error cause aDict is deleted

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
aDict.clear()
print (aDict) 

### Printing through a loop
aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}

for x in aDict:
    print (x)

print ("\n")

for x in aDict:
    print (aDict[x])

" You cannot copy a dictionary simply by typing dict2 = dict1, "
" because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2. "  
" There are ways to make a copy, one way is to use the built-in Dictionary method copy(). "

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
aDict2 = aDict.copy()

print (aDict)
print (aDict2)

#or

aDict = {"Name": "SAR", "Branch":"CSE", "Section":"B", "RollNo":118}
aDict2 = dict(aDict)

print (aDict)
print (aDict2)

### Nested Dictionary

aDict = {118 : {"Name" : "SAR", "Branch" : "CSE"}, 106 : {"Name":"Zade", "Branch":"CSE"}}

print (aDict)

#or

RollNo118 = {"Name":"SAR", "Branch":"CSE", "Section":"B"}
RollNo106 = {"Name":"ZADE", "Branch":"CSE", "Section":"B"}

aDict = {118:RollNo118, 106:RollNo106}

print(aDict)

############################################## special literals ############################################################
a = None
print (a)

print (" ")
############################################## slice ############################################################
aList = ("a", "b", "c", "d", "e", "f", "g")

a = slice(2, 5)
print (a)
print (aList[a])

############################################## Q: To Print Natural Numbers ############################################################
givenNum = int(input("Enter a number to print till"))

for x in range(1, givenNum+1):
    print (x)

############################################## Q: Area of Rectangle ############################################################
print ("Rectangle Area Calculator:")
length = int(input("Enter value for length: "))
width = int(input("Enter value for Width: "))

areaCalculator = length * width

print ("Area of your rectangle:", areaCalculator)

print(" ")
############################################## Q: Area of Square ############################################################
print ("Square Area Calculator:")
side = int(input("Enter value for side: "))

areaCalculator = side * side

print ("Area of square is: ", areaCalculator)

print (" ")
############################################## Q: Area of Circle ############################################################

print ("Circle Area Calculator:")
radius = int(input("Enter value for radius: "))

areaCalculator = 3.14 * radius * radius

print ("Area of circle is: ", areaCalculator)

print (" ")
############################################## Q: Square root ############################################################
print ("Square Root:")
a = int(input("Enter value for square root: "))

squareRooter = a * 0.5

print ("square root is: ", squareRooter)

print (" ")
####################################### Q: Program to find Maximum of two numbers ####################################################
a = int (input("Enter 1st value: "))
b = int (input("Enter 2nd value: "))

if a>b:
    print (a, "is greatest")
else:
    print (b, "is Greatest")

print (" ")
####################################### Q: Program to find Greatest among three numbers ####################################################
a = int (input("Enter 1st value: "))
b = int (input("Enter 2nd value: "))
c = int (input("Enter 3rd value: "))

if a>b and a>c:
    print (a, "is greater than", b, "and", c)
elif b>c and b>a:
    print (b, "is greater than", a, "and", c)
else:
    print (c, "is Greater than", a, "and", b)

print (" ")
############################################## Q: Python Program to find the area of triangle #####################################################
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is ", area)

print(" ")
############################################## Q: Swap two Numbers #####################################################
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))

print ("Before Swap:")
print ("a=", a, "b=", b)

a = a+b
b = a-b
a = a-b

print ("After Swap:")
print ("a=", a, "b=", b)

print (" ")
############################################## Q: GCD ############################################################
x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))

if x > y:
        small = y

else:
        small = x

for i in range(1, small + 1):
    if((x % i == 0) and (y % i == 0)):
        gcd = i

print ("The gcd is:", gcd)  

print (" ")

########################### Q: Program to find H.c.F of two numbers using functions and functions arguments ###################################
def hcf(a, b): 
    if(b == 0): 
	    return a 
    else: 
	    return hcf(b, a % b) 

a = 60 
b = 48 

print("The gcd of 60 and 48 is:", hcf(a, b))

print (" ")
###############################################################################################################################################
print (sum(range(1, 102)))

a= "Syed Abdur Rasheed"
print (a.split(" "))

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() with a lambda to get the squares
squares = list(map(lambda x: x ** 2, numbers))

# Printing the result
print(squares)

def recursive_sum(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            # If the element is a list, call the function recursively
            total += recursive_sum(element)
        else:
            # If it's a number, add it to the total
            total += element
    return total

# Example usage
example_list = [1, [2, 3], [4, [5, 6]], 7]
result = recursive_sum(example_list)
print("Sum of elements:", result)


# Define the string
my_string = "A, B, B, F, G, T, E, E"

# Calculate the length of the string
length_of_string = len(my_string)

# Print the length
print("Length of the string:", length_of_string)

################################################### Q: To reverse a number ################################################################
date = "29 November 2024"
welcomer(date)

def reverse_number(num):
    # Convert the number to a string and reverse it
    reversed_num = str(num)[::-1]
    return int(reversed_num)  # Convert back to integer

# Input from the user
number = int(input("Enter a number: "))

# Reverse the number
reversed_number = reverse_number(number)

# Display the result
print("Reversed Number:", reversed_number)

################################################################################################################################

my_list = [1, 5, 4, 6, 8, 11, 3, 12] 
new_list = list(filter(lambda x: (x%2 == 0) , my_list)) 
print(new_list) 

################################################################################################################################

#Write a Program to make a simple calculator using functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x-y

def multiply(x, y):
    x*y

def divide (x , y):
    return x/y

print("******************************Select an operation:****************************")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input())

if (choice == 1 or 2 or 3 or 4):
    num1 = float (input("Enter the first number: "))
    num2 = float (input("Enter the second number: "))

    if choice == 1:
        print (add(num1, num2))
    
    elif choice == 2:
        print (subtract(num1, num2))

    elif choice == 3:
        print(multiply(num1, num2))
    
    elif choice == 4:
        print (divide(num1, num2))
else:
    print ('invalid choice')

################################################################################################################################
try:  
    thislist = ["apple", "banana", "cherry"]  
    thislist.remove("orange")  
except:   
    print("Something went wrong") 
finally:   
    print("The 'try except' is finished")   
print(thislist) 

################################################################################################################################
  #Create a new file  
f = open("PPLab.txt", "w") 
  #Write to an Existing File #Open the file “PPLab.txt", and append content to the file: 
f = open("PPLab.txt",  "a") 
f.write("Hello World ! the file has more content!") 
f.close() 

################################################################################################################################
#Q: Python program to sort the elements of an array in ascending order and Descending order 

temp, arr = 0, [55, 69, 48, 250, 202, 570, 577]

print ("Original array: ")
for i in range (0, len(arr)):
    print(arr[i], end=" ")

print("\nSorted array in ascending order:")
for i in range (0, len(arr)):
    for j in range (i+1, len(arr)):
        if (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range (0, len(arr)):
    print(arr[i], end=" ")

print("\nSorted array in Descending order:")
for i in range (0, len(arr)):
    for j in range (i+1, len(arr)):
        if (arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for i in range (0, len(arr)):
    print(arr[i], end=" ")

################################################################################################################################
import random
num = random.randrange(1, 20, 2)
print (num)

import random
rand_string = random.choice("Nigga money")
print (rand_string)

rand_nums = random.choice([69, 77, 200, 6969, 540])
print (rand_nums)

rand_nums = random.choice((69, 77, 200, 6969, 540))
print (rand_nums)

rand_questions = random.choice(["Who the hell you think is nigga?", "Where teh fuck are my shoes?", "My balnket is so comfy?"])
print(rand_questions)

new_list = [69, 77, 200, 6969, 540]
random.shuffle(new_list)
print (new_list)

################################################################################################################################
import numpy as np
new_list = [69, 77, 200, 6969, 540]
arr = [79, 84, 57, 11, 100]
niggas = np.add(new_list, arr)
print (niggas)

import numpy as np
new_list = [69, 77, 200, 6969, 540]
arr = [79, 84, 57, 11, 100]
niggas = np.subtract(new_list, arr)
print (niggas)

import numpy as np
new_list = [69, 77, 200, 6969, 540]
arr = [79, 84, 57, 11, 100]
niggas = np.multiply(new_list, arr)
print (niggas)

import numpy as np
new_list = [69, 77, 200, 6969, 540]
arr = [79, 84, 57, 11, 100]
niggas = np.divide(new_list, arr)
print (niggas)

import numpy as np
new_list = [69, 77, 200, 6969, 540]
arr = [79, 84, 57, 11, 100]
niggas = np.power(new_list, arr)
print (niggas)
################################################### Classes and Objects ############################################################
class Lords_Student:
    college_name = "Lords institute of Engineering and Technology"
    Affliation = "OU Autonomous"
    def __init__ (self, name, rollNo, branch):
        self.name = name
        self.RollNumber = rollNo
        self.Branch = branch

class CMR_Student:
    college_name = "CMR College of Engineering and Technology"
    Affliation = "JNTU"
    def __init__ (self, name, rollNo, branch):
        self.name = name
        self.RollNumber = rollNo
        self.Branch = branch

class Shadaan_Student:
    college_name = "Shadaan College of Pharmacy"
    Affliation = "JNTU"
    def __init__ (self, name, rollNo, branch):
        self.name = name
        self.RollNumber = rollNo
        self.Branch = branch

s1 = Lords_Student("Saud", "083", "CSE")
s2 = CMR_Student("Mubtasim", "000", "CSE")
s3 = Lords_Student("Abdul Ahad", "106", "CSE")
s4 = Shadaan_Student("Sha", "025", "Pharm-D")

print (s1.name, s1.RollNumber, s1.Affliation, s1.Branch, sep = ", ")
print (s3.name, s3.RollNumber, s3.Affliation, s3.Branch, sep = ", ")
print (s2.name, s2.RollNumber, s2.Affliation, s2.Branch, sep = ", ")
print (s4.name, s4.RollNumber, s4.Affliation, s4.Branch, sep = ", ")
