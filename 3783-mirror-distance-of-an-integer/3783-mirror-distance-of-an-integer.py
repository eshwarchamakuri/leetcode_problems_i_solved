class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n-int("".join([i for i in str(n)][::-1])))