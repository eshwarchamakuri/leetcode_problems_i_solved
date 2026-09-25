class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x1=abs(z-x)
        y1=abs(z-y)
        if x1<y1:
            return 1
        elif x1>y1:
            return 2
        else:
            return 0