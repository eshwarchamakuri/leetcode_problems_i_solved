class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        def valid(n,arr):
            result=True
            for i in arr:
                if n <= i:
                    result=False
                    break
            return result
        lst=[]
        for i in range(len(nums)):
            v1=valid(nums[i],nums[:i])
            v2=valid(nums[i],nums[i+1:])
            if v1==True or v2==True:
                lst.append(nums[i])
        return lst