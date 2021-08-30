from datetime import datetime
def what_day_of_the_week(year, month, date):
    return datetime(year, month, date).strftime('%A')