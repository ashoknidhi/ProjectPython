# program to demonstrate the use of build in functions on lists
Planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']   
Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# print the length of the list
print("Number of planets:", len(Planets))
# print the maximum value in the list
print("Maximum prime number:", max(Primes)) 
# print the minimum value in the list
print("Minimum prime number:", min(Primes))
# print the sum of the list
print("Sum of prime numbers:", sum(Primes)) 
# print the sorted list
print("Sorted planets:", sorted(Planets))
# print the reversed list
print("Reversed primes:", list(reversed(Primes)))
print("Reversed planets:", list(reversed(Planets)))

# print the list in original order
print("Original planets:", Planets)
Planets.append('Pluto')  # add Pluto to the list
print("Updated planets:", Planets)
Planets.remove('Pluto')  # remove Pluto from the list
print("After removing Pluto:", Planets)
Planets.reverse()
print("Reversed planets using reverse method:", Planets)
Planets.reverse()
print("Reversed planets back to original order:", Planets)
Planets.pop()  # remove the last element
print("After popping the last planet:", Planets)
if 'Earth' in Planets:  # check if 'Earth' is in the list
    Planets.index('Earth')  # find the index of 'Earth'
    print("Index of Earth:", Planets.index('Earth'))
else :
    print("Earth is not in the list of planets.")

if 'Pluto' in Planets:  # check if 'Pluto' is in the list
    Planets.index('Pluto')  # find the index of 'Pluto'
    print("Index of Pluto:", Planets.index('Pluto'))    
else :
    print("Pluto is not in the list of planets.")