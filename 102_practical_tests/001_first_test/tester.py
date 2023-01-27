# name, surname, age = input('Please enter Name, surname and age (user ", " for separator: ').split(', ')
# print(f'Hello {surname} {name}. Your age is: {age}')

# import math
# side_a, side_b  = input('Enter side A and B: ').split()
# print(((float(side_a) ** 2) + (float(side_b) ** 2)) ** 0.5 )
#
# print(math.sqrt((float(side_a) ** 2) + (float(side_b) ** 2)))

# side_a, side_b, side_c  = input('Enter side A and B: ').split()
#
# if float(side_c) ** 2 == float(side_a) ** 2 + float(side_b) ** 2:
#     print('This is right triangle.')
# else:
#     print('This is not a right triangle')


# user_lst = input('Enter values separated by coma: ').split(', ')
#
# for x in user_lst[::-1]:
#     print(x)

# tup1 = (1, 2, 3, 5, 8)
# tup2 = (8,2,5)
#
# # print(tup1[:2] + tup2 + tup1[2:])
# tup1 = list(tup1)
# for x in tup2[::-1]:
#     tup1.insert(2, x)
# tup1 = tuple(tup1)
# print(tup1)

test_lst = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 4]
max_count = 0
result = []

for num in test_lst:
    if test_lst.count(num) > max_count:
        max_count = test_lst.count(num)

for num in test_lst:
    if test_lst.count(num) == max_count and num not in result:
        result.append(num)

print(result)


# counter = {}
#
# for num in test_lst:
#     counter[num] = test_lst.count(num)
# print(counter)
#
# result = []
# for x in counter.keys():
#     if counter[x] == max(counter.values()):
#         result.append(x)
# print(result)

seconds = 12321321312
days = seconds // (24 * 3600)
seconds %= 24 * 3600
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{minutes}:{seconds}')