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

# Lab1 modul2.2
# Ex1
# string1 = "Astazi ma duc la 'facultate'."
# string2 = '/*\/*\*/*\\*\\\n Python\n \\./\\./\\./'
# string3 = 'P y t h o n'
# print(string1)
# print(string2)
# print(string3, sep='\t')

# Lab1 modul2.2
# Ex2
# Numele_utilizatorului = input('Cum te numesti?')
# Varsta = input('Ce varsta ai?')
# An_curent = 2023
# An_nastere = (int(An_curent) - int(Varsta))
# print(f'Ceau {Numele_utilizatorului}! Deci te-ai nascut in {int(An_curent) - int(Varsta)}')

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

# Lab1 modul2.2
# Ex3

# Student code
# row = input('Introduceti un sir: ')
# print('Lungimea sirului este:', len(row))
# print('Lungimea sirului este: {}'.format(len(row)))
# print(f'Lungimea sirului este: {len(row)}')
# print('Lungimea sirului este: ' + str(len(row)))
#
# row = input('Introduceti un sir:')
# print('Lungimea sirului este:', len(row))
# print('Lungimea sirului este: {}'.format(len(row)))
# print(f'Lungimea sirului este: {len(row)}')
# print('Lungimea sirului este: ' + str(len(row)))

# Lab1 modul2.2
# Ex4
# example function center
# Student code c
# print('*'.center(7,' '))
# print('***'.center(7,' '))
# print('*****'.center(7,' '))
# print('*******'.center(7,' '))

# Student code a

# print("/-\\".center(9, ' '))
# print('//-\\\\'.center(9, ' '))
# print('-------'.center(9, ' '))
# print('\\\\-//'.center(9, ' '))
# print("\\-/".center(9, ' '))

# Student code b
# print("____".center(11, ' '))
# print('/      \\'.center(11, ' '))
# print('/        \\'.center(11, ' '))
# print('/__________\\'.center(11, ' '))

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



# Lab1 modul2.2
# Ex4