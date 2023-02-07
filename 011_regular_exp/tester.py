import re

random_sting = '78803160272'

pattern = re.compile(r'[1-6][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')

matches = pattern.finditer(random_sting)

for match in matches:
    print(match)