# CSC_120 Logbook : Pg 9, Exercise 1

# Start Program

name_file = input("Input your name ==> ") # Prompts user for input

# Get the dimensions of the terminal window
import shutil
cols, rows = shutil.get_terminal_size()

# Print the name vertically
for count in range(rows):
                print(name_file)
                
                # Print the name horizontally
                print(name_file * (cols // len(name_file)), end="")

# End Program
