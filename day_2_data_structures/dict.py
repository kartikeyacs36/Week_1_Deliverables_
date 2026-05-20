dict1 = {
    "brand" : "chervolet",
    "model": "silverado",
    "year": 2002,
    "year": 2005, 
    
}
print(dict1["year"])
print(dict1.keys()) 
print(dict1.values()) 
print(dict1.items()) 

for key, value in dict1.items(): 
    print(key, value)
dict1["color"] = "blue" 
dict1["year"] = 2003 
del dict1["model"] 

#nested dictionary
family = { 
    "child1" : {
        "name" : "Sree",
        "year" : 2000
    },
    "child2" : {
        "name" : "Kartik",
        "year" : 2003
    },
}

 #loop through a nested dictionary
for key, value in family.items():
    print(key)
    for k, v in value.items():
        print(k, v)
