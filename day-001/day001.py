from datetime import datetime
from datetime import date

today = datetime.today()
print(today)
print(type(today))

todaydate = date.today()
print(todaydate)
print(type(todaydate))

print(todaydate.year)
print(todaydate.month)
print(todaydate.day)

christmas = date(2021, 12, 25)
days_to_christmas = christmas - todaydate
print(days_to_christmas)
print(type(days_to_christmas))

print((christmas - todaydate).days)

if christmas != todaydate:
    print(f"Sorry there are still {(christmas - todaydate).days} days until Christmas!")
else:
    print("Yes!! It is Christmas 🎄")

