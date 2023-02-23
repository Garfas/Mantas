#main_module

# Create a simple calculus program as a script and as module.
# Create a program with 3 different modules:
# first, to do basic tasks with strings
# second, basic tasks with lists.
# third, basic tasks with numbers
# Import them as modules to the main.py module and show calculations.
#Sukurkite paprastą skaičiavimo programą kaip scenarijų ir kaip modulį.

# Sukurkite programą su 3 skirtingais moduliais:
# pirma, atlikti pagrindines užduotis su eilutėmis
# antra, pagrindinės užduotys su sąrašais.
# trečia, pagrindinės užduotys su skaičiais
# Importuokite juos kaip modulius į main.py modulį ir parodykite skaičiavimus.



import calculus_module
import string_module
import list_module
import number_module

# # Calculus calculations
print(calculus_module.add(2, 3)) #addition (add) sudėtis
print(calculus_module.subtract(5, 2)) #subtraction (sub)atimtis
print(calculus_module.multiply(4, 6)) #multiplication (prod) daugyba
print(calculus_module.divide(10, 2)) #division (div)  dalybas

# # String calculations
print(string_module.reverse_string("My son's name is Dorianas")) # printina atvirkštine tvarka
print(string_module.count_vowels("My son's name is Dorianas")) # count_wowels skaičiuok_balses
print(string_module.count_consonant("My son's name is Dorianas")) #count_consonant skaičiouk_priebalses


# # List calculations
my_list = [3, 5, 1, 2, 7]
print(list_module.get_length(my_list)) #suskaičiuoti my_list ilgį (kiek liste yra simbolių)
print(list_module.sort_list(my_list)) # surikiuoti nuo mažiausio iki didžiausio
print(list_module.get_sum(my_list)) #gauti visų skaičių sumą

#Number calculations
print(number_module.is_even(4)) #jeigu yra lygus 4 spausdinti True
print(number_module.is_odd(7))
print(number_module.square(5))
