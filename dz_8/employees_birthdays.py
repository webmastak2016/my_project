import datetime

employees = [
    {'name': 'Anna', 'birthday': datetime.datetime(2023, 6, 1)},  # Thursday
    {'name': 'Viktor', 'birthday': datetime.datetime(2023, 6, 2)},  # Friday
    {'name': 'Katia', 'birthday': datetime.datetime(2023, 6, 3)},  # Saturday
    {'name': 'Denis', 'birthday': datetime.datetime(2023, 6, 4)},  # Sunday
    {'name': 'Elena', 'birthday': datetime.datetime(2023, 6, 5)},  # Monday
    {'name': 'Fedor', 'birthday': datetime.datetime(2023, 6, 6)},  # Tuesday
    {'name': 'Grisha', 'birthday': datetime.datetime(2023, 6, 7)},  # Wednesday
]


def get_birthdays_per_week(employees):
    today = datetime.date.today()
    current_weekday = today.weekday()

    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

    birthdays_per_week = {day: [] for day in weekdays}

    for empl in employees:
        name = empl['name']
        birthday = empl['birthday']
        i = birthday.weekday()
        den = weekdays[i]
        print(f'{i}: {den}')

        if birthday.weekday() >= 5 or birthday.weekday() >= 6:
            birthday_weekday = weekdays[0]
        else:
            birthday_weekday = weekdays[birthday.weekday()]

        birthdays_per_week[birthday_weekday].append(name)

    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(employees)
