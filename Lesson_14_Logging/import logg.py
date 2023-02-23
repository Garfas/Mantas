# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# # Funkcija kuri nurodo kokia operaciją atliksim
# def perform_operation(a, b):
#     result = a + b
#     logging.debug(f"Operation performed: {a} + {b} = {result}")
#     return result

# # funkcija su išvestimi
# result = perform_operation(2, 3)

# print(f"The result is {result}")



import logging
a = 10
b = 0
try:
  c = a / b
except Exception as e:
  logging.error("Exception Occurred", exc_info=True)  ## At default it is True