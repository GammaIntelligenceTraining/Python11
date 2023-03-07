import hashlib

password = hashlib.md5('hello123'.encode()).hexdigest()

print(hashlib.md5(password.encode()).hexdigest())
# f30aa7a662c728b7407c54ae6bfd27d1


if hashlib.md5(input('Enter pass: ').encode()).hexdigest() == password:
    print('OK')
else:
    print('NOK')

