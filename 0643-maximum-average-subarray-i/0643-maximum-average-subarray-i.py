class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sliding_window=sum(nums[:k])
        max_count=sliding_window
        for i in range(k,len(nums)):
            sliding_window-=nums[i-k]
            sliding_window+=nums[i]
            max_count=max(sliding_window,max_count)
        return max_count/k

            