my_set = {1, 2, 3, 4}

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 6}

my_set.update([7, 8])
print(my_set)  # Output: {1, 2, 3, 4, 6, 7, 8}

# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 6, 7, 8}

# Using remove() on a non-existent element raises a KeyError
# my_set.remove(10)  # Uncommenting this will raise KeyError: 10

# Using discard() on a non-existent element does not raise an error
my_set.discard(10)

# Clearing the set
my_set.clear()
print(my_set)  # Output: set()
