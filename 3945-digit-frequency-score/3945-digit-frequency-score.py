class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s=list(str(n))
        count=0
        for i in set(s):
            mul=s.count(i)
            count+=int(i)*mul
        return count