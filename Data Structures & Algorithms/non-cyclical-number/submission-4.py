class Solution:
    def isHappy(self, n: int) -> bool:
        d=set()
        def compute_sum(n):
            l=str(n)
            return sum([int(x)**2 for x in l])
        somme=n
        while somme!=1 and not somme in d:
            
            d.add(somme)
            somme=compute_sum(somme)
        return somme==1
