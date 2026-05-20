'''#creating a variable and printing it and its type 
x = 5
y = "John"
print(x)
print(type(x))
print(y,end="\t");print(type(y))
#declaring a variable using casting while creating the variable itself
a = str(3)    # a will be '3'
b = int(3)    # b will be 3
c = float(3)  # c will be 3.0
print(a)
print(b)
print(c)
salaryperhour = 15
hoursworked = 40
weeklysalary = salaryperhour * hoursworked
print(weeklysalary)

#multiple values to multiple variables
x, y, z = "AI ", "ML", "DL"
print(x)
print(y)
print(z)

#multiple values to one variable
x = y = z = "AI"
print(x)
print(y)
print(z)

#list to variables
lang = ["ai", "ml", "dl"]
x, y, z = lang
print(x)
print(y)
print(z)

#Output variables of different types
x = "AI "
y = "John"
print(x+y)'''

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)