from datetime import timedelta, datetime

arrival = datetime(2018, 04, 13,23, 0, 0)
print arrival.strftime("%d/%m/%y %H:%M")
departure = datetime(2018, 04, 20, 1, 0, 0)
print departure.strftime("%d/%m/%y %H:%M")
full_day_start = arrival.date() + timedelta(days=1)
full_day_end = departure.date()
print full_day_start.strftime("%d/%m/%y %H:%M")
print full_day_end.strftime("%d/%m/%y %H:%M")
print full_day_end - full_day_start
