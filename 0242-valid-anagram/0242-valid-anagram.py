class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       d1=collections.Counter(s)
       d2=collections.Counter(t)
       return d1==d2