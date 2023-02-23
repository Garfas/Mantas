#Lesson 5 
#Date 2023/02/06
#Data Structures and dictionary method

# Dictionary  method
# nr.1 clear(), Pašalina visus elementus iš žodyno
# nr.2 copy(), Grąžina žodyno kopiją
# nr.3 fromkeys(), Grąžina žodyną su nurodytais raktais ir reikšme
# nr.4 get(), Grąžina nurodyto rakto reikšmę
# nr.5 items(), Grąžina sąrašą, kuriame yra kiekvienos raktų reikšmių poros eilutė
# nr.6 keys(), Grąžina sąrašą, kuriame yra žodyno raktai
# nr.7 pop(), Pašalina elementą nurodytu raktu
# nr.8 popitem(), Pašalina paskutinę įterptą rakto-reikšmių porą
# nr.9 setdefault(), Grąžina nurodyto rakto reikšmę. Jei rakto nėra: įdėkite raktą su    nurodyta reikšme
# nr.10 update(), Atnaujina žodyną su nurodytomis rakto-reikšmių poromis
# nr.11 value(), Grąžina visų žodyne esančių reikšmių sąrašą

# coutnries_and_capital = {
#     'Lithuania' : 'Vilnius',
#     'Poland' : 'warsaw',
#     'Latvia' : {
#         'capital' : 'riga',
#         'population' : 2000000,
#     }
# }

# print (coutnries_and_capital['Latvia']['population'])

# print(list(coutnries_and_capital.keys()))
# print(list(coutnries_and_capital.values()))

# print (coutnries_and_capital)
# new_country = {'spain' : 'madrid'}
# coutnries_and_capital.update(new_country)
# print(coutnries_and_capital)


# coutnries_and_capital.pop('Latvia')
# print(coutnries_and_capital)


# my_set = {1, 2, 3, 4, 'My new message'}
# print(my_set [0])                            nespausdin nes negali keisti


def Merge(dict_one, dict_two, dict_three):#Metodas merge() atnaujina  DataFrame turinį sujungdamas juos kartu,\\
# \\naudodamas nurodytąmetodą. Naudodami parametrus valdykite, \\
# \\kurias vertes palikti, o kurias pakeisti.

 result = dict_one | dict_two  | dict_three
 return result
# dictionary
dict_one = {1:10, 2:20}
dict_two = {3:30, 4:40} 
dict_three = {5:50, 6:60}
dict_four = Merge(dict_one, dict_two, dict_three)
print(dict_four)
