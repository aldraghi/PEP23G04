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

# Lab1 modul2.2
# Ex3

# sir = input('Introduceti un sir:')


# String methods
# my_string = 'Hello World, {}'
# my_string = my_string.format('Python')
# print(my_string)

# my_string = 'Hello World, {1} {0}'
# my_string = my_string.format('Python', 'User')
# print(my_string)

my_string = 'Hello World, {arg1} {arg2}'
my_string = my_string.format(arg1='Python', arg2='User')
print(my_string)