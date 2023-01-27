# 38803160272
while True:
    user_input = input('Please enter your Estonian national ID number (type "exit" to stop): ')
    if user_input.lower() == 'exit':
        quit()
    try:
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning

    except ValueError:
        print('Code you entered is not numeric')
        continue
    except UserWarning:
        print('Code you entered is not 11 numbers long')
        continue
    else:
        while True:
            user_choice = input("Please choose:\n1.Gender\n2.Date of birth\n"
                                "3.Region\n4.Validate\n5.Change ID\n0.Exit\n--> ")
            if user_choice == '1':
                if user_choice[0] in ['0', '9']:
                    gender = 'Unknown'
                elif int(user_input[0]) % 2 == 0:
                    gender = 'Female'
                else:
                    gender = 'Male'
                print(f'You are {gender}')
            elif user_choice == '2':
                if user_choice[1:3] in '12':
                    cent = '18'
                elif user_choice[1:3] in '34':
                    cent = '19'
                elif user_choice[1:3] in '56':
                    cent = '20'
                elif user_choice[1:3] in '78':
                    cent = '21'
                else:
                    cent = 'Unknown'
            elif user_choice == '3':
                r_id = int(user_input[7:10])
                if r_id in range(1, 11):
                    region = 'Kuressaare haigla'
                elif r_id in range(11, 20):
                    region = 'Tartu Ülikooli Naistekliinik'
                elif r_id in range(21, 151):
                    region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
            elif user_choice == '4':
                chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
                chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
                result = user_input[0] * chk1[0] + user_input[1] * chk1[1]
                if int(user_input[-1]) == result % 11:
                    print('ID code is valid')
                else:
                    result = user_choice[0] * chk2[0]
            elif user_choice == '5':
                break
            elif user_choice == '0':
                quit()
            else:
                print('Choice is out of range!')