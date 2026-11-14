class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        pos_min=float('inf')
        for i in range(len(nums)):
            for j in range(l,r+1):
                if i+j<=len(nums):
                    current_sum=sum(nums[i:i+j])
                    if current_sum>0:
                        if current_sum<pos_min:
                            pos_min=current_sum
        if pos_min==float('inf'):
            return -1
        else:
            return pos_min