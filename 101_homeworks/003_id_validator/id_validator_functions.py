def enter_id():
    global id_code
    while True:
        user_id = input('Please enter ID code or type "EXIT": ')
        if user_id.lower() == 'exit':
            print('Good bye!')
            quit()
        else:
            # Try, except, else to check id for errors
            try:
                int(user_id)
                if len(user_id) != 11:
                    raise UserWarning
            except ValueError:
                print('ID you entered is not numeric! ')
            except UserWarning:
                if len(user_id) > 11:
                    print('ID is too long')
                else:
                    print('ID is too short')
                continue
            else:
                id_code = user_id
                break


def print_gender():
    if int(id_code[0]) % 2 == 0 and int(id_code[0]) < 9:
        gender = 'Female'
    elif int(id_code[0]) < 9 and int(id_code[0]) < 9:
        gender = 'Male'
    else:
        gender = None
    if gender:
        print(f'You are {gender}.')
    else:
        print('Unable to determine your gender')


def print_date_of_birth():
    if id_code[0] in '12':
        bcent = '18'
    elif id_code[0] in ('3', '4'):
        bcent = '19'
    elif id_code[0] in ('5', '6'):
        bcent = '20'
    else:
        bcent = None
    if bcent:
        print(f'You were born on {id_code[5:7]}.{id_code[3:5]}.{bcent + id_code[1:3]}')
    else:
        print('Cannot determine your birth date')


def print_region_of_birth():
    if int(id_code[7:10]) in range(1, 11):
        bregion = 'Kuressaare haigla'
    elif int(id_code[7:10]) in range(11, 20):
        bregion = 'Tartu Ülikooli Naistekliinik'
    elif int(id_code[7:10]) in range(21, 151):
        bregion = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(id_code[7:10]) in range(151, 161):
        bregion = 'Keila haigla'
    elif int(id_code[7:10]) in range(161, 221):
        bregion = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(id_code[7:10]) in range(221, 271):
        bregion = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(id_code[7:10]) in range(271, 371):
        bregion = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(id_code[7:10]) in range(371, 421):
        bregion = 'Narva haigla'
    elif int(id_code[7:10]) in range(421, 471):
        bregion = 'Pärnu haigla'
    elif int(id_code[7:10]) in range(471, 491):
        bregion = 'Haapsalu haigla'
    elif int(id_code[7:10]) in range(491, 521):
        bregion = 'Järvamaa haigla (Paide)'
    elif int(id_code[7:10]) in range(521, 571):
        bregion = 'Rakvere haigla, Tapa haigla'
    elif int(id_code[7:10]) in range(571, 601):
        bregion = 'Valga haigla'
    elif int(id_code[7:10]) in range(601, 651):
        bregion = 'Viljandi haigla'
    elif int(id_code[7:10]) in range(651, 701):
        bregion = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        bregion = None
    if bregion:
        print(f'You were born in {bregion}.')
    else:
        print(f'You were born outside of Estonia.')


def validate_id():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    cnt = 0
    for num in chk1:
        result += num * int(id_code[cnt])
        cnt += 1
    if result % 11 == int(id_code[10]):
        print('ID is valid!')
    else:
        result = 0
        cnt = 0
        for num in chk2:
            result += num * int(id_code[cnt])
            cnt += 1
        if result % 11 == int(id_code[10]):
            print('ID is valid!')
        else:
            print('ID is not valid!')


def main():
    while True:
        user_input = input('Please choose:\n1.Get gender\n2.Get date of birth\n3.Get region of birth\n4.Validate\n'
                           '5.Change id\n0.Exit\n--> ')
        if user_input == '1':
            print_gender()
        elif user_input == '2':
            print_date_of_birth()
        elif user_input == '3':
            print_region_of_birth()
        elif user_input == '4':
            validate_id()
        elif user_input == '5':
            enter_id()
        elif user_input == '0':
            break
        else:
            print('Choice is out of range!')

id_code = ''

enter_id()
main()