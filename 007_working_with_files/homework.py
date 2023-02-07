with open('text_files/trimushketera.txt', 'r', encoding='UTF8') as file:
    data = file.read().lower().replace('.', '').replace(',', '')\
        .replace('!', '').replace('?', '').replace('"', '').replace('(', '').replace(')', '')

words = data.split()
unique = list(set(words))
unique.sort()

with open('text_files/trimushketera_copy.txt', 'w', encoding='UTF8') as file:
    file.write(f'There are {len(words)} words.\n')
    file.write(f'There are {len(unique)} unique words.\n')
    for word in unique:
        file.write(word + f'{word}\n')
