class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        
        mapping = {')':'(', '}':'{', ']': '['}

        for char in (s):
            if char in ('{','[','('):
                seen.append(char)
            elif char in ('}', ']', ')'):
                if len(seen)==0:
                    return False
                else:
                    top_element = seen[-1]
                    if mapping[char] != top_element:
                        return False
                    else:
                        seen.pop()
        
        return len(seen)==0



