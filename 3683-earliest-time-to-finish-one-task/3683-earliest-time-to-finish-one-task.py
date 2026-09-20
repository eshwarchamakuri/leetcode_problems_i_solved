class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        low_sum=float('inf')
        for i in tasks:
            if sum(i)<low_sum:
                low_sum=sum(i)
        return low_sum