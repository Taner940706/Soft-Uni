import re

some_string = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, some_string, flags=re.I)
print(len(matches))
