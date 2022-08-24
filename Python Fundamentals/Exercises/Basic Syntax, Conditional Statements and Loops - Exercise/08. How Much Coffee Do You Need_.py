event = input()
coffee = 0;

while event != "END":
    if event == "cat" or event == "dog" or event == "coding" or event == "movie":
        coffee += 1;
    elif event == "CAT" or event == "DOG" or event == "CODING" or event == "MOVIE":
        coffee += 2;
    event = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)