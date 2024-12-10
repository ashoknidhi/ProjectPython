#Prints the first value if it is true.  If not, it prints the second value
print(0 or 1) # prints 1 because 0 is considered to be false
print(False or 'hey') #prints hey as the first value if False
print('hi' or 'hey') #prints first value hi as it is true
print([] or False) #prints False as the first value [] is considered to be false in python
print(False or []) #prints [] as the first value is False
print("------------------")
# prints the second value only if the first value is True, it nof, it prints the first value
print(0 and 1) #Prints 0 as it is false, does not check the second value
print(False and 'hey') #prints the first value 'False' as it is considered to be false, does not continue to the second value
print('hi' and 'hey') #the first value 'hi' is considered to be true, hence, python continues to the second value and prints 'hey'
print([] and False) #prints [] as it is considered to be false in python, does not progress to check the second value
print(1 and 0) #first value, 1 is true hence it continues to the second value and prints it