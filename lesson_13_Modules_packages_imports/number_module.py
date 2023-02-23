#number_module

# | is_even(skačius) grąžina True, jei įvesties skaičius yra lyginis,
# | kitu atveju - False. Tai atliekama tikrinant, ar likusioji skaičiaus dalis, padalinta iš 2, yra lygi 0.
def is_even(num): 
    return num % 2 == 0 #likutį
# |is_odd(skaičius)  grąžina True, jei įvesties skaičius yra nelyginis skaičius, o 
# |kitu atveju - False. Tai atliekama tikrinant, ar likusioji skaičiaus dalis, padalinta iš 2, nėra lygi 0.
def is_odd(num):
    return num % 2 != 0 # nelygu
# |kvadratas(skaičius) grąžina įvesties skaičiaus kvadratą, kuris 
# |apskaičiuojamas pakeliant skaičių iki 2 laipsnio, naudojant operatorių **.
def square(num):
    return num ** 2 #kelimas laipsniu