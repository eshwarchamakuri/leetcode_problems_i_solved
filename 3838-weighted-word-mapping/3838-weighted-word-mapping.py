class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        s=""
        for word in words:
            total=0
            for j in word:
                pos=ord(j)-ord('a')+1
                total+=weights[pos-1]
            mod=26-(total%26)
            alpha=chr(97+mod-1)
            s+=alpha
        return s