#Lesson 8 Loops 2023/02/09

# #while loops 
#  # Naudodami while ciklą galime vykdyti logiką tol, kol sąlyga yra teisinga
# i = 0
# while i < 10:
#   print(i)
#   i += 1 #nepamiršt padidinti i, kitaip ciklas tęsis amžinai

#//////////
# endless loop     (nesibaigiantis ciklas (infinite loop))
#Šis ciklas neleis naudotojui kaip argumentą perduoti tuščios vietos, visada lauks, kol bus kas nors įvesta.

# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input) != 0:
#         break
# print(f"You entered {user_input }")

#////////////
#For loop

# names = ["Albert", "Tom", "Leonardo"]
# for name in names:
#     print(f"Greetings, {name}")

#/////////
# while True:
#     print('zalgiris')
#     time.sleep(1)

# apples = 0
# while apples <= 10:
#     print(f'gathered apples so far: {apples}')
#     apples += 1



#////////

# names = ['marius', 'Tomas']
# for names in names: #visada tiksliai nurodyt kas tai
#     print(names)

# ////////
# for letter in 'Mantas':
#     print(letter)

# #/////////////
# for x in range(0, 10, 2):
#     #doing somethin else
#     print(x)

#/////////
# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for_in range(0, 5)

# for number in my_number_list:
#     print(number)
#     if number >= 9:
#      break
#      for_in range(0, 10)
    
#     # Doing something else
#     print('somethin hapened')


# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in my_number_list:
#     if number == 7:
#         continue
#     print(number)
    
#//////////////////////
# i = 0
# while i < 6:
#     i += 1 # i = i +1
#     print('hey yo')
#     if i == 3:
#      print('I am here')
#      continue
# print(i)


#//////////////////
#Create a variables containing strings for username and password


# my_dict_password = ('6666')
# my_dict_username = ('Zose')
# while  True: 
#     my_dict_username = input('Enter username:')  #username input
#     my_dict_password = input('Enter password:') # pasword input
#     if my_dict_password == '6666' and my_dict_username =='Zose': #username and password data
#      print('Access granted')
#      break
#     else:
#         print('Access denied')
# print('Enter correct username and password')

#/////////////////////
# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.
# show only letters that exists




