class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            subarray=nums[i:i+3]
            sum1=subarray[0]+subarray[-1]
            mid=subarray[1]/2
            if sum1==mid:
                count+=1
        return count
