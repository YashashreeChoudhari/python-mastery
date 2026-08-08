squares = [x * x for x in range(1, 6)]
print(squares)

a = [5, 2, 8, 2]

a.append(10)
a.remove(2)
a.sort()

print(a)



a = [1, 2, 3]
b = a

b[1] = 100

print(a)
print(b)



a = [1, 2, 3, 4, 5]

b = a[1:4]
b.append(10)

print(a)
print(b)

# Write a program that takes n numbers from the user and creates a new list containing only the even numbers.
n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input())
    
    if num % 2 == 0:
        numbers.append(num)

print(numbers)