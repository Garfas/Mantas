# Lesson 11: Functions ( Part 2 )


# from typing import Any

def check_arguments(mandatory: any, *args, **kwargs) -> None:
    print(mandatory)
    if args:
       print(args)
    if kwargs:
       print(kwargs)


# check_arguments(2, 3, 4, "something", "123", name="mantas", somthing="123")
# check_arguments(101, 102)

# def multiply(x: int, y: int) -> int: #turi but prirasyta int
#     return x* y

# print(multiply(2,3))



# def my_func(n: int) -> callable:
#     return lambda a: a**n # kwargs zymejimas **  Aukščiausiu lygiu jie leidžia funkcijoms priimti neprivalomus argumentus ir suteikia mums lankstumo kviesti funkciją su bet kokiu argumentų skaičiumi. Todėl juos naudodami galime rašyti lankstesnes klases ir modulius.
# my_doubler = my_func(2) #nurodo kuriu laipsniu pakelti
# print(my_doubler(11))

               #PVZ 1 Paprasta daugybos funkcija:

# def multiply(x: int, y: int) -> int:
#     return x * y
# print(multiply(2,3))

            #  galime perrašyti kaip lambda funkciją:

# multiplication= lambda x,y : x * y
# print(multiplication(2, 3))


