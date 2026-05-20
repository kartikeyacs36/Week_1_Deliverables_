#Comprehension - list , set and dictionary comprehensions
##list comprehension - [expression if condition else expression for item in iterable]
numbers = [1, 2, 3, 4]
result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

matrix = [ #nested list comprehension
    [1, 2],
    [3, 4],
    [5, 6]
]
flat = [num for row in matrix for num in row]

##set comprehension
numbers = [1, 2, 2, 3, 3, 4]
unique = {n for n in numbers}
##Dictionary Comprehension - {key: expression if condition else expression for item in iterable}
numbers = [1, 2, 3, 4]
result = {n: "Even" if n % 2 == 0 else "Odd" for n in numbers}