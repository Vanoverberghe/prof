class Pile1:
    
    def __init__(self):
        """
        Crée une pile vide
        """
        self._tableau = []

    def est_vide(self):
        """
        Renvoie True ssi je suis une pile vide.
        """
        return len(self._tableau) == 0

    def taille(self):
        """
        Renvoie ma taille (en nombre d'éléments empilés)
        """
        return len(self._tableau)

    def empiler(self, valeur):
        """
        Empile un nouvel élément en mon sommet.
        """
        self._tableau.append(valeur)

    def depiler(self):
        """
        Dépile et renvoie la valeur de l'élément placé en mon
        sommet.

        Déclenche une erreur si je suis vide.
        """
        if self.est_vide():
            raise IndexError("Dépiler sur une pile vide")
        else:
            return self._tableau.pop()

    def consulter(self):
        """
        Renvoie la valeur de l'élément placé en mon
        sommet.

        Déclenche une erreur si je suis vide.
        """
        if self.est_vide():
            raise IndexError("Dépiler sur une pile vide")
        else:
            return self._tableau[self.taille() - 1]

    def vider(self):
        """
        Enlève tous les éléments empiles.
        """
        self._tableau = []

    def __str__(self):
        N = self.taille()

        chaîne = "("

        i = 0
        while i < N:
            chaîne += str(self._tableau[i])
            if i == N - 2:
                chaîne += " | "
            elif i < N - 2:
                chaîne += " "
            i += 1

        chaîne += ")"

        return chaîne

    def __repr__(self):
        return str(self)