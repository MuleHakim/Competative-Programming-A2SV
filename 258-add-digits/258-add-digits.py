class Solution:
    def addDigits(self, num: int) -> int:
        if num > 0: 
            return ((num - 1) % 9) + 1
        else:
            return 0