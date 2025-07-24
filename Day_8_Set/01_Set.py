# Set
"""Sets are used to store multiple items in a single variable."""

#* Note: Set items are unchangeable, but you can remove items and add new items.


Aset = {"apple", "banana","crop","drop"}
print(Aset)
print(type(Aset))# <class 'set'>
print("------------------------------")

#*****Set aare unordered, that is that doesn't follow the specific order 
"""output"""
# {'crop', 'banana', 'drop', 'apple'}
# {'banana', 'drop', 'apple', 'crop'}
# {'drop', 'banana', 'apple', 'crop'}
"""Set's output are random"""

# Duplicates Not Allowed

"""Sets cannot have two items (with the same value)."""

bset = {"apple", "banana","crop","drop", "apple"}
print(bset)#{'apple', 'drop', 'banana', 'crop'}
print("------------------------------")




# the value of 1 and True are same in set

sset = {"apple", "banana", "cherry", True, 1, 2}
print(sset)#{True, 2, 'banana', 'cherry', 'apple'}, That's why follow this rule {{Sets cannot have two items (with the same value)}}
print("------------------------------")

"""Same for False and 0"""
sset = {"apple", "banana", "cherry", False, 0, 2}
print(sset)#{False, 2, 'banana', 'cherry', 'apple'}, That's why follow this rule {{Sets cannot have two items (with the same value)}}
print("------------------------------")



# To Get the Length of a Set
"""We use len()Function"""
sset = {"apple", "banana", "cherry", True, 1, 2}
print(len(sset))#5
print("------------------------------")

#  To Construct The set() 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
print(type(thisset))

print("------------------------------")
