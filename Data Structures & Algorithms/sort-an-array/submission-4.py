class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def split(t):
            n = len(t)
            return t[:n // 2], t[n // 2:]

        def fusion(t1, t2):
            result = []
            i = j = 0

            while i < len(t1) and j < len(t2):
                if t1[i] <= t2[j]:
                    result.append(t1[i])
                    i += 1
                else:
                    result.append(t2[j])
                    j += 1

            # Ajouter les éléments restants
            result.extend(t1[i:])
            result.extend(t2[j:])

            return result

        def sort(t):
            if len(t) <= 1:
                return t

            t1, t2 = split(t)

            t1 = sort(t1)
            t2 = sort(t2)

            return fusion(t1, t2)

        return sort(nums)