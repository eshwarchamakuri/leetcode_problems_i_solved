class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        lst=[]
        cap=[]
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                lst.append(i)
                cap.append(capacity[i]-itemSize)
        min_dif=float('inf')
        index=-1
        for i in range(len(cap)):
            if cap[i]<min_dif:
                min_dif=cap[i]
                index=lst[i]
        return index