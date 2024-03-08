import datetime
x = datetime.datetime.now()
delta = datetime.timedelta(days=1)
yesterday = x - delta
tomorrow = x + delta
print("Today: ",x)
print("Yesterday: ",yesterday)
print("Tomorrow: ", tomorrow)