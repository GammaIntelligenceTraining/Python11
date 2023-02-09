import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
899-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Ms Samanta-Maria
Mrs GOLD

abc
example*com
mall hall wall tall ball
sall xall fall

af-t
'''

sentence = 'Start a sentence And then Bring it to an end'

pattern = re.compile(r'.# I am comment', re.VERBOSE)

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)