class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged)%2 == 0:
            median = (merged[(len(merged)//2) -1 ] + 
            merged[(len(merged)//2)])/2
        else:
            median = merged[len(merged)//2]
        return median