# ///////////////////////////////////////////////////////////////////////////
# FONCTIONS DONNEES
# ///////////////////////////////////////////////////////////////////////////

def recupere_donnees_fichier_csv(nom_fichier):
    """ Fonction qui récupère les données relevées par la bouée océanique sans les en-têtes de la 1ère ligne """
    profondeurs = []                                # Initialisation des listes de valeurs relevées
    pressions = []
    salinites = []
    longitudes = []
    latitudes = []
    # Ouverture du fichier csv en mode "read"
    contenu_fichier = open(nom_fichier, 'r')
    # Supprime la 1ère ligne avec les en-têtes
    contenu_fichier.readline()
    # Parcours des lignes du fichier csv contenant les données relevées
    for ligne in contenu_fichier.readlines():
        # rstrip() supprime les \n et espaces en fin de ligne
        ligne = ligne.rstrip()
        # création d'une listeValeurs. split(";") sépare les valeurs grâce au ;
        listeValeurs = ligne.split(";")
        # conversion string en int de la profondeur et insertion dans la liste correspondante
        profondeurs.append(int(listeValeurs[0]))
        # conversion string en int de la pression et insertion dans la liste correspondante
        pressions.append(int(listeValeurs[1]))
        # conversion string en float de la salinité et insertion dans la liste correspondante
        salinites.append(float(listeValeurs[2]))
        # conversion string en float de la longitude et insertion dans la liste correspondante
        longitudes.append(float(listeValeurs[3]))
        # conversion string en float de la latitude et insertion dans la liste correspondante
        latitudes.append(float(listeValeurs[4]))
    return profondeurs, pressions, salinites, longitudes, latitudes


def genere_gpx(liste_longitudes, liste_latitudes):
    """ Fonction qui génère un fichier de données géographiques au format standard international GPX
        Ce fichier est visionnable ensuite dans différents logiciels de cartographie
    """
    assert len(liste_longitudes) == len(liste_latitudes), "Les listes doivent être de même longueur"
    fichier_gpx = open(
        'bouee_ocean.gpx', 'w')    # Création et ouverture du fichier gpx en mode "write"
    entete_fichier = '<?xml version="1.0" encoding="UTF-8"?>\n'
    entete_fichier += '<gpx version="1.1" creator="BoueeOcean">\n'
    entete_fichier += '<trk>\n'
    entete_fichier += '<name>Trajectoire bouee oceanographique</name>\n'
    entete_fichier += '<trkseg>\n'
    # Ecriture du contenu de la variable entete_fichier dans le fichier gpx
    fichier_gpx.write(entete_fichier)
    for i in range(len(liste_longitudes)):
        corps_fichier = f'<trkpt lat="{liste_latitudes[i]}" lon="{liste_longitudes[i]}">\n'
        corps_fichier += f'<name>Point {i}</name>\n'
        corps_fichier += '</trkpt>\n'
        fichier_gpx.write(corps_fichier)
    bas_fichier = '</trkseg>\n'
    bas_fichier += '</trk>\n'
    bas_fichier += '</gpx>' # ajout de la balise fermée
    fichier_gpx.write(bas_fichier)
    fichier_gpx.close()                         # Fermeture du fichier gpx


# ///////////////////////////////////////////////////////////////////////////
# TRAVAIL DEMANDE
# ///////////////////////////////////////////////////////////////////////////

# QUESTION 1
# Compléter ici
profondeurs, pressions, salinites, longitudes, latitudes = recupere_donnees_fichier_csv("releves_bouee_ocean.csv")

# QUESTION 2
def conversion_Pa_en_bar(liste_pressions):
    res = []
    for pression in liste_pressions:
        res.append(round(pression/100000, 4))
    return res

print(conversion_Pa_en_bar(pressions))


# QUESTION 3
def profondeur_la_plus_salee(liste_profondeurs, liste_salinites):
    maxi = 0
    profondeurs = []
    for i in range(len(liste_profondeurs)):
        if liste_salinites[i] > maxi:
            maxi = liste_salinites[i]
            profondeurs = [liste_profondeurs[i]]
        elif liste_salinites[i] == maxi:
            profondeurs.append(liste_profondeurs[i])
    return maxi, profondeurs

# QUESTION 5

genere_gpx(longitudes, latitudes)
