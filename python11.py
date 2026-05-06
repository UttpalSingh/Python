print("Conditional problem in Python")

# Problem 1
n = int(input("Enter your age : "))

if n < 13:
    print("child")
elif n >= 13 and n <= 19:
    print("Teenager")
elif n >= 20 and n <= 59:
    print("Adult")
else:
    print("Senior")
