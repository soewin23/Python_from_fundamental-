# Use with Built-in Functions ✅
# map()<--Transform each item	
# filter()<---Keep items that match condition	
# sorted()<--Custom sort logic	

# 1. map() — Apply a function to every item in an iterable
"""Takes a function and an iterable (like a list).
Returns a new iterable where the function is applied to each element.
"""
lis = [1,2,3,4,5]
A =[]
# Using lamba to square each number
square = list(map(lambda x: x ** 2,lis))
print(square)
"""Using for loop"""
for i in lis:
    A.append(i **2)
print(A)