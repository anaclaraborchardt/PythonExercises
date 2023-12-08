# This is a sample Python script.
from Exercise2 import exercise2
from Exercise3 import exercise3
from exercise4 import exercise4


def my_function():
    name = input('Write your name: ')
    year_str = input('What is your birth year? ')

    year = int(year_str)

    age = 2023 - year

    print("Your name is " + name)
    print(age)

#all exercise:
# my_function()

# exercise2()

# exercise3()

exercise4()
