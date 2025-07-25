# program to demonstrate the use of help function
help(abs)
print("the absolute value of -10.5 is ", abs(-10.5))
# test round function
help(round)
rounded_value = round(3.14159, 2)
print("The rounded value of 3.14159 to 2 decimal places is", rounded_value)
rounded_value = round(3.14159, None)
print("The rounded value of 3.14159 to the nearest integer is", rounded_value)
rounded_value = round(31.14159, -1)
print("The rounded value of 3.14159 to the nearest 10 is", rounded_value)