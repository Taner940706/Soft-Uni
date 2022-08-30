from collections import deque

vowels = deque(input().split())
consonants = input().split()

matches = ["rose", "tulip", "lotus", "daffodil"]
matched_word = []
needed_word = ""
counter = 0

while vowels and consonants:
    vowel = vowels[0]
    consonant = consonants[-1]
    matched_word.append(vowel)
    matched_word.append(consonant)
    if needed_word:
        break
    for i in matches:
        for x in i:
            if x in matched_word:
                counter += 1
        if len(i) == counter:
            needed_word = i
            break
        else:
            counter = 0
    vowels.popleft()
    consonants.pop()

if needed_word:
    print(f"Word found: {needed_word}")
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")
else:
    print("Cannot find any word!")
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")
