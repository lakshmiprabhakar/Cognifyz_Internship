def is_palindrome(s):
    s = s.replace(" ","").lower()
    return s == s[::-1]

test_strings = [
    "malayalam",
    "radar",
    "level",
    "google",
    "leaf",
]

for string in test_strings:
    if is_palindrome(string):
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is NOT a palindrome.")