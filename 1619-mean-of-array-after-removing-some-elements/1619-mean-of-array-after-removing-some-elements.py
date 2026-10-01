import numpy as np
class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        n=len(arr)
        rem=int(n*0.05)
        arr=arr[rem:n-rem]
        return float(np.mean(arr))
