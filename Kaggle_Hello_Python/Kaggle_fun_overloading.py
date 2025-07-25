# program to demonstrate default arguments and overriding values of default arguments
def greet(name = "Guest"):
    print("Hello", name)
# prints the output with default argument
greet()

# modifying the same function to override the default argument
greet(name = "Doctor")

# As the function greet has a single default argument, it can be overloaded and called without explicitly naming the argument
greet("Engineer")
# prints the output with default argument