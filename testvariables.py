#TestVariables - exercise talks about casting or type conversion along with some fucntions that help convert variables and type checking
name = "Ashok"
age = 50 # note that this is an integer
agestr = "50" # note that this is a string
my_location = "Singapore"
__hobby__ = "Wildlife"
print ("My name is " + name + " I live in " + my_location + " and " + __hobby__ + " is my hobby, and my age is ", age)
print ("My name is " + name + ". I am ", age, " years old") # The concatenation operator '+' can be used only with strings
# 'type' function helps determine the type of variable
print (type(name))
print (type(age))
# check if 'name' is a variable of type 'str', if it is of type str, the print statement returns 'True'
print (type(name) == str)
# the same can be achieved using the function 'isinstance'
print(isinstance(name, str)) #returns true
print(isinstance(age, str)) #returns false as 'age' is a variable of type int
print(isinstance(agestr, int)) #returns false as agestr is a string and not an int
print(isinstance(int(agestr), int)) #returns true as the string agestr is initially converted to int and then the type is checked