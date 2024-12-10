#program to understand the capability the os standard library provides the python program
#importing and using this standard library provides the user the capability to interface with the OS Python is hosted on
import os

# print the name of the os
print(os.name)

# catch errors from OS and use them
try:
    # if the file does not exist, OS throws an error
    filename = 'test.txt'
    fileopen = open(filename, 'r')
    text = fileopen.read()
    fileopen.close()

# control jumps to the except statement if the program flow encounters any os errors in the try block
except IOError:
    print('Problem reading', filename)