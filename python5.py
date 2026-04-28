print("List")

myList = [123,234,'abc',987]
print(myList[0]) #123
print(len(myList)) #4
print(myList[0])  #123
myList.append(19421)
print(myList) #[123, 234, 'abc', 987, 19421]


print("Dictionary")

myDict = {
    'name' : 'kohli',
    'type' : 'Batsman',
    'run' : 120000,
}

print(myDict)  #{'name': 'kohli', 'type': 'Batsman', 'run': 120000}
print(myDict.values())  #dict_values(['kohli', 'Batsman', 120000])
print(myDict['name'])  #kohli
myDict.update({"name": "Virat"}) # update method in dictionary
print(myDict)  #{'name': 'Virat', 'type': 'Batsman', 'run': 120000}
myDict["run"] = 140000
print(myDict)  #{'name': 'Virat', 'type': 'Batsman', 'run': 140000}



print("Tuples")

myTup = (1,2,'abc',3,4)
print(len(myTup))
print(myTup[0])  #1
x = myTup.count(3) # count value in tuple
print(x)  #1
x = myTup.index(3)
print(x)  #3
