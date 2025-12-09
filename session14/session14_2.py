
from session13.session13 import users as u
print(u)

#--------------------------------

from datetime import datetime

print(datetime.now())

now = datetime.now()
print(now.hour)
print(now.minute)
print(now.year)

# ------------------------------------------

## delta time:

import datetime
birthday = datetime.date(2023, 5, 17)
now = datetime.date(2025, 10, 28)
delta = (now - birthday)
print(delta)

#-------------------------------------

## 16 Oct 2025 18:32, human read

import datetime
date_string = "2023-11-03 15:45:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
formatted_date = parsed_date.strftime("%Y-%m-%d %H")
print(formatted_date)
