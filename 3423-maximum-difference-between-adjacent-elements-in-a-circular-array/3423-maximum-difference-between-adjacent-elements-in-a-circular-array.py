class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_difference=0
        for i in range(len(nums)-1):
            if abs(nums[i]-nums[i+1])>max_difference:
                max_difference=abs(nums[i]-nums[i+1])
        if abs(nums[0]-nums[len(nums)-1])>max_difference:
            max_difference=abs(nums[0]-nums[len(nums)-1])
        return max_difference