from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    today = datetime.today().date()
    birthdays_this_week = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.strftime("%A")

            if weekday in ["Saturday", "Sunday"]:
                weekday = "Monday"

            birthdays_this_week[weekday].append(name)

    for weekday, names in birthdays_this_week.items():
        print(f"{weekday}: {', '.join(names)}")
