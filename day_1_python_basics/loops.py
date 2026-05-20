#for loop
for i in range(10): 
    print(i)
for i in range (0,6): 
    print(i)
for i in range (3,18,3): 
    print(i)
for i in range(10):
    for j in range(5):
        print(i,j)

#continue
for i in range(6):
    if i==4: 
        continue
    print(i)
#break
for i in range(6):
    if i==5: 
        break
    print(i)
#pass
for i in range(3):
    pass 

#while loop
i=3
while i<=6:
    print(i)
    i+=1