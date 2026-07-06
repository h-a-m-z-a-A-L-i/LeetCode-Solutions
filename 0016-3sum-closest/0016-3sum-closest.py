class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums 
            
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
            
        def merge(left, right):
            sorted_array = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])
            return sorted_array

        
        nums = merge_sort(nums)  
        
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
                    
        return closest_sum  