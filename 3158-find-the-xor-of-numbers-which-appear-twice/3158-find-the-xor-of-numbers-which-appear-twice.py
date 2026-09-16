class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in range(len(nums)-1):
            if nums[i]^nums[i+1]==0:
                result=result^nums[i]
        return result