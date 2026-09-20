class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        min_count=float('inf')
        n=list(str(n))
        for i in set(n):
            if n.count(i)<min_count:
                min_count=n.count(i)
        min_number=float('inf')
        for i in set(n):
            if int(i)<min_number and n.count(i)==min_count:
                min_number=int(i)
        return min_number

