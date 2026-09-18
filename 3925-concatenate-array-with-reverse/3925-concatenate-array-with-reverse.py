class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        original=nums
        reverse=nums[::-1]
        total=original+reverse
        return total