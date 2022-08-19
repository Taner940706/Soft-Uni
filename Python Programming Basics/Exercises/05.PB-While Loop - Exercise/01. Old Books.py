book = input()
new_book = input()
count = 0
is_true = False
while new_book != "No More Books":
    if new_book == book:
        is_true = True

        print(f'You checked {count} books and found it.')
        break
    count = count + 1
    new_book = input()
if not is_true:
    print("The book you search is not here!")
    print(f"You checked {count} books.")