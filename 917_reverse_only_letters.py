"""
QUESTION #917 - REVERSE ONLY LETTERS
Difficulty: Easy
"""

# test case 1 - "ab-cd" returns "dc-ba"
# test case 2 - "a-bC-dEf-ghIj" returns "j-Ih-gfE-dCba"
# test case 3 - "Test1ng-Leet=code-Q!" returns "Qedo1ct-eeLg=ntse-T!"

def reverseOnlyLetters(S: str) -> str:

    i = 0
    j = len(S) - 1

    first_half = ""
    second_half = ""

    while i < j:
        while i < j and not S[i].isalpha():
            first_half += S[i]
            i += 1
        while i < j and not S[j].isalpha():
            second_half = S[j] + second_half
            j -= 1

        if i != j:
            second_half = S[i] + second_half
            first_half += S[j]
            i += 1
            j -= 1

    if i == j:
        first_half += S[i]

    return first_half + second_half


"""
NOTES:
- time complexity: O(N//2) since both i and j are always increasing/decreasing. N = length of string.
- string doesn't support item assignment
- still need to get better at testing manually without using a debugger or the console


RESULTS: faster than 79.29% of submissions, uses less storage than 44.70% of submissions

IMPROVEMENTS:
- list(object) is a constructor that returns a list! converts string into a list IN PLACE
- "".join() joins all items in an iterable object (list or dictionary) into a string with "" in between each item
"""
