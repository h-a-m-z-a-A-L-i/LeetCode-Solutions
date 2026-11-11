class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = [str(n) for n in nums]
        
        strs.sort(key=lambda x: x * 10, reverse=True)
        
        result = "".join(strs)
        
        return "0" if result[0] == "0" else result