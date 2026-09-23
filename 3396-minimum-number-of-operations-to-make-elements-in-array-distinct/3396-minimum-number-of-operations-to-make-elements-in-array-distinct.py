class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while len(nums) != 0:
            result=False
            for i in set(nums):
                if nums.count(i)>1:
                    result=True
            if result==True:
                nums=nums[3:]
                count+=1
            else:
                return count
        return count