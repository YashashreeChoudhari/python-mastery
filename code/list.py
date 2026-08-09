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

#Practice
# Write a program that:
# Prints every number.
# Prints only the even numbers.
# Calculates the total.
# Finds the largest number without using max().
# Counts how many numbers are greater than 10.

numbers = [12, 7, 250, 4, 18, 9, 30]

# Prints every number.
for i in numbers:
    print(i)
    
#prints only the even numbers.
for i in numbers:
    if i%2==0:
        print(i)

# Calculates the total.
total=0
for i in numbers:
    total=total+i
print(total)

#Finds the largest number without using max().
lar=numbers[0]

for i in numbers:
    if i>lar:
        lar=i
print(lar)

#Counts how many numbers are greater than 10.
count=0

for i in numbers:
    if i>10:
        count+=1
print(count)

numbers = [12, 7, 25, 4, 18, 9, 30, 25]

# Write a program to find the second-largest distinct number.
large=numbers[0]
sec=numbers[0]

for i in numbers:
    if i>large:
        sec=large
        large=i
    
    elif i>sec and i!=large:
        sec=i
print(sec)

#largest and second largest using none in inialization       
large = None
sec = None

for i in numbers:

    if large is None:
        large = i

    elif i > large:
        sec = large
        large = i

    elif i != large and (sec is None or i > sec):
        sec = i

print("Largest:", large)
print("Second largest:", sec)

#enumerate()
# Write a for loop using enumerate() that produces:

# 0 -> 10
# 1 -> 20
# 2 -> 30
# 3 -> 40

numbers = [10, 20, 30, 40]
for index,task in enumerate(numbers):
    print(index,task)
    
names = ["Amit", "Rahul", "Priya"]
# Write a loop that prints:
# 1. Amit
# 2. Rahul
# 3. Priya
# for index,task in enumerate(names,start=1):
#     print(index,task)

languages = ["Python", "Java", "C++", "JavaScript", "Go"]

finding=input("Enter a language: ")
for index,language in enumerate(languages,start=1):
    if finding == language:
        print(f"{finding} found at position {index}")
        break
else:
        print("Language not found")


#Zip
names = ["Amit", "Rahul", "Priya"]
ages = [21, 22, 20]
cities = ["Pune", "Mumbai", "Delhi"]

for name, age, city in zip(names, ages, cities):
    print(name, age, city)

#Write a for loop using zip() that prints:
products = ["Laptop", "Mouse", "Keyboard"]
prices = [50000, 800, 1500]

for product,price in zip(products,prices):
    print(product,price)

students = ["Amit", "Rahul", "Priya", "Neha"]
marks = [85, 62, 91, 45]

for s,m in zip(students,marks):
    if(m>=50):
        print(f"{s} - Pass")
    else:
        print(f"{s} - Fail")

#Problem 1 — Separate data
numbers = [12, 7, 25, 4, 18, 9, 30, 25, 6, 11]
even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

#Problem 2 — Compare two lists
students = ["Amit", "Rahul", "Priya", "Neha", "Vikram"]
marks = [85, 42, 73, 91, 38]

passed=[]
failed=[]

for s,m in zip(students,marks):
    if m>=50:
        passed.append(s)
    else:
        failed.append(s)
print(passed)
print(failed)

#common
developers = ["Amit", "Rahul", "Priya", "Neha", "Vikram"]
active_users = ["Rahul", "Neha", "Amit", "Karan"]
common = []

for developer in developers:
    if developer in active_users:
        common.append(developer)

print(common)

#freq counting
numbers = [2, 4, 2, 7, 4, 2, 9, 7, 4, 4]

freq = {}

for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in freq:
    print(f"{i} -> {freq[i]}")


#product task
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]
sales = [5, 20, 12, 7, 15]
prices = [50000, 800, 1500, 12000, 3000]

high_rev = 0
high_pro = ""

for product,sale, price in zip(products, sales, prices):
    revenue=sale*price
    print(f"{product}->{revenue}")

    if revenue > high_rev:
        high_rev=revenue
        high_pro=product

print(high_rev)
print(high_pro)

