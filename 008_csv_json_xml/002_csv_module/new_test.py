x = [1, 2, 3, 4, 5]
y = iter(x)

next(y)
next(y)

for i in y:
    print(i)
