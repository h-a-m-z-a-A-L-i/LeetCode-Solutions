class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        
        mid = (n + 1) // 2
        
        left = mid - 1
        right = n - 1
        
        temp = [0] * n
        for i in range(0, n, 2):
            temp[i] = sorted_nums[left]
            left -= 1
            
        for i in range(1, n, 2):
            temp[i] = sorted_nums[right]
            right -= 1
            
        for i in range(n):
            nums[i] = temp[i]