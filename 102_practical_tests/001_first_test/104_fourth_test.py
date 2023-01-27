# some_list = [1, 2, 5, 67, 8, 4, 3, 8, 9]
some_list = input('Please enter some numbers separated by coma: ').split(', ')
# # some_list = some_list[::-1]
# some_list.reverse()
# # print(some_list)

for num in some_list[::-1]:
    print(num)
