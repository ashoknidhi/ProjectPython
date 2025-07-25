# program to return the number with 2 decimal places
def format_number(num, places):
    return (round(num, places))
  
print(format_number(3.14159, 2))  # Output: 3.14
print(format_number(3.14159, 3))  # Output: 3.141
print(format_number(3.14159, 4))  # Output: 3.1416
print
print(format_number(3.14159, 0))  # Output: 3.0
print(format_number(23.14159, -1))  # Output: 20.0 (rounds off to nearest 10)
print(format_number(123.14159, -2 ))  # Output: 100.0 (rounds off to nearest 100)


