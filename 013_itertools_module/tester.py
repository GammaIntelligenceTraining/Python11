import itertools

letters = ['a', 'b', 'c', 'd']
numbers = (0, 1, 2, 3)
names = ['Jack', 'Sarah']

# NO ORDER / NO REPEAT
# res = itertools.combinations(letters, 4)
# for x in res:
#     print(x)

# ORDERED / NO REPEAT
# res = itertools.permutations(letters, 3)
# for x in res:
#     print(x)

# ORDERED / REPEATING
# res = itertools.product(numbers, letters, repeat=2)
# for x in res:
#     print(x)

# NO ORDER / REPEATING
# res = itertools.combinations_with_replacement(numbers, 4)
# for x in res:
#     print(x)
#
# itertools.product()

combined = itertools.islice({1, 2, 3, 4, 5, 6, 7, 8}, 0, 5, 2)
print(list(combined))

with open('demo_log.txt', 'r', encoding='UTF8') as file:
    combined = itertools.islice(file, 3)
    print(list(combined))