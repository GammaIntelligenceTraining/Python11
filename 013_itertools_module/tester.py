import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4, 8, 9, 10]
selectors = [True, False, False, True]

res = itertools.dropwhile(lambda x: x > 2, numbers2)
print(list(res))

res2 = itertools.takewhile(lambda x: x > 2, numbers2)
print(list(res2))

res3 = itertools.accumulate(numbers2)

print(list(res3))