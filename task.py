import sys  # used to import the sys module
year = input("Enter your birth year: ") # user input
print(type(year))
 # The function to determine size of user input
age = 2024 - float(year)
size_year = sys.getsizeof(year) 
print("your age=", age)
print(type(age))
height = input("Enter your height in meters:") # user input
print(type(height))
 # The function to determine size of user input
size = sys.getsizeof(height) 
print("size of height", size,)

