# Calculates how much money should be in my food bank account
from __future__ import division
import datetime
import calendar

today = datetime.datetime.now()
day_of_month = today.day
days_in_current_mont = calendar.monthrange(today.year, today.month)[1]
daily_cost = 400 / 7

result = round((days_in_current_mont - day_of_month) * daily_cost, 2)

print(str(result) + ' DKK')


