#if statement 
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))  
if a > b: 
    print("a is greater than b!")

#if-else 
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are eligible to apply for driving license.")
else:
    print("You are not eligible to apply for driving license.")

# elif
marks =int(input("Enter your marks: "))
if marks >=92: 
    grade = "A+"
elif marks >=88:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >=75:
    grade = "C"
else:
    grade = "D"
print("Your grade is:", grade)

#Nested if
is_adult = True
if age>=18:
    if age>=35:
        print("Not allowed for examination.")
    else:
        print("Entry allowed.")
else:
    print("Underage.")