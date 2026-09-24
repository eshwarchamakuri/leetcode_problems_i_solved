class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        i=0
        j=len(nums)-1
        result=[]
        while i<j:
            result.append(nums[i]+nums[j])
            i+=1
            j-=1
        return max(result)