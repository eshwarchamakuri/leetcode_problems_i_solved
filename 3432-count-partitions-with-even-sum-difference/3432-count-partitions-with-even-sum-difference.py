class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-1):
            total=sum(nums[0:i])-sum(nums[i:len(nums)])
            if total % 2==0:
                count+=1
        return count