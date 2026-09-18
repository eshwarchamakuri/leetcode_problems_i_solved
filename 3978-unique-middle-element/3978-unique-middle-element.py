class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n=len(nums)//2
        unique=nums[n]
        if nums.count(unique)==1:
            return True
        else:
            return False