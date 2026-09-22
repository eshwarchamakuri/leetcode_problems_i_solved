class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        lst=[]
        for i in range(len(nums)):
            if i%10==nums[i]:
                lst.append(i)
        print(lst)
        if len(lst) != 0:
            return min(lst)
        else:
            return -1