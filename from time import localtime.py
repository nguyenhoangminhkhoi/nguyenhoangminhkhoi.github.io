from time import localtime
from turtle import *  # avoid wildcard imports like this

ATTRIBUTES = ['tm_hour', 'tm_min', 'tm_sec']

def tick():
    record = localtime()

    hands['tm_hour'].seth(record.tm_hour % 12 * 30 + record.tm_min / 2 + record.tm_sec / 120)
    hands['tm_min'].seth(record.tm_min * 6 + record.tm_sec / 10)
    hands['tm_sec'].seth(record.tm_sec * 6)

    ontimer(tick, 1000)

mode("logo")  # make 0 degrees be straight up the page

hands = {}
for size, attr in enumerate(ATTRIBUTES, start=1):
    hands[attr] = Turtle('triangle')
    hands[attr].shapesize(1 / size, size * 10)

tick()

mainloop()