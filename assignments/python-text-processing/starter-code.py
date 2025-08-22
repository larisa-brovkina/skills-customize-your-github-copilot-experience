# Starter code for Python Text Processing assignment

# Task 1: Text File Reader & Word Counter
# Fill in the code below to read a file and count lines, words, and characters.

filename = input("Enter the filename: ")
try:
    with open(filename, 'r') as file:
        text = file.read()
        # TODO: Count lines, words, and characters
        # Print the results
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")

# Task 2: Text Search and Replace
# You can add your code for the second task below.
