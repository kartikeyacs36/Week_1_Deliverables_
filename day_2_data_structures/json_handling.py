#6. JSON handling

##json functions - dumps : converts python object into json string
##loads : converts json string into python object
##dump : converts python object into json file
##load : converts json file into python object

import json
data = {
    "name": "Kartikeya",
    "age": 22,
    "city": "Guntur",
    "is_student": True,
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)
print(data)
json_data = json.dumps(data , indent=4) #the 's' in dumps or loads is for string and indent for formatting the json's indentation
print(json_data)
print(type(json_data))

python_data = json.loads(json_data ,)
print(python_data)
print(type(python_data))