expression = input()
opening_brackets = []

balanced = True

for ch in expression:
    if ch in '([{':
        opening_brackets.append(ch)
    elif not opening_brackets:
        balanced = False
        break
    else:
        last_opening_brackets = opening_brackets.pop()
        if f'{last_opening_brackets}{ch}' not in '()[]{}':
            balanced = False
            break
if balanced:
    print("YES")
else:
    print("NO")
