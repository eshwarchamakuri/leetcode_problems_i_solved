class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        result=[]
        for i in set(nums):
            for j in set(nums):
                if i<j and nums.count(i)!=nums.count(j):
                    result.append([i,j])
        result.sort()
        if len(result)==0:
            return [-1,-1]
        else:
            return result[0]
        