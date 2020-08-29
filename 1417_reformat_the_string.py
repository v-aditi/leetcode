"""
QUESTION #1417 - REFORMAT THE STRING [PASSED]
Difficulty: Easy

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by
another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
"""

# test case 1 - "abc123" returns "a1b2c3"
# test case 2 - "ab123" returns "1a2b3"
# test case 3 - "abcd" returns "" (no possible permutation)
# test case 4 - "1234" returns "" (no possible permutation)
# test case 5 - "abcd12" returns "" (no possible permutation)

def reformat(s: str) -> str:
    # preprocess the text
    integers = []
    characters = []

    for i in range(len(s)):
        try:
            test = int(s[i])
            integers.append(s[i])
        except ValueError:
            characters.append(s[i])

    # check for edge cases
    if abs(len(integers)-len(characters)) > 1:
        return ""

    output = ""
    i = 0
    # produce output string
    if len(integers) >= len(characters):
        # bounded by length of smaller array
        while i < len(characters):
            output += (integers[i] + characters[i])
            i += 1
        if len(integers) > len(characters):
            output += integers[len(integers)-1]
    if len(characters) > len(integers):
        # bounded by length of smaller array
        while i < len(integers):
            output += (characters[i] + integers[i])
            i += 1
        output += characters[len(characters)-1]
    return output

"""
NOTES:
- time complexity is O(N) where N = length of the string
- this wasn't a very time efficient implementation
- made some stupid mistakes when implementing the while loops
- want to get better at testing manually without using debugger or console

RESULTS: Faster than 5.33% of submissions, uses less memory than 26.17% of submissions

IMPROVEMENTS:
- to improve memory useage, pop the elements from the array when adding to the string
- '.isalpha()' returns True if alphabet
- try to combine steps and loops to make it more efficient
"""
