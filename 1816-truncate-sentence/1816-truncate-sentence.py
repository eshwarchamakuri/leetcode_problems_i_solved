class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        result=[]
        for i in range(k):
            result.append(s[i])
        return " ".join(result)