# to_list = ["aiden.hyunjae@gmail.com", "aiden.grrrr@gmail.com", "ho2840@email.vccs.edu"]
# msg = ", ".join(to_list) 
# print(msg)

import time
print(time.strftime('%d-%b-%Y'))

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))