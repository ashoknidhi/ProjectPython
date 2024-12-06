book = "Learning Python"
phone = "Samsung"

# printing with concatenation operator
print ("Learning Python" + " is a good book\n")
print (book + " is a good book\n")
book += " is a good book"
print (book)

# strings running into multiple lines and printing into multiple lines
print (""" This 
is 
a 
very 


good book\n""")

# quotes do not matter - whether a double quote or a single quote is used
print ('This is a good book\n')
print ('''\n This is
a

good book\n''')

#Built in methods
print ("ashok".upper())
print ("ASHOK".lower())
print ("asHOk".lower())
print ("ashok's life".title()) # converts the first alphbet to capital
print ("ashok".islower()) # checks and returns bool - either a True or False

# isalpha - to check if the string comprises of only characters and is not empty
print ("\n.........\n")
print("ashok".isalpha()) #returns true as the string has only characters
print("ashok2020".isalpha())
print ("\n.........\n")
# isalnum - to check if the string comprises or characters or digits and is not empty
print("ashok2020".isalnum()) #returns true as the string comprises of characters and digits only
print("ashok20**".isalnum()) #returns false due to the special characters
print ("\n.........\n")
# isdecimal - to check if the string comprises of digits and is not empty
print("123456".isdecimal()) #returns True as the string comprises of decimals only
print("ashok23".isdecimal()) #returns as the string has both decimals and characters
print ("\n.........\n")
# startswith - to check if the string strats with a specific substring
print("ashok".startswith("as")) #returns True as ashok starts with as
print("ashok".startswith("ok")) #returns false as the string ashok does not start with ok
print ("\n.........\n")
# endswith - to check if the string ends with a specific substring
# replace - to replace part of a string
# split - to split a string on a specific character separator
print("Good Boy".split(" "))
# strip - to trim the white spaces from a string
print("Good Boy".strip())
# join - to append new letters to a string
# find - to find the position of a substring

print ("\n")
#Global functions with strings
print (len(phone)) #prints the length or number of characters in the string.  
print ("\n")
print("am" in phone) #returns true as the string 'am' is part of the string 'samsung'

#Escape characters
# adding double quote - use a front slash
print ("enter your \"name\": ")

#Accessing specific characters in a string
print ("\n")
print (phone[0])
print (phone[-1]) #returns the last character
print (phone[-2]) #returns the last but one character
print (phone[0:3]) #returns the characters starting from 0, and 3 characters are returned.  in this case it will be 'sam'