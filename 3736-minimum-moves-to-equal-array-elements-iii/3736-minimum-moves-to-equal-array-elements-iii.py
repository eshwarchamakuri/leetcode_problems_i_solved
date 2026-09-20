class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_element=max(nums)
        count=0
        for i in nums:
            count+=abs(i-max_element)
        return count