from datetime import datetime, date

# birthday = datetime.date(1999, 7, 11)
# now = datetime.datetime.now()
# now1 = datetime.date(birthday)

passport = {
    'birthday': '1998-06-30',
    'date_of_issue': '2018-06-30'
}
year = int(datetime.today().year)
month = int(datetime.today().month)
day = int(datetime.today().day)
message = 'a passport must be issued'


def check(param):
    print(param['birthday'])
    print(param['date_of_issue'])
    birthday = param['birthday'].split('-')
    date_of_issue = param['date_of_issue'].split('-')
    print(int(birthday[0]))
    print(int(datetime.today().year))
    result = int(datetime.today().year) - int(birthday[0])
    print('result = ', result)

    if year - int(birthday[0]) == 14:
        return print(check_birthday(birthday) & check_date_of_issue(date_of_issue, birthday))
    if year - int(birthday[0]) == 20:
        print(check_birthday(birthday), check_date_of_issue(date_of_issue, birthday))
        return print(check_birthday(birthday) & check_date_of_issue(date_of_issue, birthday))
    if year - int(birthday[0]) == 45:
        return print(check_birthday(birthday) & check_date_of_issue(date_of_issue, birthday))
    else:
        return print(True)


def check_birthday(list_birthday):
    if month == int(list_birthday[1]):
        if day >= int(list_birthday[2]):
            print(message, '==')
            return True
    elif month == int(list_birthday[1]) - 1:
        if day >= int(list_birthday[2]):
            print(message, '+1')
            return True
    else:
        return False


def check_date_of_issue(list_date_of_issue, list_birthday):
    if year == int(list_date_of_issue[0]):
        print(int(list_date_of_issue[1]), int(list_birthday[1]))
        if int(list_date_of_issue[1]) >= int(list_birthday[1]):
            if int(list_date_of_issue[2]) >= int(list_birthday[2]):
                print('here')
                return True
    else:
        return False


check(passport)

