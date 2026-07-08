class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ls = []
        if len(digits) == 0:
            return []
        
        def trace(idx, current_string):
            if idx == len(digits):
                ls.append(current_string)
                return
            letters = dic[digits[idx]]
            for char in letters:
                trace(idx + 1, current_string+char)
        trace(0,"")
        return ls