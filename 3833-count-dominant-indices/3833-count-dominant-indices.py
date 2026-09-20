class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-1):
            digit_sum=0
            digit_count=0
            for j in range(i+1,len(nums)):
                digit_sum +=nums[j]
                digit_count+=1
            average=digit_sum/digit_count
            if nums[i]>average:
                count+=1
        return count