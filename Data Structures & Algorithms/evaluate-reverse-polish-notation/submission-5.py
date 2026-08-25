class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operateurs = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token not in operateurs:
                stack.append(int(token))
            else:
                droite = stack.pop()
                gauche = stack.pop()

                if token == "+":
                    resultat = gauche + droite
                elif token == "-":
                    resultat = gauche - droite
                elif token == "*":
                    resultat = gauche * droite
                else:
                    resultat = int(gauche / droite)

                stack.append(resultat)

        return stack[-1]