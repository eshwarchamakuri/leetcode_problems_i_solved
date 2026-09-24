class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result=[i for i in range(len(nums)) if nums[i]==target]
        return result