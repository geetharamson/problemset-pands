# Is today a day that begins with the letter T 

import datetime

if datetime.datetime.today().weekday() == [1,3]:
  print("Yes-today begins with a T.")
else:
  print("No-today doesnot begin with a T.")
