class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        min_index=float('inf')
        for i in range(len(nums)):
            sum1=0
            while nums[i]!=0:
                rev=nums[i]%10
                sum1+=rev
                nums[i]=nums[i]//10
            if sum1==i:
                if i<min_index:
                    min_index=i
        if min_index != float('inf'):
            return min_index
        else:
            return -1