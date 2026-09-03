from graphviz import Graph

class Labyrinthe:
    
    def __init__(self, taille):
        self.taille = taille
        
        self.cellules = [str(i) for i in range(self.taille**2)]
            
        
        self.graphe = {}
        for cellule in self.cellules:
            self.graphe[cellule] = []
            
    def affiche_graphe(self):
        """
        Affiche le graphe associé au labyrinthe avec graphviz et la liste d'adjacences en attribut
        """
        pass
            
    def casser_mur(self, cellule1, cellule2):
        """
        Casse le mur entre cellule1 et cellule2, c'est à dire relie les sommets cellule1 et cellule2 par une arête.
        
        Pré-condition: les cellules doivent être adjacentes.
        """
        pass
        
    def casser_murs(self,liste_murs):
        """
        En utilisant la méthode casser_mur, casse la liste de murs passée en paramètre
        """
        pass
            
    
    def profondeur_cycle(self, depart, parent, visites):
        """
        Utilise un parcours en profondeur pour savoir si il y a un cycle dans le graphe à partir de depart
        """
        visites[depart] = True
        
        for voisin in self.graphe[depart]:
            if not visites[voisin]:
                if self.profondeur_cycle(..., ..., ...):
                    return True
            elif voisin != parent:
                return ...
        return ...
    
    def est_cyclique(self):
        """
        Renvoies True si le labyrinthe contient au moins 1 cycle, Faux sinon
        """
        visites = {cellule: False for cellule in self.cellules}
        pass
    
    def est_connexe(self):
        """
        En utilisant les dimensions du labyrinthe et un parcours, dire si le labyrinthe est connexe
        ( pas de cellules seules ou en plusieurs groupes)
        """
        pass
    
    def est_parfait(self):
        """
        Renvoies True si le labyrinthe est parfait ( qu'il ne contient pas de cycles et qui a 1 seule composante connexe
        """
        pass
    
    
    def chemin_largeur(self, depart):
        """
        Utilise un parcours en largeur depuis depart.
        Renvoies le dictionnaire de parent défini.
        Pour garder en mémoire le chemin pour pouvoir le retrouver, on utilise un dictionnaire qui à chaque voisin non visité
        du sommet_courant, on associe le sommet courant en tant que valeur ( parent ). 
        """
        pass
    
    def remonte_chemin(self, arrivee, depart, parents):
        """
        Renvoies la liste correspondant au chemin entre arrivee et depart en utilisant les parents trouvé grace à chemin_largeur
        """
        pass
    
    
    
    def affiche_labyrinthe(self):
        print(self.ligne())
        for i in range(self.taille):
            print(self.ligne2())
            print(self.generer_colonne(i))
            print(self.ligne2())
            print(self.generer_ligne(i))
            
    def ligne(self):
        return "+-----"*self.taille+"+"
    
    def ligne2(self):
        return "|     "*self.taille + "|"

    def generer_colonne(self, i):
        s = ""
        for j in range(self.taille):
            if self.is_case_debut(i, j):
                s += f"|  {self.cellules[i*self.taille+j]:2} "
            elif not self.is_case_liee_precedente(i, j):
                s += f"|  {self.cellules[i*self.taille+j]:2} "
            else:
                s += f"   {self.cellules[i*self.taille+j]:2} "
        return s + "|"
    
    def generer_ligne(self, i):
        s = ""
        if i < self.taille:
            for j in range(self.taille):
                if str((i+1)*self.taille+j) in self.graphe[str((i)*self.taille+j)] :
                    s+="+-   -"
                else:
                    s+="+-----"
        else:
            s += "+-----"*self.taille
        s+="+"
        return s

    def is_case_debut(self, i, j):
        return i*self.taille + j == 0

    def is_case_liee_precedente(self, i, j):
        return str(i*self.taille + j) in self.graphe[str(i*self.taille + j - 1)]


# laby1 = Labyrinthe(5)
# murs1 = [(0,5),(5,10),(10,11),(11,6),(6,7),(7,8),(8,3),(3,2),(2,1),(11,16),(16,15),(16,21),(21,20),(7,12),(12,13),(12,17),(17,18),(18,19),(19,14),(14,9),(9,4),(18,23),(23,24),(23,22)]
# laby1.casser_murs([(str(i),str(j)) for i,j in murs1])
# 
# laby2 = Labyrinthe(5)
# murs2 = [(0,5),(5,10),(10,11),(11,16),(16,15),(16,17),(17,18),(18,19),(11,6),(6,1),(1,2),(1,3),(3,8),(8,13),(13,18),(12,7),(4,9),(9,14),(14,19),(20,21),(21,22),(23,24)]
# laby2.casser_murs([(str(i),str(j)) for i,j in murs2])