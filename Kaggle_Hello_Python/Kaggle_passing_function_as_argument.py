# Program to demonstrate passing functions as arguments to other functions
def square(num):
    """Returns the square of 5."""
    return num * num

def cube(fn, num = 5):
    """Returns the cube of x."""
    return fn(num) * num

number = input("Inpute the number whose cube you want to calculate: ")
print("You entered: ", number)
print(type(number))
print("The square of ",number, "is: ", square(int(number)))
print("The cube of ", number, "is:", cube(square, int(number)))   