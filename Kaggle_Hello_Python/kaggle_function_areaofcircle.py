# program to define a function to calculate the area of a circle
def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    pi = 3.14159
    return pi * (radius ** 2)

print("Please enter the radius of the circle:")
radius = float(input()) # input from user

print("Area of the circle with radius", radius, "is:", area_of_circle(radius))
# the same code using f-string for formatting
# f-string evaluates the expressions inside the curly braces at runtime and inserts the result into the string
print(f"Area of the circle with radius {radius} is: {area_of_circle(radius)}")