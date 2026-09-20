class Solution:
    def reverseDegree(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            d=ord('Z')-ord(s[i])
            t=d+33
            count+=(i+1)*t
        return count