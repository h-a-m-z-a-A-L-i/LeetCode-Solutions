class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        sign = -1 if x<0 else 1
        if x<0:
            x = abs(x)
        for i in range(len(str(x))):
            last = x%10
            
            reversed_num = (reversed_num * 10) + last
            x = x //10
        if reversed_num < -2147483648 or reversed_num > 2147483647:
            return 0
        else:
            return sign * reversed_num
            
