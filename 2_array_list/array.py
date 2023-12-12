a = [2, 5 , 8 , 9 , 12]
print("print a", a)

#  Append 
a.append(15)
print("APPEND", a)

# Insert
a.insert(0, 1)
print("INSERT", a)

print("COUNT OF 9", a.count(9))

b = [98, 5, 7, 4, 1, 2, 3, 6]
# Extend
a.extend(b)
print("Extend", a)

# Index
print("INDEX OF 98", a.index(98))

# Pop
a.pop()
print("ADTER POP", a)
a.pop(0)
print("POP 0", a)

# Remove
a.remove(98)
print("REMOVE 98", a)

# Reverse
a.reverse()
print("REVERSE", a)

# Sort
a.sort()
print("SORT", a)

# LENGTH
print("LENGTH", len(a))

# SUM
print("SUM", sum(a))

# MIN
print("MIN", min(a))

# MAX
print("MAX", max(a))

# SORTED
print("SORTED", sorted(b))

# COPY
c = a.copy()
print("COPY", c)

# clear 
a.clear()
print(a)