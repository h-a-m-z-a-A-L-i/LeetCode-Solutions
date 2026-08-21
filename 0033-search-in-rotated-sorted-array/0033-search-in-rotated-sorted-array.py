class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) -1
        while(lower<=upper):
            mid = lower+(upper - lower)//2
            if nums[mid] == target:
                return mid

            # left sorted
            if nums[lower] <= nums[mid]:
                if nums[lower] <= target <= nums[mid]:
                    upper = mid-1
                else:
                    lower = mid+1
            
            # Right sorted
            elif nums[mid]<=nums[upper]:
                if nums[mid] <= target <= nums[upper]:
                    lower = mid+1
            
                else:
                    upper = mid-1

        return -1
                
            

                

