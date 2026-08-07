# ====================================
# Day 1 - Python Fundamentals
# ====================================

# ------------------------------------
# 1. Data Types
# ------------------------------------

print(type(10))
print(type("Hello"))
print(type(print))

# ------------------------------------
# 2. Operators
# ------------------------------------

print(15 + 5)
print(20 - 8)
print(6 * 7)
print(15 / 4)
print(15 // 4)
print(15 % 4)
print(2 ** 5)

# ------------------------------------
# 3. Arithmetic Calculator
# ------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)

# ------------------------------------
# 4. Even or Odd
# ------------------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# ------------------------------------
# 5. Grade Calculator
# ------------------------------------

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")