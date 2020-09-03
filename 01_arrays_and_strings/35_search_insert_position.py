"""
QUESTION #35 - SEARCH INSERT POSITION
Difficulty: Easy
"""

# test case 1 - [1,3,5,6] and 7 returns 4
# test case 2 - [1,3,5,6] and 0 returns 0
# test case 3 - [1,3,5,6] and 2 returns 1
# test case 4 - [1,3,5,6] and 6 returns 3
# test case 5 - [] and 5 returns 0


def searchInsert(nums, target):
    # use of edge cases OUTSIDE recursive function to reduce time complexity
    if len(nums) == 0:
        return 0
    if target > nums[len(nums) - 1]:
        return len(nums)
    if target < nums[0]:
        return 0

    return binarySearch(nums, target, 0, len(nums) - 1)


def binarySearch(nums, target, low, high):
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid

    if low >= high:
        if nums[low] < target:
            return low + 1
        else:
            return low

    if nums[mid] > target:
        return binarySearch(nums, target, low, mid - 1)
    else:
        return binarySearch(nums, target, mid + 1, high)


"""
NOTES:
- need to get better at coming up with my own test cases!
- time complexity: O(log N) where N = len(nums)
- how do you deal with the trade-off between time complexity and space complexity in an interview setting?

RESULTS: faster than 86.82% and memory usage less than 78.76% of submissions

IMPROVMENTS:
- always try to account for edge cases that can be solved in constant time separately and outside the recursive function
"""