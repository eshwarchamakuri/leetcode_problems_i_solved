class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        big=sum(nums[:k])
        nums=nums[::-1]
        small=sum(nums[:k])
        return abs(small-big)
        