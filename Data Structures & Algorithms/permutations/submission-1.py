class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)
        used = [False] * n

        def dfs():
            if len(curr) == n:
                res.append(curr.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                # Choisir nums[i]
                curr.append(nums[i])
                used[i] = True

                dfs()

                # Annuler le choix
                curr.pop()
                used[i] = False

        dfs()
        return res