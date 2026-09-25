class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]
        for i in range(0,len(nums),2):
            for j in (nums[i:i+2])[::-1]:
                result.append(j)
                

        return result

