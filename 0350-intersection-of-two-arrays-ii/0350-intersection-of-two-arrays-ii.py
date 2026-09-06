class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
            
        res = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                res.append(num)
                counts[num] -= 1
                
        return res