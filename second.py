#methods in python

# string interpolation
# They are prefixed with 'f' and use curly braces {} to enclose the variables that will be formatted.
name = "Vedika"
age = 20
print(f"My name is {name} and I am {age} years old.")

# str.format() method
name = "John"
age = 50
print("My name is {} and I am {} years old.".format(name, age))

# %operator
name = "Johnathan"
age = 30
print("My name is %s and I am %d years old." % (name, age))
# “My name is %s and I am %d years old.“: This is a string that includes format specifiers:
# %s: This is a placeholder for a string.
# %d: This is a placeholder for an integer.


# addition during printing 
x = 10
y = 20
print(f"The sum of x and y is {x+y}.")

# here used r so that /n is not treated as a new line function
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)