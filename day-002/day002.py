from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)
print(type(t))

print(t.days)

print(t.seconds / 60 / 60)
print(t.seconds / 3600)

eta = timedelta(hours=16)
today = datetime.today()

print(eta)
print(today)

print(repr(eta))
print(repr(today))

print(today + eta)
print(repr(today + eta))

print(str(today + eta))
print(repr(str(today + eta)))


