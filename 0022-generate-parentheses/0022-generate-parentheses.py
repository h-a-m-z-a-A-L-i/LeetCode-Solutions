class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ls = []
        brackets = ""
        open = n
        close = n
        def trace(brackets, open , close):
            if open == 0 and close ==0:
                ls.append(brackets)
                brackets = ""
                return
            if open>0:
                trace(brackets + "(", open -1, close)
            if close > open and close > 0:
                trace(brackets + ")", open, close - 1)

        trace("", n, n)
        return ls
