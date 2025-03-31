#LECTURE1-------->>>__________________________________________
"""name= "Himangshu"
age =23
salary= 22500.66
print(type(name))
print(type(age))
print(type(salary))"""

#Variables and Data Types
"""A,B=2,3
Txt="@"
print(A*Txt*B)
name= input("name: ")
print(name)
age = int(input("age:"))
print(age)
price=  float(input("price: "))
print(price)"""

#WAP to print the sum of first n natural numbers in a pattern.
"""# Inputing Natural Number
number = int(input("Enter the Natural Number: "))

# j ranges from 1 to n
for j in range(1, number+1):

	# Initializing List
	a = []

	# i loop ranges from 1 to j
	for i in range(1, j+1):
		print(i, sep=" ", end=" ")
		if(i < j):
			print("+", sep=" ", end=" ")
		a.append(i)
	print("=", sum(a))

print()
"""
#WAP to print the power(input from user) of a num(input from user)
"""base_num = int(input("Enter a base num:"))
pow_num = int(input("Enter a power num:"))
result = (base_num**pow_num)
print(result)"""

#Swap two variables using traditional method and python method.
#Method 1:- traditional method
"""x=10
y=5
temp=0
temp=x #temporarily storing the value of x in temp
x=y #storing the actual value of y in x
y=temp#storing the actual value of x in y
print("After swapping x=",x)
print("after swapping y=",y)"""
#Python method
"""x=10
y=5
x,y=y,x   #This method can be used only in pythona
print("x=",x,"& y=",y)"""
#Conditional Statements:- after writing the condition the statement is written after giving 4 spaces.
"""if(condition): 
    statement
 elif(condition):
    statement 
 else(condition):
    statement"""
#Single line condition also called as Ternary Operator
"""<variable> = <statement1> if <condition> else <statement2>
for eg:- food = input("food= ")
        eat = "yes" if food=='cake' else 'no'
        print(eat) """
#or we can directly write the condition and statement without declaring it into a variable as below
"""<statement> if <condition> else <statement>
for e.g:- food = input("food =")
         print("sweet") if food='cake' or food = 'chocolate' else print("not sweet")"""

#  cleverif/Ternary operator
""" <var> = (false_val,true_val) [condition]
for e.g:- age = int(input("age: "))
           vote= ("yes","no")[age<18]
          print(vote)"""

#LECTURE TWO--------->>>>>>________________________________________________________________________
#string concatenation & length of str
"""str1= "hello"
str2 = "world" 
print(str1+str2)
print(len(str1))"""

#Indexing
"""str= "Himangshu"
print(str[0])
print(str[1])
print(str[2])"""

#slicing
"""str= "Himangshu"
print(str[0:5])
print(str[5:]) #5:len(str)
print(str[::-1]) #Prints the whole string in reverse
print(str[0:9:2])"""


#String Functions
#endswith() and startswith()
"""str= "I am a Coder"
newstr= str.endswith("er")
print(newstr)""" #returns true if string ends with the substring inside parenthesis and false if not

#capitalize()
"""str= "i am a Coder"
print(str.capitalize())"""#capitalizes the 1st character only

#replace()
"""str= "i am a Coder"
print(str.replace(old,new))"""#replaces old alphabet or word with new alpha or new word

#find()
"""str= "i am a Coder"
print(str.find("o"))"""#returns the idx of str of the 1st occur ence

#count()
"""str= "i am a Coder"
print(str.count("o"))""" # counts the no.of times of occurence of substring.

#format()
"""str = "Hi this a PythonCode"
print('This is a {0}{1} in {2}'.format('python ','code ','VSCode '))
print('This is a {v}{c} in {p}'.format(p='python ',c='code ',v= 'VSCode '))"""

#floatformat "{value:width.precision f}"
"""result=100/888
print("This is the {r:1.4f}".format(r=result))"""

#String literal method:- print(f"{variable}")
"""name="Jose"
age=18
marks=25.66
print(f'{name} is {age} years old and has scored {marks} marks.')"""

#spliting
"""str = "Split this string maximum"
list = str.split()
print(list)"""

"""convert= list("bananas")
print(convert)"""

#Write a function to take a str as input and return it as a list.
"""def wordtolist(word):
    return(list(word))

word = input("Word: ")
print(wordtolist(word))"""

#WAP to reverse any string input from the user without using inbuilt method.
"""str = input(str("Enter a string: "))
str1 = ""
for i in str:
    str1=i+str1
print(str1)"""  

#WAP to check if the num provided by the user is odd or even.
"""num = int(input("enter a number:- "))
evenorodd= ("odd","even")[num%2==0]
print(evenorodd)"""
#or
"""num= int(input("enter a number:- "))
print("is even") if(num%2==0) else print("is odd")"""
#or
"""num=int(input("enter a number:- "))
if(num%2==0):
    print(num, "is even")
else:
    print(num,"is odd")"""    

 #LECTURE 3---------->>>>LIST AND TUPLES________________________________________________________________
#LIST- A built in data type that lets us create mutable sequence of values.
"""marks = [94.6,90.2,85.3,76,51]
print(marks)   
print(type(marks))
print(marks[0:5])
print(len(marks))"""

"""student = ["karan",85.6,18,"Guwahati"]
student[0]= "arjun"
print(student[0:])
print(student[-3:-1])"""

#LIST METHODS
list= [6,5,4,8,9,1,3,2]
#append()
"""list.append(7) 
print(list)"""

#pop()
"""popped_item = list.pop() #by default the popped item will be the -1 index
print(list)
print(popped_item)
print(list.pop(0))  #list.pop(index)
print(list)"""

#sort()
"""list.sort() #Ascending Order
print(list)
list.sort(reverse=True) #Descending order
print(list)"""

#reverse()
"""list.reverse() 
print(list)"""

"""student= [1,2,3,4,5,6,7,8]
student.reverse()
print(student)"""

#insert()
"""student.insert(0,0)  #Inserts element 0 at index 0
print(student)"""


#TUPLE:- A built in data type that lets us create immutable sequence of values.
"""tup = (1,3,4,6,9)
# print(tup)
# print(type(tup))
# print(tup[1])
# print(tup[1:4])
#print(str(tup.__sizeof__())+ "bytes")"""

#TUPLE METHODS
"""tup= (1,2,3,4,3)

#tup.index()
print(tup.index(2))

#tup.count()
print(tup.count(3))"""

#WAP to ask the user to enter names of their 3 favourite movies & store them in a list.
"""movies=[]
movies.append(input("Enter the 1st movie:"))
movies.append(input("Enter the 2nd movie:"))
movies.append(input("Enter the 3rd movie:"))
print(movies)"""

#Write a program to check if a list contains a palindrome of list.[Hint:-use copy() method]
"""list=[]
list.append(int(input("Enter a number:")))
list.append(int(input("Enter a number:")))
list.append(int(input("Enter a number:")))
list.append(int(input("Enter a number:")))
list.append(int(input("Enter a number:")))
listCopy=list.copy()
list.reverse()
print("List is a palindrome") if(list==listCopy) else print("List is not a palindrome")"""

#WAP to print the second largest number in a list
"""arr = [5,65,205,199,98]
max1 = max2 = float('-inf')
for n in arr:
    if n > max1:
        max2 = max1
        max1 = n
    elif(n>max2 and n!=max1):
        max2= n
print(max2)""" 

#LECTURE 4------->>>>DICTIONARY AND SETS______________________________________________________
#Dictionaries are used to store data values as key:value pairs.They are unordered, mutable & dont allow duplicate keys.
# Key can be str,int,float also tuple is allowed as tuple is immutable. Value can be str,int,float,list,tuple etc.
#for e.g:-
"""dict = {

     "name": "Himangshu",
     "age": 25,
     "cgpa": 9.5,
     "marks": [84,67,91]
 }
print(dict)
print(dict["name"])
dict["name"]= "HimangshuNath"  #overwriting a value of a key is allowed
print(dict)
dict["surname"] = "Nath"      #adding a new key:value pair can be done
print(dict)"""

#NESTED DICTIONARY EXAMPLE---->>
"""student = {
    "name": "Daniel Maden",
    "age": 18,
    "subject_marks":{
        "chem": 95,
        "phy":94,
        "math":84,
    }
} 
print(student["subject_marks"])
print(student["subject_marks"]["chem"])
print(student["subject_marks"]["math"])
"""
#DICTIONARY METHODS------->>>>>>>.
"""print(tuple(student.keys()))   #student.keys()
print(tuple(student.values()))    #student.values()
pairs= (tuple(student.items()))   #student.items()
print(pairs[0])  #We can access single key:value pair in the list in the form of tuple
print(student.get("name"))        #student.get()  #write any key to get the value of it
student.update({"city":"delhi"})   #student.update({})  #allows to create new key:value pair
print(student)"""

#SET----------------->>>>>>><<<<<<<<_____________________________________________
#Set is a collection of unordered items. Each element in the set must be unique and immutable.
#Sets are mutable but the elements in set are immutable. We can pass str, int, float, tuple inside a set but not list & dictionary.
"""# set ={1,2,4,3,3,"world", "jetix", "jetix"}
# print(set)
# print(type(set))
collection = set()   """     #syntax to write a empty set
"""print(type(collection)) """

#SET METHODS
"""collection = set()
collection.add(1) 
collection.add(4)
collection.add(7)
collection.add(('ramen','pasta','cheese'))
print(collection)
print(len(collection))
collection.remove(4)
print(collection)
collection.clear()
print(collection)"""
"""collection = {"cheese","pasta","ramen","sinju","poched-egg","soyasauce","mayonise"}
print(collection)
print(collection.pop())""" #pops out a random element everytime 
"""set1= {1,2,3}
set2= {3,4,5}
print(set1.union(set2))"""  #combines both set elements and returns a new set
"""print(set1.intersection(set2))""" #combines the common elements from both sets and returns a new set

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary &
# add one by one. Use subjects name as key and marks as values.

"""marks={}
sub= int(input("Chemistry: "))
marks.update({"Chemistry" : sub})
sub= int(input("Mathematics: "))
marks.update({"Mathematics" : sub})
sub= int(input("Physics: "))
marks.update({"Physics" : sub})
print(marks)
"""
#WAP to figure out a way to store 9 & 9.0 as seperate values in the set.
#Possibility 1
"""set1={9,"9.0"}
print(set1)"""
#Possibility 2
"""set = {
    ("int",9),
    ("float",9.0)
}
print(set)"""

#LECTURE 5:- LOOPS-------------------->>>>>>>>>>>>>>>>>>>>>......._____________________________
# PYTHON USES WHILE AND FOR LOOP.

"""count=1
while count<=5:
    print("hello")
    count+=1

print(count)   """

#WAP to print the multiplication table of any number input by the user.
"""n = int(input("Enter the number of which multiplication table you need:"))
i=1
while i<=10:
    print(n*i)
    i+=1"""
#Print the element of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
"""i=1
while i<=10:
    print(i*i)
    i+=1
"""
#Search for a number x in this tuple:(1,4,9,16,25,36,49,64,81,100)
"""tuple =(1,4,9,16,25,36,49,64,81,100)
num=int(input("Enter a number from the tuple: "))
i=0
while i<len(tuple):
    if(tuple[i]==num):
        print("found",i)
    else:
        print("finding...")
    i+=1"""

#break statement is used to terminate from a loop when encountered
"""i=1
while i<=10:
  print(i)
  if(i==5):
    break
  i+=1
"""
#continue:terminates execution of the current iteration and continues execution of the loop with the next iteration
"""i=1
while i<=10:
    if(i==6):
        i+=1
        continue
    print(i)
    i+=1"""

#WAP to print all the odd numbers from 1 to 20 using while loop.
"""i=1
while i<=20:
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1"""

#for loop are genreally used for sequential traversal. For traversal strings, list, tuples etc.
#for loop
"""list = [1,2,3,4]
for val in list:
    print(val)"""

"""str = "Himangshu"
for char in str:
    print(char)""" 

#for loop with else
"""str = "Himangshu"
for char in str:
    print(char)
else:
    print("END")"""  
 
#WAP to search for a number x in this tuple using a loop:
"""tuple = (1,4,9,16,25,36,49,64,81,49,100,49)
x=int(input("Enter a num from the tuple: "))
idx=0
for val in tuple:
    if(val == x):
        print("Number found at idx",idx)
    idx+=1"""

#Range():- Range func returns a sequence of numbers, starting from 0 by default & increment by 1 by default and stops before a specified number.
#range(start?,stop,step?)
"""for el in range(5):
    print(el)"""

"""print(range(10))"""

"""seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])"""

# for i in range(2,10,2): #range(start,stop,step)
#     print(i)

#WAP to print numbers from 100 to 1 using range
"""for i in range(100,0,-1):
    print(i)
"""
#WAP to print multiplication table of any number n.
"""n=int(input("Enter any number: "))
for i in range(1,11):
    print(n*i)"""

 #PASS:- pass is a null statement that does nothing. It is used as a placeholder for future code.
"""for i in range(5):
    pass

print("Found the number")"""

#WAP to print the sum of first n numbers.(using range and while loop)
#Using while loop
"""n=int(input("Enter any number:" ))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("sum is",sum)"""   

#Using range
"""n=int(input("Enter any number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum is",sum)"""

#WAP to find the factorail of first n numbers.
#while loop
"""n=int(input("Enter any number: "))
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print("factorial is",fact)"""  

#for loop
"""n=int(input("Enter any number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print("factorial is",fact)"""    

#CHAPTER 6:- FUNCTIONS & RECURSION-------->>>>>>>>>>>>____________________________________________________________
#Block of statements that performs a specific task.
"""# def function_name(param1,param2): #function definition
# do some work
 return val"""
#function_name(argument1, argument2) #function call
#for e.g:-
"""def calc_sum(a,b):   # function definition, (a,b) are called parameters.
    return a+b"""

"""sum = calc_sum(3,3)    #function call (3,3) are called arguments.
print(sum)"""

#WAP to calcuate the avg of 3 no.s using function.
"""def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg

average =calc_avg(1,2,2)
print(average)"""   

#WAF to print the length of a list.(list is the parameter)
"""marks = [97,98,94,87,68,74,52,48,69,91,31]
cities = ["delhi","pune","gurgaon","hyderabad","bangalore","mumbai","nagpur", "guwahati","kolkata"]"""

"""def length_list(list):
    print(len(list))

length_list(cities)"""    

#WAF to print the elements of a list in a single line.(list is the parameter)
"""def print_list(list):
    for el in list:
        print(el,end=" ")

print_list(cities)"""

#WAF to find the factorial of n.(n is the parameter)
"""def find_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
       
find_fact(5)"""

#WAF to convert USD to INR
"""def convert(usd_val):
    inr_val=usd_val*87.16
    print(usd_val,"USD =",inr_val,"INR")

convert(100)"""

#WAF to take a number as input from user and print ODD if the num is odd and print even if the number is even.
"""def print_evenodd(n=int(input("Enter a number: "))):
    if(n%2==0):
        print("Even")
    else:
        print("ODD")    
print_evenodd()"""      

#RECURSION:- When a function calls itself repeatedly.
#Recursive function
"""def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)"""
#Factorial of n using recursion
"""def factorial(n):
     print(f"factorial() called with n = {n}")
     return_value = 1 if n <= 1 else n * factorial(n -1)
     print(f"-> factorial({n}) returns {return_value}")
     return return_value
factorial(4)"""

#WAF to create a simple calculator.
"""def simple_calculator():
    num1= float(input("Enter a number:- "))
    operator=input("Enter a operator among +,-,*,/ : ")
    num2= float(input("Enter a number:- "))
    add = num1+num2
    sub= num1-num2
    mul=num1*num2
    div=num1/num2
    if(operator== '+'):
        print(num1,"+",num2,"=",float(add))
    elif(operator=='-'):
        print(num1,"-",num2,"=",float(sub))
    elif(operator=='*'):
        print(num1,"*",num2,"=",float(mul))  
    elif(operator=='/'):
        print(num1,"/",num2,"=",float(div))
    while True:
        choice = str(input("Enter YES if you want keep calculating and NO to terminate the calculator : (Y/N)"))
        if(choice=='N'):
            break
        elif(choice=='Y'):
            return simple_calculator()
        else:
            return         
simple_calculator()"""       

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
#  but returns the greater if one or both numbers are odd
def lesser_func(a,b):
    if((a and b)%2==0):
        return min(a,b)
    else:
        return max(a,b)

data= lesser_func(9,7)       
print(data) 

#HIGHER ORDER FUNCTION

"""def logic(func,text):
    return func(text)

def uppercase(text):
    return text.upper()

def double(x):
    return x**2

print(logic(uppercase,"hello"))
print(logic(double,5))"""

            
#CHAPTER 7:- FILE I/O---------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>
#This is a demo how to open a file and read it using python code.
"""f= open("demo.txt", "r") #Here since the file opened is in the same folder we need not copy the entire path.
data = f.read()

print(data)

f.close()"""

""""f= open("demo.txt","r")               #readline() method is used to print the context line by line.
line1= f.readline()
print(line1)
line2 =f.readline()
print(line2)
line3= f.readline()
print(line3)
line4= f.readline()
print(line4)
f.close()"""

#Writing in a file
"""f= open("demo.txt", "w")
f.write("This is a new line overwrite by the previous")
f.close()"""

#Creating a new file using code
"""f = open("sample.txt", "w")
f.close()"""

#Overwriting a file using "r+" mode. The "r+" mode overwrites the file from the starting of the page i.e.
# the pointer is at the beginning of the page. 
"""f=open("demo.txt","r+") 
f.write("abc")
print(f.read())   # Here the output will be printed from the point where the pointer left its overwriting.
f.close()"""     

#with syntax. Here f.close() is not necessary as with syntax closes the file automatically after opening it.
"""with open("demo.txt","r") as f:
    data=f.read()
    print(data)"""

#WAF to check if the word 'overwrite' exist in the file demo.txt.
"""def check_word():
    word = "overwrite"
    with open("demo.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("not found")

check_word() """   

#WAF to find in which line of the file does the word "learning" occur first. Print -1 if word not found
"""def checkfor_word():
  word="learning"
  data=True
  line_no=1
  with open("demo.txt","r") as f:
    while data:
        data = f.readline()
        if(word in data):
           print(line_no)
           return
        line_no+=1   
  return -1        
checkfor_word()""" 

#From a file containing numbers seperated by comma, print the count of even numbers.
"""count=0
with open("demo.txt","r") as f:
    data= f.read()
    print(data)
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count) """  

#Chapter 8:- Object Oriented Programming(OOPS)----------------->>>>>>>>>>>>>>>>>>>>>>>>_______________________
#Creating class
"""class Student:
    name ="Arjun"""
#Creating Object    
"""s1=Student()
print(s1)
print(s1.name)""" 

#Constructor:- All classes have a function called __init__() ,which is always been executed when the object is being 
# initiated. 
"""class Students:
       college_name= "ABC College"     #This a class attribute which is common for all object
       default_name ="Anonymous"  
       def __init__(self,fullName,marks):      #This is a constructor which we created for adding new attributes. If we dont create a constructor, python automatically creates a default constructor.
            self.name=fullName   #obj.attr > class.attr (Obj attr is always greater than class attr)
            self.marks=marks
            print("Adding new Students in the database")
       def welcome(self):                                #This are the methods which can be used inside a class
            print("Welcome student,",self.name)    
       def getmarks(self):
             return self.marks     

s1=Students("Koron",97)
print(s1.name,s1.marks)        
s2=Students("Arjun",92)
print(s2.name,s2.marks) 
print(s1.college_name, s2.college_name)   #printing the class attribute for all diff objects.
s1.welcome()                              #Printing the new created method for a particular object.
print(s1.getmarks())  """
 
#Class and Object Attributes
"""Class attribute is not associated with object attribute
Class attr is used when a common data is need to be stored for all various/diff objects such as college name
which is same for all diff students studying in same college.
Remeber OBJECT ATTR is always on higher priority then CLASS ATTR"""

#Create a student class that takes name & marks of 3 subjects as argument in constructor.After that create a method
# to print the average.
"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding students with their marks in 3 subjects and overall average")
    def print_avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        avg = sum/3
        print("Avg marks of", self.name,"for the marks",self.marks,"is",avg)

s1 = Student("Arjun",[95,96,82])
s1.print_avg()     

s2 = Student("Karan",[89.5,36.23,95])
s2.print_avg()"""

#Static method:- Method that dont use the self parameter. Works at the level of class attr
"""class Student():
    @staticmethod    #Decorator
    def college_name():
        print("ABC college")"""
# A decorator allows us to wrap another function in order to extend the behaviour of the wrapped function,
# without permanently modifying it.

#4 major pillars of OOP are 1.) Abstraction 2.)Encapsulation 3.)Inheritance 4.)Polymorphism

#Create account classes with 2 attributes - balance & account no. Create methods for debit, credit and printing the bal.
"""class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc
        print("Total bal was Rs.",self.bal)

    def debit(self,amount):
        self.bal-=amount
        print("Amount debited from account",self.acc, "is Rs.",amount)
        print("Remaining bal is",self.print_bal())

    def credit(self,amount):
        self.bal+=amount
        print("Amount credit from account",self.acc,"is Rs.",amount)
        print("Account",self.acc,"has",self.print_bal())

    def print_bal(self):
        return self.bal            

acc1 = Account(10000,123456)
acc1.debit(1000)
acc1.credit(600)

acc2= Account(50000,54321)
acc2.debit(6500)
acc2.credit(5400)"""

#WAP to input a number a integer into a list and find out the min and max element in the list.
"""class Solution:
    def get_min_max(self, arr,mini,maxi):
        self.arr=arr
        self.mini=mini
        self.maxi=maxi
        
    def get_min_max(self):
        self.arr=[]
        while True:
            element = int(input("Enter the number:"))
            self.arr.append(element)
            choice = input("Enter another number? (y/n):")
            if choice.casefold()=='n':
                break
        self.mini=min(self.arr)
        self.maxi= max(self.arr)
        print(self.mini, self.maxi)

arr1= Solution()
print(arr1.get_min_max())"""

#Delete & private and public class 
"""class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #This is a private attr which can only accessed by class. To make it private we simply add __ in the starting of the attr
    
    def reset_pass(self):
        print(self.__acc_pass)    

acc1=Account(12345,"abcde")
print(acc1.acc_no)
print(acc1.reset_pass())""" #As we have accessed the acc_pass using a method in class so we can call the method outside the class.

#Inheritance:- When one class(children/derived) derives the properties & methos of another class(larent/base).
"""class Car:
    car_background= "automobile"
    car_color="random"
    car_tyres= "tubeless"

class Suzuki_Car(Car):
    def __init__(self):
        self.car_background
        self.car_color
        self.car_tyres

        
car1=Suzuki_Car()
print(car1.car_background)
print(car1.car_tyres)"""

#Types of Inheritance:- Single Inheritance, Multi-level inheritance, Multiple Inheritance.
#This is an example of multi level inheritance 
"""class Car:
    @staticmethod
    def start():
        print("Car has started")
    @staticmethod
    def stop():
        print("Car has stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
                
car1= Fortuner("diesel")
print(car1.type)
print(car1.start()) """       

#Example of multiple inheritance
"""class A:
    var_A= "Welcome to class A"
class B:
    var_B= "Welcome to class B"
class C(A,B):
    var_C="Welcome to class C"

c1= C()
print(c1.var_C)
print(c1.var_B)
print(c1.var_A)"""

#Super method():- It is used to access method of parent class.
"""class Car:
      def __init__(self,type):
        self.type=type
      @staticmethod
      def start():
       print("Car has started")
      @staticmethod
      def stop():
       print("Car has stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
         super().__init__(type)
         self.name=name
         
car1= ToyotaCar("Fortuner","diesel")
print(car1.name)
print(car1.type)"""

#Class method:- A class method is bound to the class and receives the class as an implicit first argument
# Note:- @staticmethod cant access or modify class state and generally for utility.
#The task is to change the attr of the class
"""class Person:
    name = "anonymous"""
    
    #def changeName(self,name):
        #Person.name=name
        #self.__class__.name= name
    #@classmethod
    #def changeName(cls,name):
        #cls.name=name    

"""p1=Person()
p1.changeName("J")
print(p1.name)
print(Person.name)"""

#Property decorator:- We use @property decorator in the class to use the method as a property.
"""class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    #def calcPercentage(self):
        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
       # print(self.percentage)

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%     

stu1=Student(86,75,39)
print(stu1.percentage)

stu1.math=93
print(stu1.percentage)"""

#POLYMORPHISM:OPERATOR OVERLOADING
#when the same operator is allowed to have different meaning according to the context.
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal= self.real + num2.real
        newImg= self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal= self.real - num2.real
        newImg= self.img - num2.img
        return Complex(newReal,newImg)


num1= Complex(3,4)
num1.showNumber()

num2=Complex(2,5)
num2.showNumber()
"""
"""num3 = num1+num2
num3.showNumber()

num4 = num1-num2
num4.showNumber()"""

#Revision           
"""dict = {'key1':'value1','key2':'value2'}
print(dict)
print(dict['key1'])
"""

"""list = [1,2,[3,4,'hello']]
list[2][2]= 'goodbye'
print(list)"""

#enumerate generator
"""word = 'abcdef'
for index,letter in enumerate(word):
    print(f'{index}:{letter},',sep=" ",end=" ")
"""
#zip function
"""list1 = [1,2,3,4,5,6,7]
list2 = ['a','b','c','d','e']
for item in zip(list1,list2):
    print(item)"""

#LIST COMPREHENSION
#element for element in (variable) or "string" inside [] returns value inside a list. For eg
"""word = "hello"
list = [el for el in word]
print(list)"""   #returns ['h','e','l','l','o']

#another example
"""list = [num for num in range(0,11)]
print(list)"""

#another example
"""my_list = [num for num in range(0,11)]
print(my_list)
my_list = [x**2 for x in my_list if x%2==0]
print(my_list)"""

#celcius to farenheit
#celcius = [0,1,3,16,22,27,29]
"""farenheit = [{((9/5)*temp +32)} for temp in celcius]
print(farenheit)"""
#or
"""fareneheit= []
for temp in celcius:
    fareneheit.append((9/5)*temp +32)
print(fareneheit)"""

#Print out the words that starts with s in this string.
#st = "Print only the words that starts with s in this sentence"
"""split_string = st.split()  
for el in split_string:
    if(el.startswith('s')):
        print(el)
    else:
        continue"""

"""even_list = [num for num in range(1,50) if num%3==0 ]
print(even_list)"""     

#Print first letter of every word in the string st.    
"""for word in st.split():
    print(word[0],sep =" ",end = " ")"""

#using list comprehension
"""new_list = [word[0] for word in st.split()]
print(new_list)"""

#Find the employee who worked for max hours and give him/her employee of the month.
#work_schedule = [('Billy',520),('Andre',519),('Natalie',522),('Jerome',250)]
"""def employee_hours(work_schedule):
    work_hours = 0
    employee_of_the_month= ""

    for employee,hours in work_schedule:
        if(hours>work_hours):
            work_hours=hours
            employee_of_the_month=employee
        else:
            pass
    return(employee_of_the_month,work_hours)

result = employee_hours(work_schedule)        
print(result)
  """

# *args and kwargs function----------------
"""def func(*args):
    print(sum(args) *0.05)
    
func(10,25,35,68)"""



    