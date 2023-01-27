def convert(seconds):
    print(seconds)
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    print(seconds)
    hours = seconds // 3600
    seconds %= 3600
    print(seconds)
    minutes = seconds // 60
    seconds %= 60
    print(seconds)
    print(f'{days}:{hours}:{minutes}:{seconds}')


user_input = int(input('Please enter amount of seconds'))
convert(user_input)


