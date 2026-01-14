from morpion import JeuMorpion
from db_manager import DBManager

def boucle_jeu(db, joueur_x_id, joueur_o_id, nom_x, nom_o):
    """Contient la boucle principale d'une partie de Morpion."""
    
    #Demander la position (de 1 à 9) et la convertir en indice (0 à 8)           
    # Fin de partie : Enregistrement et affichage
    # Gérer l'enregistrement du score et l'affichage du résultat    
        # Le perdant n'enregistre rien, ou on pourrait enregistrer une défaite, mais pour ce TP, on enregistre juste les victoires.   
    
        # On pourrait enregistrer un nul pour les deux joueurs, mais pour simplifier, enregistrons pour le premier joueur.


def main():
    """Fonction principale du programme."""
    db = DBManager()

    #Demander le nom des deux joueurs et récupérer leurs IDs           
        # Afficher le classement après chaque partie
        
if __name__ == "__main__":
    # Lancement du jeu
    main()