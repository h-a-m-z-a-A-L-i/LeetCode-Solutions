class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = []
        max_size = 0
        for i,char in enumerate(s):


            while char in ls:
                ls.pop(0)
            ls.append(char)
                
            max_size = max(max_size, len(ls))

        return max_size
