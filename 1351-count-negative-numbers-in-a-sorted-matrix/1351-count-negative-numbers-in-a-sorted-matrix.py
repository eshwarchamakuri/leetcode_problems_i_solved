class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for g in range(len(grid)):
            for i in grid[g]:
                if i<0:
                    count+=1
        return count