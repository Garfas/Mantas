

# from datetime import date


# class Person:
#     description: str = "A simple normal human being"

#     def __init__ (self, name: str, surname:str,):  # (self) gali uzvadint kaip nori reiksmes programai neturi
#         self.name: str = name
#         self.surname: str = surname


#     #hello, my name is, <name>
#     def greet(self): 
#         return f"Hello my name is {self.name}"
    
#     def walk_away(self):
#         return f"{self.name} is walking away..."
    
#     def calculate_days_left_till_black_friday(self):
#         #get tuday date
#         #initialize black friday date
#         #return black_friday_date - todays_date
#         today = date.today()
#         black_friday_date = datetime.date(2023, 11, 24)
#         delta = black_friday_date
#         return delta.days
    
#     def get_eye_color(self, eye_color: str = "brown") -> str:
#         return eye_color
    
#     def __repr__(self) -> str:
#         return f'Person: {self.name}-{self.surname}'
    
#     def __str__(self) -> str:
#         pass


# person1 = Person("Mantas", "Jankauskas")
# print(person1.calculate_days_left_till_black_friday())
# print(person1.get_eye_color("blue"))

# class house:
#     #class attribute
#     location: str = "Somewhere near Trump Tower"

#     def __init__(self, cost: int = 50000, age: float = 10.5):
#         self.cost: int = cost
#         self.age: float = age

#     #instance method
#     def get_cost(self) -> int:
#         return f"The hous cost is: {self.cost}"
    
#     #another instance method
#     def get_age(self) -> float:
#         return f"The hous ege is: {self.age}"
    
#     #yet another instance method
#     def get_hause_color(self, colour: str = "White") -> str:
#         return f"The hause colour is {self.age}"
    

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


class Spreadsheet:
    def __init__(self):
        self.data = []

    def load_from_file(self, file_path):
        with open(file_path) as f:
            self.data = [list(map(float, line.split(','))) for line in f]

    def get_cell(self, row, col):
        return self.data[row][col]

    def set_cell(self, row, col, value):
        self.data[row][col] = value

    def add(self, row1, col1, row2, col2):
        calc = Calculator()
        return calc.add(self.get_cell(row1, col1), self.get_cell(row2, col2))

    def subtract(self, row1, col1, row2, col2):
        calc = Calculator()
        return calc.subtract(self.get_cell(row1, col1), self.get_cell(row2, col2))

    def multiply(self, row1, col1, row2, col2):
        calc = Calculator()
        return calc.multiply(self.get_cell(row1, col1), self.get_cell(row2, col2))

    def divide(self, row1, col1, row2, col2):
        calc = Calculator()
        return calc.divide(self.get_cell(row1, col1), self.get_cell(row2, col2))
    
spreadsheet = Spreadsheet()

# Load data from a file
spreadsheet.load_from_file('data.csv')

# Get cell values and perform calculations
a1 = spreadsheet.get_cell(0, 0)  # a1 = 2.0
b1 = spreadsheet.get_cell(0, 1)  # b1 = 3.0
c1 = spreadsheet.add(0, 0, 0, 1)  # c1 = 5.0
d1 = spreadsheet.subtract(0, 0, 0, 1)  # d1 = -1.0
e1 = spreadsheet.multiply(0, 0, 0, 1)  # e1 = 6.0
f1 = spreadsheet.divide(0, 0, 0, 1)  # f1 = 0.6666666666666666

