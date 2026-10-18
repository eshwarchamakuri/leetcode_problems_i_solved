class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        duplicate_stones=stones.copy()
        while len(stones)>1:
            x=max(stones)
            if len(stones) != 0:
                stones.remove(x)
            y=max(stones)
            if len(stones) != 0:
                stones.remove(y)
            if x!=y:
                stones.append(abs(y-x))
        if len(stones)!=0:
            return stones[0]
        else:
            return 0