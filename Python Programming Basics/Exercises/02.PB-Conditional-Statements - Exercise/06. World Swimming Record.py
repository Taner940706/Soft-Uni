sec = float(input())
distance = float(input())
distance_per_sec = float(input())

wanted_sec = distance*distance_per_sec
extra = (distance//15)*12.5
all_sec = wanted_sec+extra


if all_sec < sec:
    print(f"Yes, he succeeded! The new world record is {all_sec:.2f} seconds.")
else:
    print(f"No, he failed! He was {all_sec-sec:.2f} seconds slower.")
