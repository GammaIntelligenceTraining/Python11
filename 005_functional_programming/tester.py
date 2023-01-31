def increment():
    global a
    a = 10
    a += 10

a = 0

increment()
print(a)