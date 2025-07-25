# Program to demonstrate lists in python
Planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(Planets[0]) # the first element starts from index 0
print(Planets[0:3])  # Slicing the list to get the first three planets
print(Planets[3])  # Accessing the fourth planet
print(Planets[-1])  # Accessing the last planet using negative indexing
print(Planets[:3]) # if the start index is not specified, it defaults to 0
print(Planets[3:])  # if the end index is not specified, it defaults to the end of the list
print(Planets[1:])  # Slicing from the second to the lastplanet
print(Planets[1:-1])  # Slicing from the second to the last but one planet
# Note: when slicing is not being used, -1 indicates the last element, but when slicing is used, -1 indicates the last but one element.
print(Planets[-3:])  # Slicing from the third last to the last planet
print(Planets[-3:-1])  # Slicing from the third last to the last but one planet