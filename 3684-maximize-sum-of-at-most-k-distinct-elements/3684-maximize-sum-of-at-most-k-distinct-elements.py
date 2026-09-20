class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums=list(set(nums))
        nums.sort()
        nums=nums[::-1]
        result=nums[:k]
        return result
