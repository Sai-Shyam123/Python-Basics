import datetime
import pytz

today = datetime.date.today()
print(today)

birthday1 = datetime.date(2009, 2, 6)
birthday = datetime.date(2006, 9, 7)
print(birthday)

#num of days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

#adding 25 days from today
tdelta = datetime.timedelta(days=25)
print(today + tdelta)

family_bday = [birthday1, birthday]
tdelta1 = datetime.timedelta(days=10)

#adding 10 days to the birthdays
print([bday+tdelta1 for bday in family_bday])

# monday = 0, sunday = 6
print(today.month)
print(today.day)
print(today.weekday())

# h:m:s

#Adding 10hours to today
print(datetime.time(7, 52, 16, 12))
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now()+hour_delta)

#datetime.date  (Y, M, D)
#datetime.time  (H, M, S, MS)
#datetime.datetime  (Y, M, D, H, M, S, MS)

datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
datetime_kuwait = datetime_today.astimezone(pytz.timezone('Asia/Kuwait'))
print(datetime_kuwait)

#Print all timezones

for tz in pytz.all_timezones:
    print(tz)


# String formatting with dates
# 2021-02-03 -> February 3, 2021

print(datetime_kuwait.strftime('%B %d, %Y'))

