class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        min_element=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                if abs(i-start)<min_element:
                    min_element=abs(i-start)
        return min_element