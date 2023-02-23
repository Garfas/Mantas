#Date 2023-01-31 Lesson 2: Data Types and Operations
#Integers (sveikieji skaičiai)
#Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}
#How to instantiate a variable as an integer in Python




#How to instantiate a variable as an integer in Python(Kaip „Python“ paversti kintamąjį sveikuoju skaičiumi)
a=8
print(a) #spausdina 8
b=100
print(b) #spausdina 100


#Integer Operations (Sveikūjų skaičių operacijos)
#Operation    Result
# x + y       sum  of x and y (x ir y suma)
# x - y       difference  of x and y (x ir y skirtumas)
# x * y       product  of x and y (x ir y sandauga)
# x / y       quotient of x and y (dalyba x ir y)
#x // y       floored quotient of x and y ( x ir y padalijimas iš apačios)
#x % y        remaindert of x / y (x / y moddulis (likutis))
#x ** y       x to the power y (eksponentija (x pakelta y))
a = 10
b = 20
c = a + b
print(c) #spaudina 30 ( suma)

a = 10
b = 20
c = a - b
print(c) #spausdina -10 (skirtumas)

a = 10
b = 5
c = a * b 
print(c) #spausdina 50 ( sandauga)

a = 10
b = 10
c = a / b 
print(c) #spausdina 1.0 (dalyba )

a = 20
b = 10
c = a // b 
print(c) #spausdina 2 (padalijimas iš apačios)

a = 20
b = 10
c = a % b
print(c) #spausdina 0  (moddulis (likutis))

a = 2
b = 3
c = a ** b
print(c) #spausdina 8  (eksponentija (x pakelta y))







#Date 2023-01-31 Lesson 2: String operations
#String is simply a piece of text, it could be a single letter or the while word or an entire sentence:(Eilutė yra tiesiog teksto dalis, tai gali būti viena raidė, nors žodis arba visas sakinys:)
#ps:.rašant pritn(name[įrašyt skaičių])
#letter = "a" (raidė rašoma tarp " ")
#sentence = "I really enjoy learning python !"(sakinys rašomas tarp " ")
#name = "Code Academy" (vardas rašomas tarp " ")

name = "Code Academy"
print(name[0]) #rašo raide(C)
print(name[1]) #spausdina raide(o)
print(name[11]) #spausdina raide(y)
print(name[-11]) #spausdina raide(0)
print(name[-1]) #spausdina raide(y)
print(name[5 : 12]) #spausdina (Academy)


name = 'Code Academy'
print(name.upper())#pakeičia žodį į didžiąsias raides
print(name.replace('C', 'k'))#pakeičia nurodyta raidę į tą kurią parašom


#Combining of string (String apjungimas)
greeting = 'Hello, my name is'
name = 'Mantas'
completed_greeting = f"{greeting} {name}" # f'{}' (kai nori pridėt kintamuosius)
print(completed_greeting) # print (Hello, my name is Mantas)

# another option Combining of string
greeting = "Hello, my name is"
name = "Mantas Jankauskas"
completed_greeting = greeting + " " + name #vietoj f' kintamojo rašom taip: greeting + " " + name
print(completed_greeting) #print Hello, my name is Mantas Jankauskas

# Conversion of types
#str() Returns a string object
#int()  Returns an integer number
#float() Returns a floating point number
a = "55"
b = int(1.8) #grąžino sveikiajį skaičių 1
c = float(5) #grąžino skaičių po kablelio 5.0
print(a)
print(b)
print(c)

a = 60
b = str(a) # str grąžino eilutės a skaičių 
c = float(a) #grąžino skaičių po kablelio 60.0
print(a)
print(b)
print(c)

a = "Hello" #išspausdino Hello
b = int(9.8) #grąžino sveikiajį skaičių 9
c = float(10) #grąžino skaičių po kablelio 10.0
print(a)
print(b)
print(c)

#User input (vartotojo įvestys)


# Exercises number 1, lesson 2, 2023/01/31
#Sukurkite programą, leidžiančią vartotojui įvesti savo vardą ir amžių
#Apskaičiuoti metus, kuriais vartotojas gimė
#Išspausdinti atsakymą į terminalą
name = str("Mantas")#User name
last_name = str("Jankauskas") #User last name
age = str("37") #user age
country = str("Lithunia")
city = str("Vilkaviškis")
age = 37 #Age in years
today_date = 2023 #The date of January 2023 
corection = 1 #YEARLY CORRECTION FOR MONTHLY ERROR
birth_date = (today_date - age - corection)

print(f"Your name is {name}, you last name is {last_name}, you are {age} years old, your home country {country}, Your place of birth {city}, your date of birth {birth_date}")


# Exercises number 2, lesson 2, 2023/01/31
#1 Sukurti programą, leidžiančią vartotojui įvesti visą sakinį
#3 spausdinti kas antrą sakinio raidę

x = 'The fastest car' #sentence x
z = 'Koenigsegg One' #sentence z
e = (x + z) #1
w = 'The fastest car  koenigsegg One' #2 make sentence backwards
print(w[::-1]) #print
print(e)

#2 išspausdinti sakinį atbuline tvarka
x = 'The fastest car' #sentence x
z = 'Koenigsegg One' #sentence z
e = (x + z) 
w = 'The fastest car  koenigsegg One' #sentence backwards
print(w[0::-10]) #every second letter in the sentence NEPADARYTA ISSIAISKINT
#print(w[::-1]) #print
#print(e)

#3 spausdinti kas antrą sakinio raidę



##Create program that allows user to enter text (Sukurkite programą, kuri tikisi, kad naudotojas įves du skaičius)
#print outcome (atspausdint atsakyma)
x = (25)
y = (10)
e = (5)
z =  x * y % e
print(z)  

#Convert that text to Leet speak 1337" (konvertuot teksta į Lett speak 1331")
find = ('M', 'a', 'n', 't', 'a', 's') #rasti
repl = ('1', 's', 'p', '&', '$', '*')#pakeisti
print(find, repl)
