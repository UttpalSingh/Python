import math

#Problems in Function


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

num = int(input("enter a number : "))
a,c = parm_of_circle(num)
print(f"Area : {a:2f}")
print(f"Circumference : {c:2f}")