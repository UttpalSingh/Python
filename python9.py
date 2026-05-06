print("Dictionary in Python")

# Notes:-
# Dictionary is mutable.(line16)
# .get() is used to acess data by using key.(line18)
# .pop() is used to delete data from the dict by using key name.(line22)
# del is used to delete data from the memory.(line25)


Player_Details = {
    "name" : "Virat",
    "ID" : 18,
    "CallSign" : "Chiku",
    "Player" : "GOAT"
}
# print(Player_Details) #{'name': 'Virat', 'ID': 18, 'CallSign': 'Chiku', 'Player': 'GOAt'}
# print(Player_Details["name"]) # Virat
# Player_Details["name"] = "KingKohli" 
# print(Player_Details["name"]) # KingKohli

# Methods in Dictionay
# print(Player_Details.get("ID")) # 18
# Player_Details.pop("CallSign") # this method is used to delete data from the dict by the key name
# print(Player_Details) # {'name': 'Virat', 'ID': 18, 'Player': 'GOAT'}
# del Player_Details["ID"] # it delete the reference from the memory
# print(Player_Details) # {'name': 'Virat', 'CallSign': 'Chiku', 'Player': 'GOAT'}

# # Loop on dictionary
# for i in Player_Details:
    # print(i) # it gives only key name
    # print(i,Player_Details[i]) # it gives value with key name

# for key,value in Player_Details.items(): # By this we can print both key and value 
    # print(key) # it gives key 
    # print(value) # it gives value 
    # print(key,value) # it gives both key and value

# # Add value in dictionay
# Player_Details["Type"]  = "Batsman" 
# print(Player_Details ) # {'name': 'Virat', 'ID': 18, 'CallSign': 'Chiku', 'Player': 'GOAT', 'Type': 'Batsman'}

# Dictionary inside Dictionary
tea_shop = {
    "chai" : {
        "Masala" : "Spicey",
        "Ginger" : "Zesty"
    },
    "Tea" : {
        "Green" : "Mild",
        "Black" : "Strong"
    }
}
# print(tea_shop) # {'chai': {'Masala': 'spicey', 'Ginger': 'zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# print(tea_shop["chai"]) # {'Masala': 'spicey', 'Ginger': 'zesty'}
# print(tea_shop["chai"]["Masala"]) # spicey

Keys = ["masala","ginger","lemon"]
default_value = "delicious"
new_dict = dict.fromkeys(Keys,default_value)
print(new_dict) # {'masala': 'delicious', 'ginger': 'delicious', 'lemon': 'delicious'}

# Merge two dictionary
d1 = {'x': 1, 'y': 2}
d2 = {'k': 3, 'z': 4}

d3 = d1 | d2
print(d3) # {'x': 1, 'y': 2, 'k': 3, 'z': 4}