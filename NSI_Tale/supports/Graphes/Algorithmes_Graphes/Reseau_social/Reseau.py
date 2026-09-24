from Pile import Pile1
from File import File1
from graphviz import Digraph

class Reseau:
    """
    Une classe représentant un graphe.
    """
    
    def __init__(self, noeuds, aretes):
        """
        Initialise un réseau social sous forme de dictionnaire avec les utilisateurs et relations donnés.

        Paramètres:
        -----------
        users : liste
            Une liste d'utilisateurs dans le réseau social.
            Les sommets de mon graphe.
        relations : liste de tuples
            Une liste de tuples représentant les amis et demande d'amis dans le réseau social, où chaque tuple est de la forme (user1, user2) pour indiquer un arc entre user1 et user2.
            Une arête est représentée par 2 couples (i, j) et (j, i)
        """
        self.noeuds = noeuds
        self.relations = aretes
        pass
        
    def parcours_profondeur(self, start):
        """
        Méthode pour effectuer un parcours en profondeur d'un graphe à partir du sommet de départ spécifié.

        Args:
            start: Le sommet de départ à partir duquel le parcours en profondeur commence.

        Returns:
            Une liste des sommets visités dans l'ordre du parcours en profondeur.
        """
        pass
    
    def parcours_largeur(self, start):
        """
        Méthode pour effectuer un parcours en largeur d'un graphe à partir du sommet de départ spécifié.

        Args:
            start: Le sommet de départ à partir duquel le parcours en largeur commence.

        Returns:
            Une liste des sommets visités dans l'ordre du parcours en largeur.
        """
        pass
    
    def possede_relation_commune(self, start, end):
        """
        Recherche un chemin entre deux sommets du graphe en utilisant un algorithme de parcours.

        Args:
            start: le sommet de départ
            end: le sommet d'arrivée

        Returns:
            True si il y a un chemin entre start et end ( dans n'importe quel sens ), False sinon
        """
        pass 
   
       
    
    def affiche(self):
        """
        Affiche le graphe avec la librairie Graphviz.
        """
        dot = Digraph('Graphe', format='pdf', graph_attr = dict(rankdir='RL', concentrate= 'true'))
        
        for i,j in self.relations:
            if (j,i) in self.relations:
                dot.edge(i, j, dir="none")
            else:
                dot.edge(i, j)
                
        dot.view()