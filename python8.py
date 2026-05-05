print("List in Python")

# Notes:-
# List is mutable (line10)
# We can change any value using slicing if we pass it in the form of array.(line13)
# .pop() and .remove() is used to remove item from the list.(line32)
# .insert() is used to add value in the list.(line39)

dish_variety = ["AlooParatha","ChickenCurry","EggCurry","MuttonHandi"]
# print(dish_variety[0]) # AlooParatha
# print(dish_variety[1:4]) # ['ChickenCurry', 'EggCurry', 'MuttonHandi']
# dish_variety[3] = "ChickenTikka"
# print(dish_variety) # ['AlooParatha', 'ChickenCurry', 'EggCurry', 'ChickenTikka']

# # changing the value using slicing
# print(dish_variety[1:2]) # ['ChickenCurry']
# #dish_variety[1:2] = "PannerTikka"
# #print(dish_variety) # ['AlooParatha', 'P', 'a', 'n', 'n', 'e', 'r', 'T', 'i', 'k', 'k', 'a', 'EggCurry', 'MuttonHandi']
# # Here in line 14 it gives the value in the form of array
# dish_variety[1:2] = ["PannerTikka"] # here we pass the value in the form of array
# print(dish_variety) # ['AlooParatha', 'PannerTikka', 'EggCurry', 'MuttonHandi']

# # Loop in Python
# for dish in dish_variety:
#     print(dish,end=" ") # AlooParatha ChickenCurry EggCurry MuttonHandi

# # Condition in Python
# if "EggCurry" in dish_variety:
#     print("item found")
# else:
#     print("Not Found")

# # Remove item in List
# dish_variety.pop() # remove last item from the list
# print(dish_variety) # ['AlooParatha', 'ChickenCurry', 'EggCurry']
# dish_variety.remove("ChickenCurry") # remove item by value
# print(dish_variety) # ['AlooParatha', 'EggCurry']

# Insertion in Python
dish_variety.insert(1,"MushroomMasala") # this method is used to insert value by using indexing
print(dish_variety) # ['AlooParatha', 'MushroomMasala', 'ChickenCurry', 'EggCurry', 'MuttonHandi']