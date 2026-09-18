class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        unique=-1
        for i in range(len(nums)):
            if nums.count(nums[i])==1 and nums[i]%2==0:
                unique=nums[i]
                break
        return unique