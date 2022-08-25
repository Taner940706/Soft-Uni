road = [int(x) for x in input().split(" ")]
right_road = road[::-1]
left_racer = 0;
right_racer = 0;

for i in range(len(road)//2):
    if road[i] == 0:
        left_racer = left_racer*0.8;
    else:
        left_racer += road[i];

for j in range(len(right_road)//2):
    if right_road[j] == 0:
        right_racer = right_racer*0.8;
    else:
        right_racer += right_road[j];

if left_racer > right_racer:
    print(f"The winner is right with total time: {right_racer:.1f}");
else:
    print(f"The winner is left with total time: {left_racer:.1f}");
