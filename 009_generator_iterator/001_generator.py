# Generator function has yield instead of return
# This results in iterator like behaviour
def squares(start, stop):
    for i in range(start, stop):
        yield i ** 2  # yield returns only one result


x = squares(1, 11)  # Generator object is created

print(next(x))
print(next(x))
print(next(x))

# similar to iterator, generator will end after last element is reached
for num in x:
    print(num)


# print(next(x))  # will raise error