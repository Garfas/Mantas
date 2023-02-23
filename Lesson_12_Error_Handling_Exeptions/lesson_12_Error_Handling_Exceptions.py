

# def print_name_age_with_arguments(age: int, name: str = "Mantas", *args, **kwargs)-> None: # None rasomas kada nieko negrazinas non return
#     print(f"{name}, {age}")
#     print(f"free arguments: {args if args else 'args not been improvide'}, free key arguments: {kwargs if kwargs else 'kwargs not been inprovide'}")

# print_name_age_with_arguments(25, "Mantas", "Argument", street = "Gedimino")


# from typing import Union

# def divider(number: Union[float, int]) -> Union[float, int] :
#     return number / 2 if isinstance(number, float) else number // 2 



# try:
#     my_divider_number = divider('0')
#     print('my_divider_number')
# except TypeError:
#     print('We are f*cked uo!')
# except ZeroDivisionError:
#     print("Never delete with 0")





# def divider(number: Union[float, int]) -> Union[float, int]:
#     try:
#         return number / 2 if isinstance(number, float) else number // 2 
#     except TypeError:
#         print('Wrong type received')
    # except Exception as e:
    #     print(f'Error  {e}')



# def physics_is_fun(temp_c: float, pressure_mbar: float, time_utc:int, weight_kg: float) -> None:
#     pass
# physics_is_fun(temp_c= 55.87, pressure_mbar= 26.58, time_utc= 1258996, weight_kg= 458.6 )







# 1. Create at least 5 different functions and try to handle at least 5 built-in Python Exceptions.
# 2. Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.
# 3. Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication. Handle all possible errors that may occur.
# 4. Update previous task with possible raise exception.


# //////

# def my_function(father, grandfather, child) -> None:    
#     print("the oldest person is " + grandfather)
# my_function(father = "Jonas", grandfather = "Vitas", child = "Dorianas") 




# def multipleNum(num1 : any) -> bool:
#     return num1 * 11
# result = multipleNum(9.5)
# print(result)
# if result > 9.5:
#     print('result is great,')


# 2. Create a function what would include full cycle of error handling (try/except/else/finally) with real world scenario example.

# Try, except.

# def divide(x, y):
#     try:
#         result = x // y
#         print("OK ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("The answer is not possible ! You are dividing by zero ")
# divide(50, 2)
# divide(100, 0)


#  Try, except, else.

# def divide (a, b):
#     try:
#         result = a // b
#     except ZeroDivisionError:
#         print("The answer is not possible ! You are dividing by zero ")
#     else:
#         print("OK ! Your answer is :", result)
# divide(10, 5)
# divide(6,0)


#Try, except, else, finally.

def divide(x, y):
    
#     try:
#         result = x // y
#     except ZeroDivisionError:
#             print("The answer is not possible ! You are dividing by zero ")
#     # except Exception as e:
#             # print(f'Error  {e}')
#     else :
#             print("OK ! Your answer is :", result)      
#     finally:       
#             print("always allowed")

# divide (10, 5)
# divide(6, 0)

#////////////////
