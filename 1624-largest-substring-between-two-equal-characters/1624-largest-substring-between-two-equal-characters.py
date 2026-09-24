class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_count=0
        flag=False
        for i in range(len(s)):
            first=i+1
            for j in range(i+1,len(s)):
                if s[j]==s[i]:
                    second=j
                    if max_count<abs(first-second):
                        max_count=abs(first-second)
                    flag=True
        if flag==False:
            return -1
        else:
            return max_count
        
