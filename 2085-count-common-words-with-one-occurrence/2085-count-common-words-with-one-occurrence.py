class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        count=0
        for i in set(words1):
            if i in words1 and i in words2:
                if words1.count(i)==1 and words2.count(i)==1:
                    count+=1
        return count