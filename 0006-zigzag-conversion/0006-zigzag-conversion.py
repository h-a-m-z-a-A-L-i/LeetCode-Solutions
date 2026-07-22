class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cycle_len = 2* numRows -2 # Full cycle like a wheel

        for i , char in enumerate(s):
                
            idx = i% cycle_len
                
            # if idx<numRows going up , else down
            row = idx if idx < numRows else cycle_len - idx
            rows[row]+=char
        return ''.join(rows)


