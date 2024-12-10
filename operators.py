# program to understand various operators in python and their usage
age = 5 # assignment operator
#Arithmetic Operator
# +, -, *, /, %, ** and //
# // is the floor division - rounds down the nearest whole number
# % is the remainder
# ** is the raised to power operator
# Examples
squr = age ** 2
print ("The square of ", age, " is ", squr)
flrdiv = age // 2
print ("Floor division of ", age, " when divided by 2 is ", flrdiv)
rmdr = age % 2
print ("Remainder from dividing ", age, " by 2 is ", rmdr)

# combining arthimetic operators with assignment operators
age +=4
print (age)
age -=1
print (age)
age *=2
print (age)
age /=4
print (age)
age **=2
print (age)

#----------------------------------------------------------------------
# Comparison Operators
# ==, !=, <=, >=, >, <
print ("\n condition operators \n")
print (age == 16) # True as age is equal to 16
print (age != 15) # True as age is not equal to 15, age is 16
print (age <= 15) # False
print (age >= 15) # True
print (age < 18) # True

#---------------------------------------------------------------------
# Boolean Operators
# or, and and not
print ("\n Boolean Operators \n")
condition1 = True
condition2 = False

print (not condition1) # returns false
print (condition1 or condition2) # returns true as one of the conditions is true
print (condition1 and condition2) # returns false as one of the conditions is false
print ("\n")

#or operator returns the value of the first operator if it is not false or returs the second operator value irrespective of whether it is false or true
print (0 or 1) # returns 1 as 0 is considered false
print (False or 'hey') # returns hey as first value is 'False'
print ('hi' or 'hey') # returns hi as it is true
print ([] or False) # returns the second operator 'False' as the first operator [] is considered to be false.
print (False or []) # returns the second operator '[]' as the first operator 'False' is considered to be false

#and operator checks the second value only if the first value is true. if the second value is true, it returns the second value, if not, it returns the first value
print ("\n")
print (0 and 1) #returns the first value '0' as it is false.  Does not check the second value as the first value is false
print (1 and 0) # first value is true, hence checks the second value. Second value is false.  system returns second value '0'
print (False and 'hey') # returns 'False' as the first value is false
print ('hi' and 'hey') # First value is true.  returns the second value 'hey'
print ([] and False) #First value is false hence returns first value []
print (False and []) #First value is False, returns first value 'False'

#------------------------------------------------------------------------
# Bitwise Operators
# &: binary and, |: binary or, ^: exclusive or, ~: binary not, << Shift left, >> shift right
print ("\n")

#----------------------------------------------------------------------
# Identity operator 'is' - to compare two objects and return true if they are similar
# Membership operator 'in'abs - to check in the given object is the member of the list or other sequence

# Ternery operator
# if a == 4 then b = c else b = d
# return True if age > 18 else False