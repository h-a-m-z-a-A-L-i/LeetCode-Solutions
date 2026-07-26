class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        ls = []
        sign = 1
        # 1. Skip all spaces first
        while i < len(s) and s[i] == " ":
            i += 1

        # 2. Check for a sign exactly once (Safety check: make sure i is still in bounds!)
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        while i<len(s) and s[i].isdigit():

            ls.append(s[i])
            i+=1
        
        
        if ls:
            digit =int("".join(ls))
            if sign:
                digit =sign * (digit)

            
            if digit < -2**31:
                return -2**31
            if digit > 2**31 - 1:
                return 2**31 -1
            return digit
        else:
            return 0
