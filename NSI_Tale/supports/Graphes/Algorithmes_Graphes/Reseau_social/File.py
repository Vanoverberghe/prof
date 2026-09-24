class File1:

    def __init__(self):
        """
        Crée une file vide
        """
        self._tableau = []

    def est_vide(self):
        """
        Renvoie True ssi je suis une file vide.
        """
        return len(self._tableau) == 0

    def taille(self):
        """
        Renvoie ma taille (en nombre d'éléments emfilés)
        """
        return len(self._tableau)
 
    def enfiler(self, valeur):
        """
        Enfile un nouvel élément.
        """
        self._tableau.append(valeur)

    def defiler(self):
        """
        Défile et renvoie la valeur de l'élément placé premier
        dans la file (le plus ancien).

        Déclenche une erreur si je suis vide.
        """
        if self.est_vide():
            raise IndexError("Défiler sur une file vide")
        else:
            return self._tableau.pop(0)

    def consulter(self):
        """
        Renvoie la valeur de l'élément placé en position
        de défilement (la valeur la plus ancienne).

        Déclenche une erreur si je suis vide.
        """
        if self.est_vide():
            raise IndexError("Défiler sur une file vide")
        else:
            return self._tableau[0]

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
            if i < N - 1:
                chaîne += " ← "
            i += 1

        chaîne += ")"

        return chaîne

    def __repr__(self):
        return str(self)