class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        count=float('inf')
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==1 and nums[j]==2:
                    if abs(i-j) <count:
                        count=abs(i-j)
        if count==float('inf'):
            return -1
        else:
            return count