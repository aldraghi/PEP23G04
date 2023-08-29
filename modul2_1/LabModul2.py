# print("Programming","Essentials","in", sep="***", end = "...")
# print("Python")
# print("    *", "        *")
# print("   * *", "      * *")
# print("  *   *", "    *   *")
# print(" *     *", "  *     *")
# print("***   ***","***   ***" )
# print("  *   *", "    *   *")
# print("  *   *", "    *   *")
# print("  *****", "    *****")
# print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n"*2, end= "\n")
# print("    *         *\n   * *       * *\n  *   *     *   *\n *     *   *     *\n***   *** ***   ***\n  *   *     *   *\n  *   *     *   *\n  *****     *****\n"*2)
# print(0o123)
# print(0x123)
# print(0.0000000000000000000001) #literal float
# print("I like \"Monty Python\"")
# print('I like "Monty Python"')
# print('I\'m Monty Python.')
# print(True > False)
# print(True < False)
# Lab Write a one-line piece of code, using the print() function, as well as the newline and escape characters,
# to match the expected result outputted on three lines.
# print("\"I'm\"\n", "\"\"learning\"\"\n", "\"\"\"Python\"\"\"")
# 2.3 Operators and expressions
# +, -, *, /, //, %, **
# ** --> 2**3 --> 2 la puterea 3
# print(2+2) #4
# print(2 ** 3) #8
# print(2 ** 3.) #8.0
# print(2. ** 3) #8.0
# print(2. ** 3.) #8.0

# A / (slash) sign is a divisional operator.
# print(6 / 3) #2.0
# print(6 / 3.) #2.0
# print(6. / 3) #2.0
# print(6. / 3.) #2.0

# --> The result produced by the division operator is always a float!

# A // (double slash) sign is an integer divisional operator.
# its result lacks the fractional part - it's absent (for integers),
# or is always equal to zero (for floats); this means that the results are always rounded;
# print(6 // 3)  #2
# print(6 // 3.) #2.0
# print(6. // 3) #2.0
# print(6. // 3.)#2.0

# print(6 // 4)  #1
# print(6. // 4) #1
# The result of integer division is always rounded to the nearest integer value that is less
# than the real (not rounded) result.

# print(6 / 4)   #1.5
# print(6. / 4)  #1.5

# The rounding goes toward the lesser integer value, and the lesser integer value is -2
# print(-6 // 4)   #-2 since the real value is -1.5
# print(6. // -4)  #-2.0 since the real value is -1.5
#
# print(-6 / 4)   #-1.5 results are the real value
# print(6. / -4)  #-1.5 results are the real value

# % --> The result of the operator is a remainder left after the integer division.

# print(14 % 4)   #2
# Results explanation
# 14 // 4 gives 3 → this is the integer quotient;
# 3 * 4 gives 12 → as a result of quotient and divisor multiplication;
# 14 - 12 gives 2 → this is the remainder.

# print(12 % 4.5)
# Results explanation
# print(12 // 4.5)
# 12 // 4.5 gives 2.0  → this is the integer quotient;
# print(2.0 * 4.5)
# 2.0 * 4.5 gives 9.0 → as a result of quotient and divisor multiplication;
# print(12 - 9.0)
# 12 - 9.0 gives 2 → this is the remainder.

# The addition operator is the + (plus) sign

# print(-4 + 4)  #0
# print(-4. + 8) #4.0

# The subtraction operator is obviously the - (minus) sign

# print(-4 - 4)  #-8
# print(4. - 8)  #-4.0
# print(4 - 8)   #-4
#
# print(-1.1)    #-1.1

# Operators and their priorities
# print(2 + 3 * 5)  #17
# The phenomenon that causes some operators to act before others
# is known as the hierarchy of priorities.

# The binding of the operator determines the order of computations
# performed by some operators with equal priority, put side by side in one expression.
# Most of Python's operators have left-sided binding, which means that the calculation
# of the expression is conducted from left to right.

# print(9 % 6 % 2)
# from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1

# The exponentiation operator uses right-sided binding
# print(2 ** 2 ** 3)  # 256 --> 2 ** 3 → 8; 2 ** 8 → 256

# List of priorities
# Priority	Operator
# 1	**
# 2	+, - (note: unary operators located next to the right of the power operator bind more strongly)	unary
# 3	*, /, //, %
# 4	+, -	binary


# print(3%5)
# print(3 // 5) #0
# print(0 * 5)  #0
# print(3 - 0)  #3

# print(2 * 3 % 5) #1 --> Both operators (* and %) have the same priority,
#                       so the result can be guessed only when you know the
#                       binding direction. --> in this case is left to right


# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)  #10

# print(4 ** -1)  #0.25

# print(15 - 1 * (5 * (1 + 2)))

# Exercise
# print((2 ** 4), (2 * 4.), (2 * 4))  #16 8.0 8

# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4)) #-0.5 0.5 0 -1

# print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# print(2 ** 3 ** 2)
# print(3 ** 2)
# print(2 ** 9)
#
# print(2 % 4)
# print(2 % -4)

# 2.4 Variables
# Keywords -->reserved keywords
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# A variable comes into existence as a result of assigning a value to it.
# var = 1
# print(var)

# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'
# print(var, account_balance, client_name)
# print(var)
# Results 1 1000.0 John Doe / 1

# var = "3.8.5"
# print("Python version: " + var)

# Assign a new value to an already created variable
# var = 1
# print(var)
# var = var + 1
# print(var)

# var = 100
# var = 200 + 300
# print(var)
# #Results is 500

# The square of the hypotenuse is equal to the sum of the squares of the other two sides.

# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c)
# Results are 5.0

# LAB Test
# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples.
# They were all very happy and lived for a long time. End of story.

# Task
# 1.create the variables: john, mary, and adam;
# client_name1 = "john"
# client_name2 = "mary"
# client_name3 = "adam"
# print(client_name1, client_name2, client_name3)
# var1 = 3
# var2 = 5
# var3 = 6
#
# print("john has", + var1, "apples")
# print("mary has", + var2, "apples")
# print("adam has", + var3, "apples")
#
# print("var1", "var2", "var3", sep=", ")
#
# total_apples = var1 + var2 + var3
# print("Total number of apples:", total_apples)

# Results:
# john mary adam
# john has 3 apples
# mary has 5 apples
# adam has 6 apples
# var1, var2, var3
# Total number of apples: 14

# Shortcut operators
# calculate a series of successive values of powers of 2
# x = x * 2 OR x *= 2

# i = i + 2 * j ⇒ i += 2 * j
# var = var / 2 ⇒ var /= 2
# rem = rem % 10 ⇒ rem %= 10
# j = j - (i + var + rem) ⇒ j -= (i + var + rem)
# x = x ** 2 ⇒ x **= 2

# LAB
# 1. Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

# miles to kilometers;
# kilometers to miles.

# Initial code:

# kilometers = 12.25
# miles = 7.38
# miles_to_kilometers = ###
# kilometers_to_miles = ###
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Test code

# kilometers = 12.25
# miles = 7.38
#
# miles_to_kilometers = miles * kilometers
# kilometers_to_miles = kilometers / miles
#
# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Results
# 7.38 miles is 90.4 kilometers
# 12.25 kilometers is 1.7 miles

# 2. Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints
# the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:

# 3x3 - 2x2 + 3x - 1

# The result should be assigned to y.

# Test Data
# Sample input
#
# x = 0
# x = 1
# x = -1
#
# Expected Output
#
# y = -1.0
# y = 3.0
# y = -9.0

# Editor code
# x =  # hardcode your test data here
# x = float(x)
# # write your code here
# print("y =", y)

# 2.5 Leaving comments in code
# In Python, a comment is a piece of text that begins with a # (hash) sign and extends to the end of the line.

# LAB
# The code in the editor contains comments. Try to improve it: add or remove comments where you find it appropriate

# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

# Editor code
# a = 2 # number of hours
# seconds = 3600 # number of seconds in 1 hour
#
# print("Hours: ", a) #printing the number of hours
# print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

# here we should also print "Goodbye", but a programmer didn't have time to write any code
# this is the end of the program that computes the number of seconds in 3 hour

# Test code
# number_of_hours = 2
# seconds = 3600
#
# print("Hours: ", number_of_hours) #printing the number of hours
# print("Seconds in Hours: ", number_of_hours * seconds) # printing the number of seconds

# here we should also print "Goodbye", but a programmer didn't have time to write any code
# this is the end of the program that computes the number of seconds in 3 hour

# 2.6 Input

# The input() function is able to read data entered by the user and to return the same data to the running program.

# Editor code
# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")

# The input() function with an argument
# The input() function can do something else: it can prompt the user without any help from print()

# Editor code:
# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# Editor code bad example
# This means that you mustn't use it as an argument of any arithmetic operation, e.g., you can't use this data to
# square it, divide it by anything, or divide anything by it.

# # Testing TypeError message.
#
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Results:
# Enter a number: 10
# Traceback (most recent call last):
#   File "C:\Users\aldraghi\PycharmProjects\PEP23G04\modul2_1\LabModul2.py", line 329, in <module>
#     something = anything ** 2.0
#                 ~~~~~~~~~^^~~~~
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
#
# Process finished with exit code 1

# Python offers two simple functions to specify a type of data and solve this problem - here they are: int() and float().
# the float() function takes one argument (e.g., a string: float(string)) and tries to convert it into a float (the rest is the same).

# Editor code

# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)
# Results:
# Enter a number: 10
# 10.0 to the power of 2 is 100.0
#
# Process finished with exit code 0

# find the length of a hypotenuse using operator input for both legs' lengths
# Editor code
# leg_a = (float(input("Input first leg length: ")))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)
# Results:
# Input first leg length: 11
# Input second leg length: 23
# Hypotenuse length is 25.495097567963924

# Process finished with exit code 0

# Test code ?????
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = round((leg_a**2 + leg_b**2) ** .5)
# print("Hypotenuse length is", hypo)

# As the print() function accepts an expression as its argument, you can remove the variable from the code.
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", round((leg_a**2 + leg_b**2) ** .5))

# Result
# Input first leg length: 44
# Input second leg length: 23
# Hypotenuse length is 50
#
# Process finished with exit code 0

# String operators
# Concatenation
# The + (plus) sign, when applied to two strings, becomes a concatenation operator
# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")
# Result:
# May I have your first name, please? Alin
# May I have your last name, please? Draghici
# Thank, you.
#
# Your name is Alin Draghici.
#
# Process finished with exit code 0

# Don't forget - if you want the + sign to be concatenated, not an adder, you must ensure that both its
# arguments are strings.

# Replication

# The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains
# commutative in this position) becomes a replication operator

# string * number
# number * string

# It replicates the string the same number of times specified by the number.

# This simple program "draws" a rectangle, making use of an old operator (+) in a new role:
# print("+" + 20 * "-" + "+")
# print(("|" + " " * 20 + "|\n") * 10, end="")
# print("+" + 20 * "-" + "+")

# Type conversion
# convert a number into a string
# function capable of doing that is called
# str(number)

# The "right-angle triangle"
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
#
# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

# LAB1

# Your task is to complete the code in order to evaluate the results of four
# basic arithmetic operations.

# Editor code
# input a float value for variable a here
# input a float value for variable b here

# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

# print("\nThat's all, folks!")

# Test code
# var_a = float(input("Variable a: "))  # input a float value for variable a here
# var_b = float(input("Variable b: "))  # input a float value for variable b here
# print("Addition", var_a + var_b)
# print("Subtraction", var_a - var_b)
# print("Multiplication", var_a * var_b)
# print("Division", var_a / var_b)


# output the result of addition here
# output the result of subtraction here
# output the result of multiplication here
# output the result of division here

# print("\nThat's all, folks!")

# print(var_a + var_b, var_a - var_b, var_a * var_b, var_a / var_b)

# LAB2

# complete the code in order to evaluate the following expression:

# Editor code
# x = float(input("Enter value for x: "))
#
# # Write your code here.
#
# print("y =", y)

# Test code1 x + (1/x)
# x = float(input("Enter value for x: "))
# y = float(x + (1/x))
# print("y =", y)
# Result:2

# Test code
# x = float(input("Enter value for x: "))
# y = float(1 / (x + 1 / (x + (1 / (x + (1 / x ))))))
# print("y =", y)

# LAB3

# prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes
# (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59).
# The result has to be printed to the console.

# Editor code
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# Write your code here.

# Test code ??
#

#
#
# print(123 + 0.0)


# x = input()
# y = int(input())
#
# print(x * y)


# x = int(input())
# y = int(input())
#
# x = x / y
# y = y / x
# print(x)
# print(y)

