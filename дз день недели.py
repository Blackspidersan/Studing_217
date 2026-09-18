def is_leap(year):
    return year % 4 == 0 and (
        year % 100 != 0 or year % 400 == 0
    )  # правило високосного года


def days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    return 29 if is_leap(year) else 28


def date_to_days(d, m, y):
    years_passed = y - 1
    days = years_passed * 365
    days += years_passed // 4
    days -= years_passed // 100
    days += years_passed // 400
    for month in range(1, m):
        days += days_in_month(month, y)
    days += d
    return days


def parse_date(s):
    parts = s.split(".")
    d, m, y = int(parts[0]), int(parts[1]), int(parts[2])
    return d, m, y


def get_day_of_week(d, m, y):
    days_words = [
        "Воскресенье",  # остаток 0
        "Понедельник",  # остаток 1
        "Вторник",  # остаток 2
        "Среда",  # остаток 3
        "Четверг",  # остаток 4
        "Пятница",  # остаток 5
        "Суббота",  # остаток 6
    ]
    total_days = date_to_days(d, m, y)
    day_index = total_days % 7
    return days_words[day_index]


date_input = input("Введите дату ДД.ММ.ГГГ:")
day, month, year = parse_date(date_input)
day_of_week = get_day_of_week(day, month, year)
print(day_of_week)
