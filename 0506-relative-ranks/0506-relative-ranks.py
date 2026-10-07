class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp=sorted(score)
        max_nums=(temp[::-1])[:3]
        freq={}
        count=0
        for i in temp[::-1]:
            count+=1
            if i in max_nums:
                if i==max_nums[0]:
                    freq[i]='Gold Medal'
                elif i==max_nums[1]:
                    freq[i]='Silver Medal'
                else:
                    freq[i]='Bronze Medal'
            else:
                freq[i]=str(count)
        result=[]
        for s in score:
            result.append(freq[s])
        return result