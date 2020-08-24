# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Shows a simple example of how Python error handling for
#              exceptions. Shows a simple example of Python pickling/un-pickling
#              features using a pre-written dictionary.
# ChangeLog (Who,When,What):
# Hyo Park, 08.20.2020,Created started script
# ---------------------------------------------------------------------------- #

# Exceptions

def main():
    # Pre-exception handling example commented out
    # Get two numbers
    # num1 = int(input('Enter a number: '))
    # num2 = int(input('Enter a second number: '))
    # Divide num1 by num2 and display the result
    # result = num1 / num2
    # print(num1, 'divided by', num2, 'is', result)

    try:
        # Get two numbers
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter a second number: '))
        result = num1 / num2
        # Exception handling for ZeroDivisionError
        print(f"{num1} divided by {num2} is {result}.")
    except ZeroDivisionError:
        print("A number cannot be divided by a zero!")
    else:
        print("There was no ZeroDivisionError detected.")


# Call the main function.
main()
print()

# Pickling

# Imports pickle module
import pickle

# Dictionary of my favorite Seattle SuperSonics players
fav_sonics = {'PG': 'Gary Payton',
              'SG': 'Ray Allen',
              'SF': 'Detlef Schrempf',
              'PF': 'Shawn Kemp',
              'C ': 'Sam Perkins'}


# Function to write dictionary to .dat file
def save_data_to_file(file_name, dic_data):
    output_file = open(file_name, 'wb')
    pickle.dump(dic_data, output_file)
    output_file.close()


# Calling function to write dictionary to a .dat file
save_data_to_file("sonics.dat", fav_sonics)


# Function for un-pickling dictionary from .dat file
def read_data_from_file(file_name):
    obj_file = open(file_name, "rb")
    dic_of_data = pickle.load(obj_file)
    obj_file.close()
    print("My all-time favorite Seattle SuperSonics players are: ")
    for key, value in dic_of_data.items():
        print(f"{key} : {value}")


# Printing dictionary saved in .dat file
read_data_from_file("sonics.dat")

# Pickle a file down to hard drive and bring it back up
