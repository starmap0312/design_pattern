from datetime import datetime
import pytz

print("instantiate a datetime object")
dt = datetime(2016, 10, 8, 5, 18, 20)
print(dt)

print("print the datetime object to the defined format")
print(datetime.strftime(dt, '%Y/%m/%d %H:%M:%S'))

print("convert a string to a datetime object")
dt_str = '2016/10/08 05:18:18 GMT'
print(dt_str)
dt = datetime.strptime(dt_str, '%Y/%m/%d %H:%M:%S %Z')
print(dt)

utc = pytz.timezone('UTC')
tpe = pytz.timezone('Asia/Taipei')
us = pytz.timezone('US/Pacific')

print("specify the time zone of a datetime object")
dt_us = dt.replace(tzinfo=us)
print(dt_us)
dt_utc = dt.replace(tzinfo=utc)
print(dt_utc)
dt_tpe = dt.replace(tzinfo=tpe)
print(dt_tpe)

print("compare two datetime objects")
print(dt_us > dt_utc)

print("compute the time difference of two datetime objects")
print(dt_us - dt_tpe)
