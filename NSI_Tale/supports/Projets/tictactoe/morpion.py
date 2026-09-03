class JeuMorpion:
    """Représente le jeu du Morpion."""
    
    def __init__(self):
        # Initialiser le plateau (liste de 9 éléments)
        self.plateau = ...
        self.joueur_actuel = ...
        self.partie_finie = False
     
    def afficher_plateau(self):
        """Affiche le plateau de jeu formaté."""
                
    def faire_coup(self, position):
        """Joue un coup à la position donnée (0 à 8)."""
    def verifier_victoire(self):
        """Vérifie si le joueur actuel a gagné."""        
        
    def verifier_nul(self):
        """Vérifie si le plateau est plein sans victoire."""
        
    def reset(self):
        """Réinitialise le plateau pour une nouvelle partie."""