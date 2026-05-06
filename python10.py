print("Tuple in Python")

# Notes:-
# Tuple is immutable.(line8)

heroes = ("IronMan","SuperMan","BatMan","SpiderMan")
# print(heroes[0]) # IronMan
# heroes[0] = "Hulk"
# print(heroes) # error

#Slicing in Tuple
print(heroes[0:3]) # ('IronMan', 'SuperMan', 'BatMan')

# Merge two tuple
newHeroes1 = ("CaptainAmerica","Thor")
newHeroes2 = ("Flash","DoctorStrange")
newHeroes3 = newHeroes1 + newHeroes2
# print(newHeroes3) # ('CaptainAmerica', 'Thor', 'Flash', 'DoctorStrange')
newHeroes4 = newHeroes1.__add__(newHeroes2)
# print(newHeroes4) # ('CaptainAmerica', 'Thor', 'Flash', 'DoctorStrange')

dish = ("Pratha","Chole","Raita")
(pratha,chole,raita) = dish
print(pratha,chole,raita) # Pratha Chole Raita