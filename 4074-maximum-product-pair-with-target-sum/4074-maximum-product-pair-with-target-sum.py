class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        max_product=float('-inf')
        o=-1
        m=-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target and nums[i]>nums[j]:
                    if nums[i]*nums[j]>max_product:
                        max_product=nums[i]*nums[j]
                        o=i
                        m=j
        return [o,m]