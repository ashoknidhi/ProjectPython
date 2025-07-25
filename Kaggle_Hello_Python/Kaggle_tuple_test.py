a = [1,2,3]
b = [5,6,7]
# to swap values of a and b
# The usual approach is to use a temporary variable
# temp = a 
# a = b
# b = temp
# But in Python, we can do it more elegantly without a temp variable
a, b = b, a
print("a:", a)
print("b:", b)

