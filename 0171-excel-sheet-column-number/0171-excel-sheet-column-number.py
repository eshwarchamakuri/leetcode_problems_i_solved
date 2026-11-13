class Solution:
    def titleToNumber(self, e: str) -> int:
        e=e[::-1]
        n=len(e)
        value=0
        for i in range(len(e)):
            value=value+((pow(26,i))*(ord(e[i])-ord('A')+1))
        return value
        