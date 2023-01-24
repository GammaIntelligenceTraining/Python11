# try:
#     user_input = float(input('Enter number: '))
# except:
#     print('Must enter a number!')
# else:
#     print(user_input ** 2)
# finally:
#     print('Good bye!')
while True:
    try:
        user_id = input('Please enter id code: ')
        int(user_id)
        if len(user_id) != 11:
            raise Exception

    except ValueError:
        print('Code you entered is not numeric.')
        continue
    except Exception:
        if len(user_id) > 11:
            print('Code is too long!')
        else:
            print('Code is too short!')
        continue
    else:
        print('Your id code is', user_id)
        break