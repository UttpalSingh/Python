print("Internal working of python")

a = 10
# In python there is no dataType of variable but dataType of value exist
# Here 10 will store in the memory with its dataType but not variable a


# List is mutable
myList1 = [1,2,3,4,5]
myList2 = myList1

myList1 = "chai"
myList2 = myList1
print(myList2)
# here reference of myList1 will change from [1,2,3,4,5] to "chai" so myList2 will print "chai"
# [1,2,3,4,5] will deleted from the memory bcz it has no reference 


List1 = [11,22,33,44,55]
List2 = List1
print(List2) # [11, 22, 33, 44, 55]
List1[0] = 99
print(List1) # [99, 22, 33, 44, 55]
print(List2)  # [99, 22, 33, 44, 55]
#####################################
L1 = [123,456,789]
L2 = L1
print(L2) # [123, 456, 789]
L2 = [123,456,789]
L1[0] = 342
print(L2) # [123, 456, 789]
# Here value of L2 will remain [123,456,789] bcz List is mutable and we give new value of L2 in line 29 that is similar to L1 but they are diffrent
# So the new value of L2 is [123, 456, 789] and L1 is [342,456,789]