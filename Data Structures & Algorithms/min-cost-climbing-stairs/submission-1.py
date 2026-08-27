class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m={}
        n=len(cost)
        def rec(i):
            if i<0:
                return 0
            if i<=1:
                return cost[i]
            if i in m:
                return m[i]
            a= rec(i-1)
            b = rec(i-2)
            m[i]=min(a,b) + (cost[i] if i < len(cost) else 0)
            return m[i]
        return rec(n)