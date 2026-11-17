class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        if n < 2:
            return n
            
        count = 1
        prev_diff = 0
        
        for i in range(1, n):
            curr_diff = nums[i] - nums[i - 1]
            
            if (curr_diff > 0 and prev_diff <= 0) or (curr_diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = curr_diff
                
        return count