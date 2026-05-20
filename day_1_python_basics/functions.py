#built-in type function
print("The Knowledge Factory!") 

 #user-defined function 
def display():
     print("Hello, welcome to The Knowledge Factory!")
display()

#user defined function with parameters
def add(a, b): 
    return a + b
result = add(3, 5)
print(result)

#lambda function
square = lambda x: x * x 
print(square(5))

 #nested function - a function defined inside another function
def brand():
    print("car brands")
    def model():
        print("car models")
    model()
brand()
