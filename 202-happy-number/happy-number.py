class Solution:
    def isHappy(self, n: int) -> bool:
        h = set()
        while(n != 1):
            sum = 0
            while n > 0:
                d = n % 10
                n = n // 10
                sum = sum + d * d
            if sum in h:
                return False
            h.add(sum)
            n = sum
        return True
       