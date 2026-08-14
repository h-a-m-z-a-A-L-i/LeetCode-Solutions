class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to their Roman numeral symbols in descending order
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        roman_numeral = []
        
        # Loop through the map and extract pieces greedily
        for value, symbol in value_map:
            if num == 0:
                break
            # Determine how many times this symbol fits into num
            count = num // value
            if count > 0:
                roman_numeral.append(symbol * count)
                num -= value * count
                
        return "".join(roman_numeral)