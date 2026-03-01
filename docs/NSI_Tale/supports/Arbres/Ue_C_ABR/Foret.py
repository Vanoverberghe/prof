import graphviz
import random

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None
        
class ArbreBinaireRecherche:
    def __init__(self):
        self.racine = None
        
    def est_vide(self):
        return self.racine is None

    def sous_arbre_gauche(self):
        return self.racine.gauche
    
    def sous_arbre_droit(self):
        return self.racine.droite

    def inserer(self, valeur):
        self.racine = self._inserer(self.racine, valeur)

    def _inserer(self, racine, valeur):
        if racine is None:
            return Noeud(valeur)
        
        if valeur < racine.valeur:
            racine.gauche = self._inserer(racine.gauche, valeur)
        elif valeur > racine.valeur:
            racine.droite = self._inserer(racine.droite, valeur)

        return racine

    def rechercher(self, valeur):
        return self._rechercher(self.racine, valeur)

    def _rechercher(self, racine, valeur):
        if racine is None or racine.valeur == valeur:
            return racine
        
        if valeur < racine.valeur:
            return self._rechercher(racine.gauche, valeur)
        else:
            return self._rechercher(racine.droite, valeur)

    def parcours_infixe(self):
        resultats = []
        self._parcours_infixe(self.racine, resultats)
        return resultats

    def _parcours_infixe(self, racine, resultats):
        if racine:
            self._parcours_infixe(racine.gauche, resultats)
            resultats.append(racine.valeur)
            self._parcours_infixe(racine.droite, resultats)
        
    def panneaux(self):
        return f"<- Gauche : {self.sous_arbre_gauche().valeur if self.sous_arbre_gauche() is not None else 'X'}, -> Droite : {self.sous_arbre_droit().valeur if self.sous_arbre_droit() is not None else 'X'}"
    
    def courant(self):
        return self.racine.valeur
    
    def avancer_gauche(self):
        if self.sous_arbre_gauche() is None:
            print("C'est un cul de sac!")
            return
        self.racine = self.sous_arbre_gauche()
        
    def avancer_droit(self):
        if self.sous_arbre_droit() is None:
            print("C'est un cul de sac!")
            return
        self.racine = self.sous_arbre_droit()
        
    def sorcier(self):
        print(f"Bonjour aventurier(e), le coffre se trouve près du caillou {random.choice(self.parcours_infixe())}")
        
        
        
import random

class NoeudArbreBinaire:
    def __init__(self, valeur, gauche=None, droite=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite

class ArbreBinaire:
    def __init__(self, racine=None):
        self.racine = racine
        
    def est_vide(self):
        return self.racine is None

    def inserer_aleatoire(self, valeur):
        nouveau_noeud = NoeudArbreBinaire(valeur)
        if self.racine is None:
            self.racine = nouveau_noeud
        else:
            self._inserer_aleatoire(self.racine, nouveau_noeud)
            
    def sous_arbre_gauche(self):
        return self.racine.gauche
    
    def sous_arbre_droit(self):
        return self.racine.droite

    def _inserer_aleatoire(self, noeud, nouveau_noeud):
        if random.choice([True, False]):  # Choix aléatoire entre gauche et droite
            if noeud.gauche is None:
                noeud.gauche = nouveau_noeud
            else:
                self._inserer_aleatoire(noeud.gauche, nouveau_noeud)
        else:
            if noeud.droite is None:
                noeud.droite = nouveau_noeud
            else:
                self._inserer_aleatoire(noeud.droite, nouveau_noeud)

    def parcours_infixe(self, racine):
        resultats = []
        self._parcours_infixe(racine, resultats)
        return resultats

    def _parcours_infixe(self, noeud, resultats):
        if noeud:
            self._parcours_infixe(noeud.gauche, resultats)
            resultats.append(noeud.valeur)
            self._parcours_infixe(noeud.droite, resultats)
        
    def panneaux(self):
        return f"<- Gauche : {self.sous_arbre_gauche().valeur if self.sous_arbre_gauche() is not None else 'X'}, -> Droite : {self.sous_arbre_droit().valeur if self.sous_arbre_droit() is not None else 'X'}"
    
    def courant(self):
        return self.racine.valeur
    
    def avancer_gauche(self):
        if self.sous_arbre_gauche() is None:
            print("C'est un cul de sac!")
            return
        self.racine = self.sous_arbre_gauche()
    
    def avancer_droit(self):
        if self.sous_arbre_droit() is None:
            print("C'est un cul de sac!")
            return
        self.racine = self.sous_arbre_droit()
    
    def sorcier(self):
        print(f"Bonjour aventurier(e), le coffre se trouve près du caillou {random.choice(self.parcours_infixe(self.racine))}")
    


# Exemple d'utilisation
FORET_2 = ArbreBinaireRecherche()
FORET = ArbreBinaire()

valeurs = [i for i in range(1,100)]

random.shuffle(valeurs)

for valeur in valeurs[:15]:
    FORET_2.inserer(valeur)
    FORET.inserer_aleatoire(valeur)
    
FORET_DEBUT = FORET
FORET_2_DEBUT = FORET_2

FORET.sorcier()

VALEUR_RECHERCHEE = random.choice(valeurs[:20])
