class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                ancien_indice=stack.pop()
                res[ancien_indice]=i-ancien_indice
                
            stack.append(i)
        return res


                