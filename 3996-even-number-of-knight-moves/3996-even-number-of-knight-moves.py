class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        if (start[0]+start[1])%2==(target[0]+target[1])%2:
            return True
        else:
            return False