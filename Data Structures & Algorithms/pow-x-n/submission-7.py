class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(k):
            if k == 0:
                return 1.0

            half = recur(k // 2)
            if k % 2 == 0:
                return half * half
            return half * half * x

        if n < 0:
            return 1 / recur(-n)
        return recur(n)