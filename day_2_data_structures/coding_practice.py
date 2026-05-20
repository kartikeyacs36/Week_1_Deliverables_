# print asterik
for i in range(5):
    print("*" * (i + 1))    

#finding the largest number in a list
numbers = [3, 5, 2, 8, 1]
largest = numbers[0]
for number in numbers:  
    if number > largest:
        largest = number
print("The largest number is:", largest)

#checking if a string is a palindrome
string = input("Enter a string: ")
reversed_string = string[::-1]
if string == reversed_string:
    print("The string is a palindrome")
else:    
    print("The string is not a palindrome")

#counting the number of vowels in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("The number of vowels in the string is:", count)

#checking if a number is prime
number = int(input("Enter a number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:   
    print(number, "is not a prime number")  

#checking if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")

#checking if a number is positive, negative or zero
number = float(input("Enter a number: "))
if number > 0:
    print(number, "is a positive number")
elif number < 0:
    print(number, "is a negative number")
else:
    print(number, "is zero")

#checking for a number x in tuple using a while loop
numbers = (1, 2, 3, 4, 5)
x = int(input("Enter a number to check: "))
i = 0
found = False
while i < len(numbers):
    if numbers[i] == x:
        found = True
        break
    i += 1
if found:
    print(x, "is in the tuple")
else:    
    print(x, "is not in the tuple")

#checking for a number x in tuple using a for loop
numbers = (1, 2, 3, 4, 5)
x = int(input("Enter a number to check: "))
found = False
for number in numbers:
    if number == x:
        found = True
        break
if found:
    print(x, "is in the tuple")
else:
    print(x, "is not in the tuple")

#add 9 and 9.0 in a set and the length of the set must be 2
my_set = set()
my_set.add(("int", 9))
my_set.add(("float", 9.0))
print("The length of the set is:", len(my_set))
print("The set is:", my_set)
print(type(my_set))
