import math
serial_name = input()
serial_duration = int(input())
rest_duration = int(input())

lunch_duration = rest_duration/8
relax_duration = rest_duration/4
remain_duration = rest_duration - (lunch_duration + relax_duration)

if remain_duration >= serial_duration:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(remain_duration-serial_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(serial_duration - remain_duration)} more minutes.")