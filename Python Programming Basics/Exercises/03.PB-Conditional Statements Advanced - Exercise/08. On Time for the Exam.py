exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
diff_hours = 0
diff_minutes = 0

if 0 <= exam_hour <= 23 and 0 <= arrival_hour <= 23 and 0 <= exam_minutes <= 59 and 0 <= arrival_minutes <= 59:
    if exam_hour < arrival_hour:
        print('Late')
        diff_hours = arrival_hour - exam_hour
        diff_minutes = 60 - exam_minutes + arrival_minutes
        if 0 < diff_minutes < 60:
            print(f'{diff_minutes} minutes after the start')
        if diff_minutes > 59:
            diff_minutes %= 60
            if diff_minutes < 10:
                print(f'{diff_hours}:0{diff_minutes} hours after the start')
            else:
                print(f'{diff_hours}:{diff_minutes} hours after the start')
    elif exam_hour == arrival_hour:
        if arrival_minutes > exam_minutes:
            diff_minutes = arrival_minutes - exam_minutes
            print('Late')
            print(f'{diff_minutes} minutes after the start')
        elif arrival_minutes == exam_minutes:
            print('On time')
        else:
            diff_minutes = exam_minutes - arrival_minutes
            if 0 < diff_minutes < 30:
                print('On time')
                print(f'{diff_minutes} minutes before the start')
            else:
                print('Early')
                print(f'{diff_minutes} minutes before the start')
    elif exam_hour > arrival_hour:
        diff_minutes = 60 - arrival_minutes + exam_minutes
        diff_hours = exam_hour - arrival_hour
        if diff_minutes > 0 and diff_minutes != 60:
            diff_hours -= 1
        diff_minutes += diff_hours * 60
        if 0 < diff_minutes <= 30:
            print('On time')
            print(f'{diff_minutes} minutes before the start')
        elif 60 > diff_minutes > 30:
            print('Early')
            print(f'{diff_minutes} minutes before the start')
        elif diff_minutes > 59:
            print('Early')
            diff_minutes %= 60
            if diff_minutes < 10:
                print(f'{diff_hours}:0{diff_minutes} hours before the start')
            else:
                print(f'{diff_hours}:{diff_minutes} hours before the start')