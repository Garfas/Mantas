# Find all of the numbers from 1-1000 that are divisible by 6.
# Find all number from 1-1000 that have 9 in them.
# Given string: text = 'In this lecture we will review some additional functionalities of python built-in data structures.' calculate how many words have letter 'e' in it.
# Given the same string as in previous exercise: calculate count of letters that have more than 5 characters.
# Write a program that checks if given number is a perfect square.

#                ///////papildomas skaitymas//////////
# [Real Pyhton comprehensions](https://realpython.com/list-comprehension-python/)
# [Real Python math](https://realpython.com/python-math-module/)

# from optparse import Values


# squares = []
# for number in range(10):
#     print(number)
#     if number == 5:
#        squares.append(number * number)
# print(f' first: {squares}')

# we have 5 name

# names = "tomas , marius, gytis, roma, Igle"
# names = []  
# for names in name"
#     if(names) >= 5:
#        count = count + 1;  

# print("names" + str(count));  

# squares = [number * number for number in range(10) if number == 5]
# print(f'second: {squares}')

# my_smth = {
#     'Alpha': 1,
#     'Beta': 2,
# }
# squares = {i : i* i for i in range(10) if i <= 6}
# print(squares)

# d=dict()
# for x in range(1,16):
#     d[x]=x**2
# print(d) 

#Create a dictionary with 5 kay:value pairs, Keys must be strings, values must be numbers double digits(int)
# Use dictionary comprehension to create a new dictionary where keys are the same keys as your currents ones just all cappital letters, 
# and values are in reverse order. (25 -> 52)

names = {
    'Marius':'22',
    'Tomas':'35',
    'kipras':'11', 
    'zose':'44', 
    'marta':'60'
    }
# my_dict = {name.upper(): int(str(number)[::-1]) for (name, number) in names.items()}
# # print(my_dict)
# my_new_dict ={}
# for name, number in names.items():
#     my_new_dict[name.upper()] = int(str(number)[::-1])
# print(my_new_dict)




# values = ['a', 'b', 'c']
# for count, value in enumerate(values):
#     print(count, value)
