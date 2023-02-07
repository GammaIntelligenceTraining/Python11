import csv

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
