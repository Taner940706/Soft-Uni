def palindrome(word, ind=0):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
