class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        count=len(nums)
        average=sum(nums)/count
        for i in range(1,10000):
            if i>average and i not in nums:
                return i
                break
        