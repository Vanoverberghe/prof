##############################################################################
# Jeux de données fournis                                                    #
##############################################################################
from livres import livres
from emprunts import emprunts

##############################################################################
# Écrire le code de la fonction anciennete_moyenne de la question 1          #
##############################################################################

def anciennete_moyenne(livres: list) -> float:
    if livres == []:
        return None
    else:
        total = 0
        for livre in livres:
            total += 2026-livre.annee
        return total/len(livres)
    

##############################################################################
# Écrire le code de la fonction dictionnaire_emprunts de la question 2       #
##############################################################################

def dictionnaire_emprunts(livres: list, emprunts: list) -> dict:
    d = {l.titre: [] for l in livres}
    for emp in emprunts:
        if emp['titre'] in d:
            d[emp['titre']].append(emp)
    return d

##############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4      #
##############################################################################

def supprimer_emprunts_courts(liste_emprunts):
    """
    Supprime de la liste tous les emprunts dont la durée
    est strictement inférieure à 10 jours.
    """
    for emprunt in liste_emprunts[:]:
        if emprunt['duree'] < 10:
            liste_emprunts.remove(emprunt)
    return liste_emprunts

def test_supprimer():
    emprunts_test = [
        {'titre': 'Livre A', 'adherent': 'Alice', 'duree':  4, 'note': 5},
        {'titre': 'Livre B', 'adherent': 'Alice', 'duree':  5, 'note': 4},
        {'titre': 'Livre C', 'adherent': 'Alice', 'duree': 15, 'note': 3},
        {'titre': 'Livre D', 'adherent': 'Alice', 'duree':  7, 'note': 4},
        {'titre': 'Livre E', 'adherent': 'Alice', 'duree':  8, 'note': 5},
    ]

    supprimer_emprunts_courts(emprunts_test)

    print("Résultat après suppression des emprunts courts :")
    for e in emprunts_test:
        print(f"{e['titre']} — durée : {e['duree']} jour(s)")


emprunts_test = [
    {"titre": "Les Misérables", "adherent": "Alice",   "duree": 28, "note": 4},
    {"titre": "L'Étranger",     "adherent": "Bruno",   "duree":  7, "note": 5},
    {"titre": "Les Misérables", "adherent": "Camille", "duree": 40, "note": 4},
]
from livres import Livre
livres_test = [
    Livre("Les Misérables", "Victor Hugo",  1862, 1488, "roman historique"),
    Livre("L'Étranger",     "Albert Camus", 1942,  186, "philosophique"),
    Livre("Germinal",       "Émile Zola",   1885,  591, "roman social"),
]