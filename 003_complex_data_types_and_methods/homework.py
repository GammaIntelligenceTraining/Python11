for num in range(0, 101):
    if num % 5 == 0 and num % 3 == 0:
        print(num, 'fizzbuzz')
    elif num % 3 == 0:
        print(num, 'fizz')
    elif num % 5 == 0:
        print(num, 'buzz')
