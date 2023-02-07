import csv

# Solve using 'reader()' method
with open('data/happiness.csv', 'r', encoding='UTF8') as file:
    happiness_data = list(csv.reader(file))  # save data to list for multiple iterations

analysis_data = []
for row in happiness_data:
    analysis_data.append([row[3], row[1]])

analysis_data.sort(reverse=True)

res = []

for line in analysis_data:
    if analysis_data.index(line) > 9:
        break
    res.append(line)


for row in res:
    print(row)


# Solve using 'DictReader()' method
with open('data/happiness.csv', 'r', encoding='UTF8') as file:
    happiness_data = list(csv.DictReader(file))

analysis_data = []

for line in happiness_data:
    analysis_data.append([line['GDP per capita'], line['Country or region']])

analysis_data.sort(reverse=True)

res = []
for line in analysis_data:
    if analysis_data.index(line) > 9:
        break
    res.append(line)

for line in res:
    print(line)


# # Solutiuon with menu
# def get_top(top_number, col, data):
#     analysis_data = []
#     for row in data:
#         analysis_data.append([row[col], row[1]])
#
#     analysis_data.sort(reverse=True)
#
#     res = []
#
#     for line in analysis_data:
#         if analysis_data.index(line) > top_number:
#             break
#         res.append(line)
#
#     return res
#
#
# def main():
#     while True:
#         user_choice = input('Please choose\n1.GDP per capita\n2.Social support\n3.Healthy life expectancy\n'
#                             '4.Freedom to make life choices\n5.Generosity\n6.Perceptions of corruption\n'
#                             '0.Exit\n--> ')
#         if user_choice in '123456':
#             while True:
#                 user_top = input('How many top rows? -> ')
#                 if user_top.isdigit():
#                     break
#                 else:
#                     print('Code you entered is not numeric')
#             if user_choice == '1':
#                 top = get_top(int(user_top), 3, happiness_data)
#                 for line in top:
#                     print(line)
#             elif user_choice == '2':
#                 top = get_top(int(user_top), 4, happiness_data)
#                 for line in top:
#                     print(line)
#             elif user_choice == '3':
#                 top = get_top(int(user_top), 5, happiness_data)
#                 for line in top:
#                     print(line)
#             elif user_choice == '4':
#                 top = get_top(int(user_top), 6, happiness_data)
#                 for line in top:
#                     print(line)
#             elif user_choice == '5':
#                 top = get_top(int(user_top), 7, happiness_data)
#                 for line in top:
#                     print(line)
#             elif user_choice == '6':
#                 top = get_top(int(user_top), 8, happiness_data)
#                 for line in top:
#                     print(line)
#         elif user_choice == '0':
#             print('Good bye!')
#             break
#         else:
#             print('Choice is out of range!')
#
#
# main()

