# # Modul3 - stringuri si metode de folosire a lor
# Exemplu1
# my_added_string = 'add me'
# string1 = 'Hello World\n'
# string2 = r'Hello World\n'
# string3 = '''
#
# Hello World
#
# '''
# string4 = f'Hello World {my_added_string}'
# string5 = rf'Hello World {my_added_string}'
# print(string1, string2, string3, string4, string5, sep='\t')

# Exemplu2

# string_with_quotes = 'my string \''
# print(string_with_quotes)

# Lab1 Module 2.2 - Operații cu șiruri
# Ex1
# string1 = "Astazi ma duc la 'facultate'."
# string2 = '/*\/*\*/*\\/*\\\n Python\n \\./\\./\\./\\./'
# string3 = 'P y t h o n'
# print(string1)
# print(string2)
# print(string3, sep='\t')

# Lab1 Module 2.2 - Operații cu șiruri
# Ex2
# Numele_utilizatorului = input('Cum te numesti?')
# Varsta = input('Ce varsta ai?')
# An_curent = 2023
# An_nastere = (int(An_curent) - int(Varsta))
# print(f'Ceau {Numele_utilizatorului}! Deci te-ai nascut in {int(An_curent) - int(Varsta)}', end='.')

# String methods
# my_string = 'Hello World, {}'
# my_string = my_string.format('Python')
# print(my_string)

# my_string = 'Hello World, {1} {0}'
# my_string = my_string.format('Python', 'User')
# print(my_string)

# my_string = 'Hello World, {arg1} {arg2}'
# my_string = my_string.format(arg1='Python', arg2='User')
# print(my_string)

# my_string = 'Hello World, {arg1} {arg2}'
# print(len(my_string))

# Lab1 Module 2.2 - Operații cu șiruri
# Ex3

# Student code
# row = input('Introduceti un sir: ')
# print('Lungimea sirului este: {}'.format(len(row)))
# print(f'Lungimea sirului este: {len(row)}')
# print('Lungimea sirului este: ' + str(len(row)))
# print('Lungimea sirului este:', len(row))


# Lab1 Module 2.2 - Operații cu șiruri
# Ex4
# example function center

# Student code a
# print("/-\\".center(9, ' '))
# print('//_\\\\'.center(9, ' '))
# print('-------'.center(9, ' '))
# print('\\\\_//'.center(9, ' '))
# print("\\_/".center(9, ' '))

# print('/-\\'.center(33, ' '))
# print('/---\\'.center(33, ' '))
# print('/-----\\'.center(33, ' '))
# print('0---------0'.center(33, ' '))
# print('\\-----/'.center(33, ' '))
# print('\\---/'.center(33, ' '))
# print('\\-/'.center(33, ' '))

# Student code b
# print("____".center(11, ' '))
# print()
# print('/    \\'.center(11, ' '))
# print('/______\\'.center(11, ' '))

# Student code c
# print('*'.center(7, ' '))
# print('***'.center(7, ' '))
# print('*****'.center(7, ' '))
# print('*******'.center(7, ' '))





# Slice - Taierea unui sir

# my_string = 'Hello World'
# print(my_string[0])
# print(my_string[len(my_string) - 1])

# my_string = 'Hello World'
# print(my_string[0])
# print(my_string[len(my_string) - 1])
# print(my_string[-1])

# 'Hello World'
# 0123456789
# -10-9-8-7-6-5-4-3-2-1
# Index
# my_string = 'Hello World'
# print(my_string[len(my_string) - 1])
# print(my_string[-1])
# print(my_string[-3])

# 'Hello World'
# 0123456789
# -10-9-8-7-6-5-4-3-2-1
# my_string = 'Hello World'
# print(my_string[0:3])
# print(my_string[-5:-1])

# 'Hello World'
# 0123456789
# -10-9-8-7-6-5-4-3-2-1
#Slice
# my_string = 'Hello World'
# print(my_string[0:3])
# print(my_string[-5:-1])
# print(my_string[-5:])
# print(my_string[:-2])
# print(my_string[:])
# Result
# Hel
# Worl
# World
# Hello Wor
# Hello World

# Step
# my_string = 'Hello World'
# print(my_string[::1])
# print(my_string[::-1])
# print(my_string[::-2])
# print(my_string[0:7:1])
# Result
# Hello World
# dlroW olleH
# drWolH
# Hello W



# Module 2.2 - Operații cu șiruri
# Ex5

# str1 = input('Enter a word:')
# print('a:', str1)
# print('b:', str1[::-1])
# print(bool(a == b))

# if (a) == (b):
#     print('Palindrome: True')
# else:
#     print('Palindrome: False')




# Module 2.2 - Operații cu șiruri
# Ex6

# print('Hello Python')
# print('Ana are mere')
# print('Pizza Party')
# print()
# print('Hello', 'Python', sep="_")
# print('Ana', 'are', 'mere', sep="_")
# print('Pizza', 'Party', sep='_')
# print()
# print('Hello Python', end='.\n')
# print('Ana are mere', end='.\n')
# print('Pizza Party', end='.\n')
# print()
# print('Hello' * 4, 'Python')
# print('Ana' * 4, 'are mere')
# print('Pizza' * 4, 'Party')

# Module 2.2 - Operații cu șiruri
# Ex7

# var_a = 5.
# var_b = 5
# var_c = "ana"
# print(var_a)
# print(var_b)
# print(var_c)
# print()
# print('Location of a is:', hex(id(var_a)))
# print('Location of b is:', hex(id(var_b)))
# print('Location of c is:', hex(id(var_c)))
# print()
# print('Type of variable a is:', type(var_a))
# print('Type of variable b is:', type(var_b))
# print('Type of variable c is:', type(var_c))
