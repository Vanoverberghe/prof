import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    """
    Classe représentant un graphe à partir d'une matrice d'adjacence
    """
    
    def __init__(self, nb_sommets):
        # Attribut qui représente une matrice de dimensions remplie de 0 au départ ( nb_sommets * nb_sommets )
        self.mat = . . . 
        
        # Liste de tout les sommets présents dans le graphe,
        # ils doivent être dans l'ordre dans lequel ils se trouvent dans la matrice.
        self.sommets = . . .
        
    def afficher_matrice(self):
        """
        Affiche proprement la matrice du graphe 
        """
        pass
        
    def get_matrice(self):
        """
        Renvoie la matrice d'adjacence du graphe
        """
        pass
    
    def get_sommets(self):
        """
        Renvoie tout les sommets du graphe
        """
        pass
        
    def est_oriente(self):
        """
        Renvoies True si le graphe est orienté, faux sinon
        
        Pré-condition : la matrice doit être carrée
        """
        pass
    
    def indice_sommet(self, nom_sommet):
        """
        Renvoies l'indice d'un sommet du graphe ( A quelle ligne/colonne corresponds-t-il dans la matrice )
        
        L'indice dans la matrice et dans la liste de sommets est normalement le même.
        
        Pré-condition: nom_sommet est un nom de sommet deja présent dans le graphe.
        """
        pass
        
        
    def ajouter_sommet(self, nom_sommet):
        """
        Ajoute un sommet dans le graphe au dernier emplacement de la liste des sommets.
        On ajoutera aussi une nouvelle colonne et une nouvelle ligne correspondant bien au sommet ajouté.
        A l'ajout, le sommet n'a aucun lien avec les autres sommets
        
        Pré-condition : nom_sommet n'est pas encore utilisé dans le graphe, s'il l'est, ne rien faire.
        
        Effets de bord: modifie self.mat et self.sommets
        """
        pass
        
    def supprimer_sommet(self, nom_sommet):
        """
        Supprime un des sommets du graphe en le supprimant de la liste des sommets
        et en supprimant toute la ligne et la colonne associé à ce sommet.
        
        Pré-condition : nom_sommet existe deja dans le graphe, sinon ne rien faire.
        
        Effets de bord: modifie self.mat et self.sommets
        """
        pass
        
    def ajouter_lien(self, sommet1, sommet2, oriente = False):
        """
        Ajoute un lien entre le sommet 1 et le sommet 2, ajoute une arête si oriente = False,
        un arc allant de sommet1 vers sommet2 si oriente = True
        
        Effet de bord: modifie self.mat
        """
        pass
            
    def supprime_lien(self, sommet1, sommet2, oriente = False):
        """
        Supprime le lien entre le sommet 1 et le sommet 2, supprime tout le lien oriente = False,
        supprime le sens sommet1 vers sommet2 si oriente = True
        
        Effet de bord: modifie self.mat
        """
        pass
            
    def successeurs(self, sommet):
        """
        Renvoies la liste des successeurs de sommet dans le graphe grace à la matrice d'adjacence
        
        Pré-condition : sommet est présent dans le graphe
        """
        pass
    
    def predecesseurs(self , sommet):
        """
        Renvoies la liste des predecesseurs de sommet dans le graphe grace a la matrice d'adjacence
        
        Pré-condition : sommet est présent dans le graphe
        """
        pass
    
    def voisins(self, sommet):
        """
        Renvoies la liste des voisins de sommet dans le graphe
        Les successeurs et prédécesseurs sont tous voisin de sommet.
        
        Pré-condition : sommet est présent dans le graphe
        """
        pass
    
     def degre_sortant(self, sommet):
        """
        Renvoie le degré sortant du sommet passé en argument
        """
        pass
    
    def degre_entrant(self, sommet):
        """
        Renvoie le degré du sommet passé en argument
        """
        pass
    
    def degre(self, sommet):
        """
        Renvoie le degré du sommet passé en argument
        """
        pass
        
    def matrice_to_liste(self):
        """
        Renvoies les listes de successeurs correspondant au graphe
        
        Les clés seront les noms des sommets
        """
        pass
    
    def affiche_graphe(self):
        """
        Genere la visualisation du graphe a l'aide de networkx.
        
        Le choix de la représentation utilisé est libre.
        """
        pass
                