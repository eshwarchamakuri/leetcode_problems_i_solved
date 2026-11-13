class Solution:
    def titleToNumber(self, e: str) -> int:
        e=e[::-1]
        n=len(e)
        value=0
        for i in range(len(e)):
            letter_value=ord(e[i])-ord('A')+1
            value=value+((pow(26,i))*letter_value)
        return value
        