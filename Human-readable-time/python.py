import math


def make_readable(seconds):
    hoursLeft = math.floor(seconds / 3600)
    min = math.floor((seconds - hoursLeft * 3600) / 60)
    secondsLeft = seconds - hoursLeft * 3600 - min * 60
    secondsLeft = round((secondsLeft * 100) / 100)
    hhString = str(hoursLeft)
    mmString = str(min)
    ssString = str(secondsLeft)
    if (len(hhString) < 2):
        hhString = "0" + hhString

    if (len(mmString) < 2):
        mmString = "0" + mmString

    if (len(ssString) < 2):
        ssString = "0" + ssString

    return hhString + ":" + mmString + ":" + ssString


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))

# return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
