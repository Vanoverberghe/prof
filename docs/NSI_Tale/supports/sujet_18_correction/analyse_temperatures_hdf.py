# =================================================================================#
# Données de test
donnees_test = [
    # Lille - Données sur 2010 et 2020
    {'date': '2010-01-15', 'station': 'Lille',   'temperature': 4.2},
    {'date': '2010-06-20', 'station': 'Lille',   'temperature': 18.5},
    {'date': '2011-03-10', 'station': 'Lille',   'temperature': 9.1},
    {'date': '2020-02-14', 'station': 'Lille',   'temperature': 7.8},
    {'date': '2020-08-22', 'station': 'Lille',   'temperature': 22.3},
    {'date': '2021-05-30', 'station': 'Lille',   'temperature': 17.6},

    # Amiens - Données sur 2010 et 2020
    {'date': '2015-04-10', 'station': 'Amiens',  'temperature': 12.4},
    {'date': '2020-07-15', 'station': 'Amiens',  'temperature': 21.0},
    {'date': '2021-09-20', 'station': 'Amiens',  'temperature': 16.5},

    # Calais - Données uniquement sur 2020
    {'date': '2020-03-15', 'station': 'Calais',  'temperature': 9.8},
    {'date': '2021-07-10', 'station': 'Calais',  'temperature': 19.2},
    {'date': '2022-11-25', 'station': 'Calais',  'temperature': 8.5},
]

# =================================================================================#
#  Question 1 : Ecrire le code de votre fonction température_moyenne

def temperature_moyenne(station, donnees):
    total = 0
    eff = 0 # On compte à la main puisque qu'on ne peut pas connaitre l'effectif d'une seule station grace a len
    for d in donnees:
        if d['station'] == station:
            total += d['temperature']
            eff += 1
    if eff == 0:
        return None
    return total/eff

# =================================================================================#
#  Question 2 : Ecrire le code de votre fonction detection_anomalies

def detecter_anomalies(station, seuil, donnees):
    res = []
    temp = temperature_moyenne(station, donnees)
    if temp is None:
        return res
    for d in donnees:
        if d['station'] == station and abs(temp - d['temperature']) > seuil:
            res.append(d['date'])
    return res
# =================================================================================#
# code de la fonction evolution_par_decennie à corriger dans la question 4:


def evolution_par_decennie(station, donnees):
    """
    Calcule l'évolution des températures moyennes par décennie pour une station.

    ATTENTION: Cette fonction contient un bug volontaire à détecter et corriger.

    Arguments:
        station (str): Nom de la station météo (ex: 'Lille', 'Amiens')
        donnees (list): Liste de dictionnaires de relevés

    Renvoie:
        dict: Dictionnaire {décennie : température_moyenne}
              ex: {2010: 11.2, 2020: 15.8}
              Renvoie un dictionnaire vide si la station n'existe pas
    """
    # Filtrage des relevés pour la station
    releves_station = [r for r in donnees if r['station'] == station]

    if not releves_station:
        return {}

    # Regroupement par décennie
    temperatures_par_decennie = {}

    for releve in releves_station:
        # Extraction de l'année de la date (format: 'YYYY-MM-DD')
        annee = int(releve['date'].split('-')[0])

        # Calcul de la décennie
        decennie = (annee // 10)          # BUG : devrait être (annee // 10) * 10

        if decennie not in temperatures_par_decennie:
            temperatures_par_decennie[decennie] = []

        temperatures_par_decennie[decennie].append(releve['temperature'])

    # Calcul des moyennes
    moyennes = {}
    for decennie, temperatures in temperatures_par_decennie.items():
        moyennes[decennie] = round(sum(temperatures) / len(temperatures), 2)

    return moyennes


# =================================================================================#
#  Exercice 2.1 :
"""
Tests
À compléter par le candidat dans le cadre de la question 3
"""


def test_station_inexistante():
    """
    Test 1 : Tester une station qui n'existe pas

    À compléter:
    1. Appeler evolution_par_decennie avec une station inexistante
    2. Vérifier que le résultat est un dictionnaire vide
    """
    assert evolution_par_decennie('Denain', donnees_test) == {}
    


def test_une_seule_decennie():
    """
    Test 2: Tester une station avec données sur une seule décennie

    À compléter:
    1. Appeler evolution_par_decennie avec la station appropriée
    2. Vérifier que le résultat ne contient qu'une seule décennie (2020)
    3. Vérifier la température moyenne
    """
    d = evolution_par_decennie('Calais', donnees_test) 
    assert list(d.keys()) == [2020]
    assert d[2020] == temperature_moyenne('Calais', donnees_test)

def test_plusieurs_decennies():
    """
    Test 3 : Tester une station avec données sur plusieurs décennies

    À compléter:
    1. Appeler evolution_par_decennie avec la station appropriée
    2. Vérifier que le résultat contient bien les clés 2010 et 2020
    3. Vérifier que les températures moyennes sont cohérentes
    """
    d = evolution_par_decennie('Lille', donnees_test)
    
    # présence des deux décennies
    assert 2010 in d
    assert 2020 in d

    # deux décennies exactement
    assert len(d) == 2

    # les valeurs sont numériques
    assert isinstance(d[2010], (int, float))
    assert isinstance(d[2020], (int, float))
    
    
