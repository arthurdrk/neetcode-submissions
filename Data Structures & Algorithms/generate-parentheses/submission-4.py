class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(opening, closing):
            # n parenthèses ouvrantes et n fermantes
            if opening == n and closing == n:
                res.append("".join(curr))
                return

            # Ajouter une parenthèse ouvrante
            if opening < n:
                curr.append("(")
                dfs(opening + 1, closing)
                curr.pop()

            # Ajouter une parenthèse fermante
            if closing < opening:
                curr.append(")")
                dfs(opening, closing + 1)
                curr.pop()

        dfs(0, 0)
        return res