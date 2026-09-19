class Solution:
    def similarPairs(self, words: list[str]) -> int:
        count=0
        result=[]
        for i in words:
            result.append(set(i))
        for i in range(len(result)):
            for j in range(i+1,len(result)):
                if result[i]==result[j]:
                    count+=1
        return count