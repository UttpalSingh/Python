import math

#Problems in Function

#Notes
#lambda function(60)
#Format String(51,52,92)
#Add multiple value in function(64)[function with *args]
#Print multiple parameter and argument inside a function(89)[function with **kwargs]


#Problem1
def calculateSquare(num):
    print(num ** 2)

# num = int(input("Enter number : "))
# calculateSquare(num)
####################################
def calculateSquare(num):
    return num ** 2

# num = int(input("Enter number : "))
# square = calculateSquare(num)
# print(square)
# print(calculateSquare(num))

#Problem2
def sum_of_numbers(a,b):
    return a+b;

# a = int(input("Enter a number : "))
# b= int(input("Enter a number : "))
# print(sum_of_numbers(a,b))

# Problem3
def multiply_input(a,b):
    return a*b

# print(multiply_input(3,4))
# print(multiply_input('a',3))
# print(multiply_input(4,'b'))

# Problem4
def parm_of_circle(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    return area,circumference

# num = int(input("enter a number : "))
# a,c = parm_of_circle(num)
# print(f"Area : {a:2f}")
# print(f"Circumference : {c:2f}")

# Problem5
def greet(name = "Raj"): # function with default parameter
    return "Hi" + " " + name + " " + "You are welcome here"

# print(greet("VIGI"))

#Probelm6
cube = lambda x: x ** 3
# print(cube(3))

#Problem7 
def sum_all(num):
    sum = 0
    for i in num:
        sum += i
    return sum

# n = int(input("enter a number to run number of loop : "))

list = []

# for i in range(1,n+1):
    # num = int((input("Enter a number : ")))
    # list += [num]
# print("sum = ",sum_all(list)) # here I store the value list in function

def sum_All(*args):
    print(*args) # 1 2 3 4
    print(args) # (1, 2, 3, 4)
    for i in args:
        print (i * 2) # 2,4,6,8

    return sum(args)
# print("sum = ",sum_All(1,2,3,4))

#Problem8
def printKwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
# print(printKwargs(name = "virat",role = "Batsman",nickname = "Chiku"))

#Problem9
