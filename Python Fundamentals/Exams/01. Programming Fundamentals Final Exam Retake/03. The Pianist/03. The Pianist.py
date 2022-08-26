n = int(input())
songs = {}

for i in range(n):
    song = input().split("|")
    if song[0] not in songs.keys():
        songs[song[0]] = [song[1], song[2]]

command = input()

while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        if command[1] not in songs.keys():
            songs[command[1]] = [command[2], command[3]]
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{command[1]} is already in the collection!")
    if command[0] == "Remove":
        if command[1] in songs.keys():
            songs.pop(command[1])
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    if command[0] == "ChangeKey":
        if command[1] in songs.keys():
            songs[command[1]][1] = command[2]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    command = input()
t = dict(sorted(songs.items(), key=lambda s: (s[0], s[1][0])))
for key, value in t.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
