#adding three inputs to a list 
movies=[]
movies.append(input("Enter the name of a movie: ") )
movie2 = input("Enter the name of another movie: ")  
movies.append(movie2) 
movie3 = input("Enter the name of another movie: ")
movies.append(movie3)
print(movies)
#checking if a list is a palindrome
list=[1, 2, 3, 4, 5, 4, 3, 2, 1]
list1=list.copy()
list1.reverse()
if list==list1:
    print("The list is a palindrome")
else:    
    print("The list is not a palindrome")

#python Lists - store multiple items in a single variable. lists are mutable (can be changed) , ordered and indexed , allows duplicate values

fruits = ["apple", "banana", "cherry"] #create a list
print(fruits)
print(len(fruits)) # len() is a built-in function which returns the length of the list
print(fruits[1]) #accessing elements of the list by index - starts from 0
print(fruits[-1]) #accessing the last element of the list ; -2 is the second last element and so on.
print(fruits[0:2]) #slicing - accessing multiple elements of the list within a range - start index included , end index excluded
print(fruits[1:])
print(fruits[-2:])

if "papaya" in fruits:
    print(True)
else:
    print(False)
fruits[1]="mango" #updating an element of the list
fruits[0:2] = ["apple", "watermelon"] #updating multiple elements of the list

##list methods : append(), insert(), remove(), pop(), clear(), reverse(), sort()

fruits.append("orange") #adding an element to the end of the list.
fruits.insert(1, "kiwi") #adding an element at a specific index
fruits.remove("apple") #removing an element from the list
fruits.pop() #removing the last element of the list or if we specify index it will remove the element at that index eg ; pop(1)
fruits.reverse() #reversing the list
fruits.sort() #sorting the list

vegetables = ["carrot", "potato", "tomato"]

fruits.extend(vegetables) #adding multiple elements or a list to the end of the list , this method can work with tuples  , sets and dictionaries as well
fruits.clear()#clearing the list , but it will not delete the list itself - still available in the memory
del fruits #deleting the entire list ; if we try to print fruits , it will throw an error

fruits = ["apple", "banana", "cherry"]
##loop through a list
for i in range(len(vegetables)):
    print(vegetables[i])

fruits = fruits + vegetables #concatenating two lists
