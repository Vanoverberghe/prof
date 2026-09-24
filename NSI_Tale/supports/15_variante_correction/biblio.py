# -----------------------------------------------------------------------------
# Numéros de téléphones
# Question 1 : nettoyage des numéros de téléphone

# Écrire la fonction normalisation_tel ici

def normalisation_tel(tel: str) -> str:
    res = ''
    for caractere in tel:
        if caractere in '0123456789':
            res += caractere
    return res

import sqlite3


def test_normalisation_tel():
    """
    Tous les tests doivent passer...
    """
    assert normalisation_tel("06 12 34 56 78") == "0612345678"
    assert normalisation_tel("07.89.01.23.45") == "0789012345"
    assert normalisation_tel("(0)6.55.44.33.22") == "0655443322"
    assert normalisation_tel("0.6.12.99.90.12") == "0612999012"
    assert normalisation_tel("06-23-45-67-89") == "0623456789"
    assert normalisation_tel("0623145896 dupuis") == "0623145896"
    assert normalisation_tel("061299901") == "061299901"
    assert normalisation_tel("06129990123") == "06129990123"
    print("Les tests de la fonction normalisation_tel sont passés")


# -----------------------------------------------------------------------------
# Question 2 : validation des numéros de téléphone


def validation_tel(tel):
    """
    Validation des numéros de téléphone portable français
    selon les conditions spécifiées.
    :param tel: numéro de téléphone (déjà normalisé)
    :return: True si le numéro est valide, False sinon
    """
    if len(tel) != 10:
        return False
    if tel[0] != "0":
        return False
    if tel[1] != "6" and tel[1] != "7":
        return False
    return True


# Écrire votre jeu de tests permettant
# de vérifier le bon fonctionnement de la fonction.
def test_validation_tel(tel):
    assert validation_tel('0648956578')
    assert validation_tel('0726589357')
    assert not validation_tel('0320798565')
    assert not validation_tel('3244')
    assert not validation_tel('083663636363')

# -----------------------------------------------------------------------------
# Détermination de la liste des emprunts en retard
# Question 3 : interrogation de la base de données

DB_PATH = "biblio.sqlite"


def adherents_livres_empruntes_apres(date):
    """
    Renvoie les noms et prénoms des adhérents ayant emprunté un livre
    après la date `date`, triés par ordre alphabétique de noms puis prénoms.

    :param date: date d'emprunt minimale (format AAAAMMJJ)
    :return: liste [(nom_adherent, prenom_adherent)]
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    resultat = cursor.execute(
        """
    SELECT adherent.nom, adherent.prenom
    FROM adherent
        JOIN emprunt ON adherent.id = emprunt.id_adherent
    WHERE emprunt.date_emprunt > ?
    ORDER BY adherent.nom, adherent.prenom;
    """,
        (date,),
    )
    return list(resultat)


def emprunts_en_retard(date):
    """
    Renvoie les emprunts de livres non rendus dont la date d'emprunt
    est antérieure à la date `date`.

    Un emprunt est "en retard" si :
      - le livre n'a pas été rendu (date_retour est NULL)
      - la date d'emprunt est strictement antérieure à `date`

    :param date: date limite (format AAAAMMJJ)
    :return: liste [(id_emprunt, titre_livre, tel_adherent, date_emprunt)]
             triée par id_adherent puis date_emprunt croissants
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    resultat = cursor.execute(
    """
    SELECT emprunt.id, livre.titre, adherent.telephone, emprunt.date_emprunt
    FROM emprunt
    JOIN adherent ON adherent.id = emprunt.id_adherent
    JOIN livre ON livre.id = emprunt.id_livre
    WHERE emprunt.date_emprunt < ? AND date_retour is NULL
    ORDER BY emprunt.id_adherent, emprunt.date_emprunt;
    """,
        (date,),
    )
    return list(resultat)


def test_emprunts_en_retard():
    emprunts = emprunts_en_retard("20251101")
    assert len(emprunts) == 31
    assert emprunts[0] == (60, "Fahrenheit 451", "06 12 34 56 78", "20250928")
    assert emprunts[1] == (2, "1984", "06 12 34 56 78", "20251026")
    assert emprunts[2] == (4, "Astérix et Cléopâtre", "07.89.01.23.45", "20251021")
    assert emprunts[3] == (6, "Sherlock Holmes", "(0)6.55.44.33.22", "20251028")
    assert emprunts[4] == (8, "L'Étranger", "0784512369", "20251024")
    assert emprunts[5] == (9, "Germinal", "06-23-45-67-89", "20251016")
    assert emprunts[6] == (11, "Le Seigneur des anneaux", "03 20 45 67 89", "20251029")
    assert emprunts[7] == (13, "La Nuit des temps", "0.7.12.34.56.78", "20251027")
    assert emprunts[8] == (16, "Fondation", "01.45.78.12.36", "20251025")
    assert emprunts[9] == (18, "Mort sur le Nil", "07 98 76 54 32", "20251031")
    
    # Le test sur l'ordre était mal écrit dans le sujet, ca ne respectait pas ce qu'on demandait

    print("Les tests de la fonction emprunts_en_retard sont passés")


test_emprunts_en_retard()


# -----------------------------------------------------------------------------
# Question 4 : détermination de l'emprunt le plus ancien par adhérent


def emprunt_le_plus_recent(emprunts):
    """
    Renvoie un dictionnaire ayant pour clef le numéro de téléphone des adhérents,
    et dont la valeur associée est l'emprunt le plus RÉCENT (date la plus grande)
    pour chaque adhérent identifié par son numéro de téléphone.

    Chaque emprunt est un tuple :
    (id_emprunt, titre_livre, tel_adherent, date_emprunt)
    """
    plus_recent = {}
    for emprunt in emprunts:
        tel = emprunt[2]
        date = emprunt[3]
        if tel not in plus_recent:
            plus_recent[tel] = emprunt
        elif date > plus_recent[tel][3]:   # ← bug ici, on voulait les dates les plus grandes ( > et non pas < )
            plus_recent[tel] = emprunt
    return plus_recent


def test_emprunt_le_plus_recent():
    emprunts_pour_test = [
        (60, "Fahrenheit 451", "06 12 34 56 78", "20250928"),
        (2,  "1984",           "06 12 34 56 78", "20251026"),
        (4,  "Astérix et Cléopâtre", "07.89.01.23.45", "20251021"),
        (6,  "Sherlock Holmes", "(0)6.55.44.33.22", "20251028"),
        (8,  "L'Étranger",     "0784512369",     "20251024"),
        (9,  "Germinal",       "06-23-45-67-89", "20251016"),
        (11, "Le Seigneur des anneaux", "03 20 45 67 89", "20251029"),
        (13, "La Nuit des temps", "0.7.12.34.56.78", "20251027"),
        (16, "Fondation",      "01.45.78.12.36", "20251025"),
        (18, "Mort sur le Nil","07 98 76 54 32", "20251031"),
    ]

    resultat = emprunt_le_plus_recent(emprunts_pour_test)

    assert resultat == {
        "06 12 34 56 78":    (2,  "1984",           "06 12 34 56 78", "20251026"),
        "07.89.01.23.45":    (4,  "Astérix et Cléopâtre", "07.89.01.23.45", "20251021"),
        "(0)6.55.44.33.22":  (6,  "Sherlock Holmes", "(0)6.55.44.33.22", "20251028"),
        "0784512369":        (8,  "L'Étranger",     "0784512369",     "20251024"),
        "06-23-45-67-89":    (9,  "Germinal",       "06-23-45-67-89", "20251016"),
        "03 20 45 67 89":    (11, "Le Seigneur des anneaux", "03 20 45 67 89", "20251029"),
        "0.7.12.34.56.78":   (13, "La Nuit des temps", "0.7.12.34.56.78", "20251027"),
        "01.45.78.12.36":    (16, "Fondation",      "01.45.78.12.36", "20251025"),
        "07 98 76 54 32":    (18, "Mort sur le Nil","07 98 76 54 32", "20251031"),
    }
    print("Les tests de la fonction emprunt_le_plus_recent sont passés")
