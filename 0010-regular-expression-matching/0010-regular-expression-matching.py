class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0
        def dfs(i,j):
            if j==len(p):
                return i==len(s) # if both are empty then return True
            #if current char match the p or there is '.' in p 
            current_match = i<len(s) and (s[i]==p[j] or p[j] == '.')
            if (j+1) < len(p) and p[j+1] == '*':
                return dfs(i,j+2) or (current_match and dfs(i+1,j))
            # move forward if there is match
            if current_match:
                return dfs(i+1,j+1)
            return False
        return dfs(0,0)

