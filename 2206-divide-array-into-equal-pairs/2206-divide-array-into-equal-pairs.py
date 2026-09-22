class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        result=True
        for i in set(nums):
            if nums.count(i) %2 !=0:
                result=False
                break
        return result
