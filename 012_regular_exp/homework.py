import re

# HASH colors (#FFFFFF)

# Number with + sign
# sample = '345-12312+123123+12312-21312*2133-123 123123 21312'
# pattern = re.compile(r'(\d+)[^+\d]|(\d+$)', re.IGNORECASE)
#
# matches = pattern.finditer(sample)
#
# for match in matches:
#     print(match.group(1) or match.group(2))


# # Time
# sample = '14:20, 30:13, 13:90, 123:23, 21:213, 123:123, 43:32'
# pattern = re.compile(r'\b([01][0-9]|2[0-3]):([0-5][0-9])\b')
# matches = pattern.finditer(sample)
#
# for match in matches:
#     print(match)

# People.txt
# with open('people.txt', 'r', encoding='UTF8') as file:
#     data = file.read()
#
# name_pattern = re.compile(r'([A-Za-z]+ [A-Za-z-]+)\n')
# address_pattern = re.compile(r'\d{3} [0-9A-Za-z\'-]+ St\., [A-Za-z\' -]+ [A-Z]{2} \d{5}')
# matches1 = name_pattern.findall(data)
# print(len(matches1))
#
# matches2 = address_pattern.findall(data)
# print(len(matches2))
#
# people_pairs = list(zip(matches1, matches2))
#
# people_dict = {}
# cnt=0
# for name, address in people_pairs:
#     people_dict[cnt] = {'name': name, 'address': address}
#     cnt += 1
#
# print(people_dict)


# A-Za-z0-9
# sample = 'aasdasd213123ASDASDasd'
#
# pattern = re.compile(r'[^A-Za-z0-9]')
# matches = pattern.findall(sample)
#
# if matches:
#     print(False)
# else:
#     print(True)
#
# if not matches:
#     print(True)
# else:
#     print(False)

# # ISIKUKOOD
# sample = '38803160272'
# pattern = re.compile(r'[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
# matches = pattern.finditer(sample)
#
# for m in matches:
#     print(m)