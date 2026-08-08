for i in range(5):
    print(i)
    
for i in range(2, 10, 2):
    print(i)
    
for i in range(5, 0, -1):
    print(i)

for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
    
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Done")

for i in range(3):
    for j in range(4):
        print("X")

for i in range(3):
    print(i)
else:
    print("Done")
    
# Takes a number n from the user.
# Prints all numbers from 1 to n.
# Prints "Even" for even numbers and "Odd" for odd numbers.
n=int(input("Enter a number: "))
for i in range(1,n+1,1):
    if i%2==0:
        print("Even",i)
    else:
        print("Odd",i)
