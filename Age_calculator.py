import datetime

def calculate_age(birthdate):
    today = datetime.date.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        if today.month > 1:
            prev_month = today.month - 1
            prev_year = today.year
        else:
            prev_month = 12
            prev_year = today.year - 1

        first_day_of_this_month = datetime.date(today.year, today.month, 1)
        last_day_of_prev_month = first_day_of_this_month - datetime.timedelta(days=1)
        days_in_prev_month = last_day_of_prev_month.day

        days = days + days_in_prev_month
        months = months - 1

    if months < 0:
        months = months + 12
        years = years - 1

    return years, months, days
while(True):
    birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
    if birth_input.lower() == "exit":
        print("Goodbye!")
        break
    try:
        birthdate = datetime.datetime.strptime(birth_input, "%Y-%m-%d").date()
        today = datetime.date.today()
        if birthdate > today:
            print("Birthdate cannot be in the future.")
        else:
            years, months, days = calculate_age(birthdate)
            print(f"You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid format! Please use YYYY-MM-DD.")
