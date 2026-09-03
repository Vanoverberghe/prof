import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    """
    Classe représentant un graphe à partir d'une matrice d'adjacence
    """
    
    def __init__(self, nb_sommets):
        # Attribut qui représente une matrice de dimensions remplie de 0 au départ ( nb_sommets * nb_sommets )
        self.mat = [[0 for _ in range(nb_sommets)] for _ in range(nb_sommets)]
        
        # Liste de tout les sommets présents dans le graphe,
        # ils doivent être dans l'ordre dans lequel ils se trouvent dans la matrice.
        self.sommets = [chr(i+65) for i in range(nb_sommets)]
        
    def afficher_matrice(self):
        """
        Affiche proprement la matrice du graphe 
        """
        print(*self.mat, sep="\n")
        
    def get_matrice(self):
        """
        Renvoie la matrice d'adjacence du graphe
        """
        return self.mat
    
    def get_sommets(self):
        """
        Renvoie tout les sommets du graphe
        """
        return self.sommets
        
    def est_oriente(self):
        """
        Renvoies True si le graphe est orienté, faux sinon
        
        Pré-condition : la matrice doit être carrée
        """
        for i in range(len(self.mat)):
            for j in range(i+1, len(self.mat)):
                if self.mat[i][j] != self.mat[j][i]:
                    return True
        return False
    
    def indice_sommet(self, nom_sommet):
        """
        Renvoies l'indice d'un sommet du graphe ( A quelle ligne/colonne corresponds-t-il dans la matrice )
        
        L'indice dans la matrice et dans la liste de sommets est normalement le même.
        
        Pré-condition: nom_sommet est un nom de sommet deja présent dans le graphe.
        """
        return self.sommets.index(nom_sommet)
        
        
    def ajouter_sommet(self, nom_sommet):
        """
        Ajoute un sommet dans le graphe au dernier emplacement de la liste des sommets.
        On ajoutera aussi une nouvelle colonne et une nouvelle ligne correspondant bien au sommet ajouté.
        A l'ajout, le sommet n'a aucun lien avec les autres sommets
        
        Pré-condition : nom_sommet n'est pas encore utilisé dans le graphe, s'il l'est, ne rien faire.
        
        Effets de bord: modifie self.mat et self.sommets
        """
        self.sommets.append(nom_sommet)
        for ligne in self.mat:
            ligne.append(0)
        self.mat.append([0] * len(self.mat[0]))
        
    def supprimer_sommet(self, nom_sommet):
        """
        Supprime un des sommets du graphe en le supprimant de la liste des sommets
        et en supprimant toute la ligne et la colonne associé à ce sommet.
        
        Pré-condition : nom_sommet existe deja dans le graphe, sinon ne rien faire.
        
        Effets de bord: modifie self.mat et self.sommets
        """
        if nom_sommet in self.sommets:
            ind = self.indice_sommet(nom_sommet)
            self.mat.pop(ind)
            for ligne in self.mat:
                ligne.pop(ind)
            self.sommets.pop(ind)
        
    def ajouter_lien(self, sommet1, sommet2, oriente = False):
        """
        Ajoute un lien entre le sommet 1 et le sommet 2, ajoute une arête si oriente = False,
        un arc allant de sommet1 vers sommet2 si oriente = True
        
        Effet de bord: modifie self.mat
        """
        ind1 = self.indice_sommet(sommet1)
        ind2 = self.indice_sommet(sommet2)
        self.mat[ind1][ind2] = 1
        if not oriente:
            self.mat[ind2][ind1] = 1
            
    def supprime_lien(self, sommet1, sommet2, oriente = False):
        """
        Supprime le lien entre le sommet 1 et le sommet 2, supprime tout le lien oriente = False,
        supprime le sens sommet1 vers sommet2 si oriente = True
        
        Effet de bord: modifie self.mat
        """
        ind1 = self.indice_sommet(sommet1)
        ind2 = self.indice_sommet(sommet2)
        self.mat[ind1][ind2] = 0
        if not oriente:
            self.mat[ind2][ind1] = 0
            
    def successeurs(self, sommet):
        """
        Renvoies la liste des successeurs de sommet dans le graphe grace à la matrice d'adjacence
        
        Pré-condition : sommet est présent dans le graphe
        """
        ind = self.indice_sommet(sommet)
        res = []
        for i in range(len(self.mat)):
            if self.mat[ind][i] == 1:
                res.append(self.sommets[i])
        return res
    
    def predecesseurs(self , sommet):
        """
        Renvoies la liste des predecesseurs de sommet dans le graphe grace a la matrice d'adjacence
        
        Pré-condition : sommet est présent dans le graphe
        """
        ind = self.indice_sommet(sommet)
        res = []
        i = 0
        while i < len(self.mat):
            if self.mat[i][ind] == 1:
                res.append(self.sommets[i])
            i+=1
        return res
    
    def voisins(self, sommet):
        """
        Renvoies la liste des voisins de sommet dans le graphe
        Les successeurs et prédécesseurs sont tous voisin de sommet.
        
        Pré-condition : sommet est présent dans le graphe
        """
        pred = self.predecesseurs(sommet)
        succ = self.successeurs(sommet)
        res = pred
        for s in succ:
            if s not in pred:
                res.append(s)
        return res
        
    def degre_sortant(self, sommet):
        """
        Renvoie le degré sortant du sommet passé en argument
        """
        return len(self.successeurs(sommet))
    
    def degre_entrant(self, sommet):
        """
        Renvoie le degré du sommet passé en argument
        """
        return len(self.predecesseurs(sommet))
    
    def degre(self, sommet):
        """
        Renvoie le degré du sommet passé en argument
        """
        return len(self.voisins(sommet))
    
    def matrice_to_liste(self):
        """
        Renvoies les listes de successeurs correspondant au graphe
        
        Les clés seront les noms des sommets
        """
        res = dict()
        for i in range(len(self.mat)):
            sommet = self.sommets[i]
            res[sommet] = self.successeurs(sommet)
        return res
    
    def affiche_graphe(self):
        """
        Genere la visualisation du graphe a l'aide de networkx.
        
        Le choix de la représentation utilisé est libre.
        """
        G = nx.DiGraph() if self.est_oriente() else nx.Graph()

        # Ajout des sommets
        G.add_nodes_from(self.sommets)

        # Ajout des arêtes selon la matrice d'adjacence
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                if self.mat[i][j] == 1:
                    G.add_edge(self.sommets[i], self.sommets[j])

        # Dessiner le graphe
        pos = nx.spring_layout(G)  # Positionnement automatique
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12)

        # Affichage
        plt.show()
