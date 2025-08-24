#1
from datetime import datetime, timedelta
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print("Day:", day)
print("Month:", month)
print("Year:", year)
print("Hour:", hour)
print("Minute:", minute)
print("Timestamp:", timestamp)

#2
date_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print("ngay dc format:", date_format)

#3
str_ngay= "5 December, 2019"
date_object = datetime.strptime(str_ngay, "%d %B, %Y")
print(date_object)

#4
new_year = datetime(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0)
kcach = new_year - now
print("Thoi gian con lai toi nam moi la", kcach)
del kcach

#5
a = datetime(1970, 1, 1)
kcach = now - a
print("Kcach thoi gian tu 1970 toi hien tai la", kcach)

#6 so ngay con lai de hoi vien het han
ngay_het_han = datetime.now() + timedelta(days=30)
print("Goi hoi vien se ket thuc vao ngay", ngay_het_han)
