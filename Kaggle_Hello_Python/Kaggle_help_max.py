def mod_5(x):
    return x % 5

print (
    'which number is the biggest',
    max(100, 51, 14),
    'which number is the biggest modulo 5',
    max(100, 51, 14, key=mod_5),
    sep='\n'
)
# The optional key argument to max() allows you to specify a function that will be applied to each 
# element before comparison i.e the function will be applied to each element in the iterable,
# and the element with the maximum value of the function will be returned.