class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Step 1: Sort the array to easily manage duplicates and use two pointers
        nums.sort()
        
        for i in range(len(nums) - 2):
            # If the current number is greater than 0, the remaining numbers 
            # will also be greater than 0, making it impossible to sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Initialize two pointers for the remaining part of the array
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    # Sum is too small, move the left pointer to increase the sum
                    left += 1
                elif total > 0:
                    # Sum is too large, move the right pointer to decrease the sum
                    right -= 1
                else:
                    # Found a valid triplet!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicate values for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Advance past the last unique elements
                    left += 1
                    right -= 1
                    
        return res