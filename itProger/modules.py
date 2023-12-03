import time
import datetime as dt
import for_modules as fm
from for_modules1 import mult_three_numbers as fm1

import cowsay as cs

# Freeze a program
time.sleep(1)

print(dt.datetime.now())

fm.hello()
print(fm.sum_three_numbers(1, 2, 3))
print(fm.name)

print(fm1(2, 2, 2))

cs.cow('Hello')