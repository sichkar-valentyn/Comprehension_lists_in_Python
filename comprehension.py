
# Without using list-comprehension in Python
x = [-2, -1, 0, 1, 2]
y = []
for i in x:
    y.append(i * i)
print(y)

# With using list-comprehension in Python
x = [-2, -1, 0, 1, 2]
y = [i * i for i in x]
print(y)

y = [i * i for i in x if i > 0]
print(y)

z = [(g, k) for g in range(3) for k in range(3) if k >= g]
print(z)

# If we change the square brackets to round brackets
# We'll get the generator
z = ((g, k) for g in range(3) for k in range(3) if k >= g)
print(z)
print(next(z))
print(next(z))

print(list(z))
