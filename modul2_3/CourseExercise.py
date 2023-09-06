
# Equality
# var = 0  # Assigning 0 to var
# print(var == 0)
#
# var = 1  # Assigning 1 to var
# print(var == 0)
# # Results
# # True
# # False

# Inequality
# var = 0  # Assigning 0 to var
# print(var != 0)
#
# var = 1  # Assigning 1 to var
# print(var != 0)
#
# False
# True

# LAB1
# n = int(input("Enter a number: "))
# print(n >= 100)

# Results
# False
# False
# False --> not as expected output = True
# True
# False
# True

# Example1 = how to identify the larger of two numbers

# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# Print the result
# print("The larger number is:", larger_number)

# Results
# Enter the first number: 100
# Enter the second number: 101
# The larger number is: 101

# Example2 = code variation

# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
#
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2
#
# # Print the result
# print("The larger number is:", larger_number)

# Enter the first number: 100
# Enter the second number: 75
# The larger number is: 100


# Example3 = find the largest of three numbers

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# Results
# Enter the first number: 34
# Enter the second number: 344
# Enter the third number: 3444
# The largest number is: 3444

