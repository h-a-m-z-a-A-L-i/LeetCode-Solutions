class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        curr = 1
        
        for k in range(1, rowIndex + 1):
            curr = curr * (rowIndex - k + 1) // k
            row.append(curr)
            
        return row