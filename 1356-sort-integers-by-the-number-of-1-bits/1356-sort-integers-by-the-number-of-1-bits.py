class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        binary=[]
        for i in arr:
            binary.append(int((bin(i)[2:]).count('1')))
        binary.sort()
        result=[]
        for i in set(binary):
            for j in arr:
                if i==int(bin(j)[2:].count('1')):
                    result.append(j)
        return result