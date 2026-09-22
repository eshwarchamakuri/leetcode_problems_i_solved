class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums1=nums
        max1=max(nums)
        nums.remove(max1)
        max2=max(nums)
        max_product=max1*max2
        min1=min(nums1)
        nums1.remove(min1)
        min2=min(nums1)
        min_product=min1*min2
        total_product=max_product-min_product
        return total_product

        
        
