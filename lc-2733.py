# Given an integer array `nums` containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

# Return the selected integer.

class Solution: 
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return -1 if len(nums) <= 2 else sorted(nums)[-2]