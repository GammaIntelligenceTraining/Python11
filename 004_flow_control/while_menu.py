# https://et.wikipedia.org/wiki/Isikukood
while True:
    user_choice = input("Please choose:\n1.Print 'Hello world'\n2.Print 'Hello planet\n"
                        "3.Exit\n--> ")

    if user_choice == '1':
        print('Hello world')
    elif user_choice == '2':
        numbers = range(0, 10)
        for num in numbers:
            if num == 6:
                continue
            print(num)
        print('Hello planet')
    elif user_choice == '3':
        break
    else:
        print('Choice is out of range!')
    print('New Cycle')
print('Good bye')

