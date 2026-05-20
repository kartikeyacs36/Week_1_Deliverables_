#a program to count the number of students with a certain grade
grades=("A", "B", "C", "D", "F", "A", "B", "C", "A" )
grade = input("Enter the grade to count: ")
print("The number of students with grade", grade, "is:", grades.count(grade))

#loop through a tuple
for i in range(len(grades)):
    print(grades[i])
#concatenating two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)   