"""
QUESTION #20 - VALID PARENTHESES
Difficulty: Easy
"""

# test case 1 - "((})" returns False
# test case 2 - "(){}[" returns False (odd length, edge case)
# test case 3 - "{}[]()" returns True
# test case 4 - "({[]})" returns True
# test case 5 - "((" returns False (didn't come up with this one myself)

def isValid(s) -> bool:
    if len(s) % 2 != 0:
        return False

    openbrackets = ["(", "{", "["]
    brackets = []

    for index in range(len(s)):
        if s[index] in openbrackets:
            brackets.append(s[index])
            continue

        if len(brackets) > 0:
            check = brackets.pop()
        else:
            return False

        if s[index] == ")" and check == "(":
            continue
        elif s[index] == "}" and check == "{":
            continue
        elif s[index] == "]" and check == "[":
            continue
        else:
            return False

    if len(brackets) == 0:
        return True
    else:
        return False

"""
NOTES:
- how do you come up with better test cases? Is there a systematic way to do so?
- made a few syntax errors, need to be more careful!!
- time complexity: O(N) where N = len(s)

RESULTS: faster than 39.38% and memory usage less than 87.02% of submissions

IMPROVEMENTS:
- Using hash maps makes comparison of corresponding brackets easier & faster
"""