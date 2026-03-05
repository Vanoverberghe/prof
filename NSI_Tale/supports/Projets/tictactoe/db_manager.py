import sqlite3

class DBManager:
    """Gère la connexion à la base de données et les opérations CRUD."""
    
    def __init__(self, db_name="morpion.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.creer_tables()
        
    def connect(self):
        """Établit la connexion à la base de données."""
        # Établir la connexion        
        
    def creer_tables(self):
        """Crée les tables Joueurs et Scores si elles n'existent pas."""
        try:
            # Créer la table Joueurs (id INTEGER PRIMARY KEY, nom TEXT UNIQUE)   
            
            # Créer la table Scores (id INTEGER PRIMARY KEY, joueur_id INTEGER, resultat TEXT (Victoire/Nul), FOREIGN KEY)




    def get_or_create_joueur(self, nom_joueur):
        """Récupère l'ID d'un joueur ou le crée s'il n'existe pas."""
        # Chercher le joueur
        # Insérer le nouveau joueur
    def enregistrer_score(self, joueur_id, resultat):
        """Enregistre le résultat d'une partie pour un joueur (e.g., 'Victoire', 'Nul')."""
        # Insérer le score
   def get_classement(self):
        """Affiche le classement (nombre de victoires par joueur)."""
        # Requête SQL pour compter les 'Victoire' et joindre avec Joueurs        

    def close(self):
        """Ferme la connexion à la base de données."""

if __name__ == '__main__':
    # Testez votre classe DBManager
    db = DBManager()
    joueur1_id = db.get_or_create_joueur("Alice")
    joueur2_id = db.get_or_create_joueur("Bob")
    
    db.enregistrer_score(joueur1_id, "Victoire")
    db.enregistrer_score(joueur1_id, "Nul")
    db.enregistrer_score(joueur2_id, "Victoire")
    db.enregistrer_score(joueur2_id, "Victoire")
    
    classement = db.get_classement()
    print("\n🏆 Classement des Victoires :")
    for nom, victoires in classement:
        print(f"- {nom} : {victoires} victoires")
    
    db.close()