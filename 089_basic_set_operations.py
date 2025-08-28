# Set Operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)  # {1, 2, 3, 4, 5, 6}
print(A.union(B))  # {1, 2, 3, 4, 5, 6}

# Intersection
print(A & B)  # {3, 4}
print(A.intersection(B))  # {3, 4}

# Difference
print(A - B)  # {1, 2}
print(A.difference(B))  # {1, 2}

# Symmetric Difference
print(A ^ B)  # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
